from queue import Queue
from flask import Flask, jsonify, request, flash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import pytz
import queue
import uuid
from flask_jwt_extended import JWTManager
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from flask_login import login_user, UserMixin, LoginManager, logout_user


# configuration
DEBUG = True

task_queue = queue.Queue()

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lida:123@localhost:5432/db_ps'
app.config['SECRET_KEY'] = '548b2563213f3c0c1bcb915a'
jwt = JWTManager(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
ma = Marshmallow(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    print("user_loader", User.query.get(int(user_id)))
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    components = db.relationship('Components', backref='user_components', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, user_text_password):
        self.password_hash = bcrypt.generate_password_hash(user_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


# schema
class UserSchema(ma.SQLAlchemySchema):
    class  Meta:
        fields = ("id", "username", "password")
        
# schema obj
user_schema = UserSchema() 
userss_schema = UserSchema(many=True)

# table
class Components(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    ctype = db.Column(db.String(length=150), db.ForeignKey('comptypes.name'))
    qrcode = db.Column(db.String(length=180), nullable=False, unique=True)
    addts = db.Column(db.DateTime(), nullable=False)
    cstat = db.Column(db.String(length=30), default='новый')
    statts = db.Column(db.DateTime(), nullable=False)
    tests = db.Column(db.String(length=150), default='Отсутствует')
    rem = db.Column(db.String(length=1024), default='Отсутствует')
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    conclusion = db.Column(db.String(length=1024), nullable=False, default='-')
    server_id = db.Column(db.Integer(), db.ForeignKey('servers.id'))

    def __init__(self, ctype, qrcode, addts, cstat, statts, tests, rem, owner, conclusion):
        self.ctype = ctype
        self.qrcode = qrcode
        self.addts = addts
        self.cstat = cstat
        self.statts = statts
        self.tests = tests
        self.rem = rem
        self.owner = owner
        self.conclusion = conclusion

# schema
class ComponentSchema(ma.SQLAlchemySchema):
    class  Meta:
        fields = ("id", "ctype", "qrcode", "addts", "cstat", "statts", "tests", "rem", "owner", "conclusion", "server_id")
        
# schema obj
component_schema = ComponentSchema() 
components_schema = ComponentSchema(many=True)

# table
class Comptypes(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=150), nullable=False, unique=True)
    count = db.Column(db.Integer(), nullable=False)
    decoding = db.Column(db.String(length=150), nullable=False, unique=True)
    components = db.relationship('Components', backref='type_of_components')

    def __init__(self, name, count, decoding, components):
        self.name = name
        self.count = count
        self.decoding = decoding
        self.components = components

# schema
class ComptypeSchema(ma.SQLAlchemySchema):
    class  Meta:
        fields = ("id", "name", "count", "decoding")  

# schema obj
comptype_schema = ComptypeSchema() 
comptypes_schema = ComptypeSchema(many=True)

class Servers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    qrcode = db.Column(db.String(length=180))
    asts = db.Column(db.DateTime, nullable=False, default=datetime.date)
    vts = db.Column(db.DateTime, default=datetime.date)
    """ aid = db.Column(db.Integer(), db.ForeignKey('plant.id')) """
    """ vid = db.Column(db.Integer(), primary_key=True) """
    cmps = db.relationship('Components', backref='components')
    """ tstts = db.Column(db.DateTime, default=datetime.utcnow) """
    """ tstres = db.Column(db.String(length=2048)) """
    sstat = db.Column(db.String(length=30), default='новый')
    """ snum = db.Column(db.String(length=30), unique=True) """

    def __init__(self, qrcode, asts, vts, cmps, sstat):
        self.qrcode = qrcode
        self.asts = asts
        self.vts = vts
        self.cmps = cmps
        self.sstat = sstat

# schema
class ServerSchema(ma.SQLAlchemySchema):
    class  Meta:
        fields = ("id", "qrcode", "asts", "vts", "sstat") 

# schema obj
server_schema = ServerSchema() 
servers_schema = ServerSchema(many=True)

#  ------------------ get all servers
@app.route('/app/server_list', methods=['GET'])
def get_servers():
    all_servers = Servers.query.all()
    print(all_servers)
    data = []
    for p in all_servers:
        data += [{'qrcode': p.qrcode}]
        print(data)
    return  servers_schema.jsonify(all_servers)

#  ------------------ get all components
@app.route('/app/component_list', methods=['GET'])
def get_components():
    all_components = Comptypes.query.all()
    return  comptypes_schema.jsonify(all_components)

@app.route('/app/component/<id>/', methods=['GET'])
def component_details(id):

    component_detail = Comptypes.query.get(id)
    data = [{'id': p.id, 'decoding': component_detail.decoding, 'conclusion': p.conclusion, 'qrcode': p.qrcode, 'cstat': p.cstat, 'addts': p.addts, 'statts': p.statts, 'tests': p.tests, 'rem': p.rem} for p in component_detail.components]
    for p in component_detail.components:
        print(p.addts)
    if component_detail:
        return jsonify(data)
    else:
        return "No component with that ID"

@app.route('/app/current_component/<id>/', methods=['GET'])
def current_component(id):

    current_component = Components.query.filter_by(id=id).first()
    current_comptype = Comptypes.query.filter_by(name=current_component.ctype).first()
    data = {'id': current_component.id, 'conclusion': current_component.conclusion, 'qrcode': current_component.qrcode, 'cstat': current_component.cstat, 'tests': current_component.tests, 'rem': current_component.rem, 'ctype_id': current_comptype.id, 'ctype_name': current_comptype.name, 'decoding': current_comptype.decoding }
    if current_component:
        return jsonify(data)
    else:
        return "No component with that ID"

#  ------------------ post or add new 
@app.route('/app/create_component/<username>/', methods=['GET', 'POST'])
def add_component(username):
    print("USERNAME: ", username)
    ctype = request.json['ctype']
    qrcode = request.json['qrcode']
    errors = ""
    if qrcode == "":
        errors = '500'
        return errors
    result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
    if result != None:
        errors = '505'
        return errors
    user = User.query.filter_by(username=username).first()
    addts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cstat = 'новый'
    statts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tests = 'Отсутствует'
    rem = 'Отсутствует'
    owner = user.id
    conclusion = '-'

    components = Components(ctype, qrcode, addts, cstat, statts, tests, rem, owner, conclusion)
    db.session.add(components)
    db.session.commit()

    comptypes = Comptypes.query.filter_by(name=ctype).first()
    comptypes.count = comptypes.count + 1
    db.session.add(comptypes)
    db.session.commit()

    return component_schema.jsonify(components)

@app.route('/app/add_chassis', methods=['GET', 'POST'])
def add_chassis():
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server_to_create = Servers(qrcode=result.qrcode,
                                   asts=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                   vts =datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                   sstat='новый',
                                   cmps=[result]
                                  )
        server_to_create.cstat = 'установлен в изделие'
        result.cstat = 'установлен в изделие'
        db.session.add(server_to_create)
        db.session.add(result)
        db.session.commit()

        return jsonify(server_to_create.id)


@app.route('/app/get_chassis/<int:server_id>/', methods=['GET', 'POST'])
def get_chassis(server_id):
        return jsonify(server_id)

@app.route('/app/add_fan140/<int:server_id>/', methods=['GET', 'POST'])
def add_fan140(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.id)

@app.route('/app/add_fan_control_board/<int:server_id>/', methods=['GET', 'POST'])
def add_fan_control_board(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.id)

@app.route('/app/add_fan40/<int:server_id>/', methods=['GET', 'POST'])
def add_fan40(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        for cmps in server.cmps:
            print("COMPONENTS", cmps)

        return jsonify(server.id)

@app.route('/app/add_indicator_board/<int:server_id>/', methods=['GET', 'POST'])
def add_indicator_board(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.id)

@app.route('/app/add_power_management_module/<int:server_id>/', methods=['GET', 'POST'])
def add_power_management_module(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.id)

@app.route('/app/add_motherboard/<int:server_id>/', methods=['GET', 'POST'])
def add_motherboard(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.id)    

@app.route('/app/add_ddr4_memory_module/<int:server_id>/', methods=['GET', 'POST'])
def add_ddr4_memory_module(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.id)

@app.route('/app/add_m2_ssd/<int:server_id>/', methods=['GET', 'POST'])
def add_m2_ssd(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.id)

@app.route('/app/add_raiser_2U_board/<int:server_id>/', methods=['GET', 'POST'])
def add_raiser_2U_board(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.id)

@app.route('/app/add_network_card/<int:server_id>/', methods=['GET', 'POST'])
def add_network_card(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.id)

@app.route('/app/add_raiser_1U_board/<int:server_id>/', methods=['GET', 'POST'])
def add_raiser_1U_board(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.id)


@app.route('/app/add_raid_card/<int:server_id>/', methods=['GET', 'POST'])
def add_raid_card(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.id)

@app.route('/app/add_disk_basket/<int:server_id>/', methods=['GET', 'POST'])
def add_disk_basket(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        hdd_backplane = Components.query.filter_by(qrcode=request.json['hdd_backplane_qrcode']).first()
        sas_expander = Components.query.filter_by(qrcode=request.json['sas_expander_qrcode']).first()
        server.cmps += [hdd_backplane]
        server.cmps += [sas_expander]
        hdd_backplane.cstat = 'установлен в изделие'
        sas_expander.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(hdd_backplane)
        db.session.add(sas_expander)
        db.session.commit()

        return jsonify(server.id)

@app.route('/app/add_power_supply_2k6/<int:server_id>/', methods=['GET', 'POST'])
def add_power_supply_2k6(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        for cmps in server.cmps:
            print("COMPONENTS", cmps)
            print("CTYPE", cmps.ctype)
            print("SERVER_ID", cmps.server_id)

        return jsonify(server.id)

@app.route('/app/testing/<int:id>/', methods=['GET'])
def testing(id):
        global task_queue
        task = ''
        component = Components.query.filter_by(id=id).first()
        uu = uuid.uuid4()
        if component.ctype == 'power_supply_2k6':
                task = 'PWR_Supply'
        elif component.ctype == 'fan_140' or component.ctype == 'fan_40':
                task = 'Fan_Module'
        elif component.ctype == 'raiser_board':
                task = 'Riser_card'
        elif component.ctype == 'hdd_backplane':
                task = 'Backplane'
        elif component.ctype == 'motherboard':
                task = 'Mainboard'
        elif component.ctype == 'power_management_module':
                task = 'PWR_Module'
        task_queue.put( jsonify( { 'return_code' : 0, 'task': task, 'snum': component.qrcode, 'task_uuid': uu, 'id': component.id } ) )
        return jsonify(component.id)

@app.route('/app/gettask/', methods=['GET'])
def gettask():
        global task_queue
        if not task_queue.empty():
                task_json = task_queue.get()
                task_queue.task_done()
                return task_json

        return jsonify( { 'return_code' : 0 } )

@app.route('/app/getresults/', methods=['GET', 'POST'])
def getresults():

        id = request.json['id']
        cstat = request.json['cstat']
        print(request)

        component = Components.query.filter_by(id=id).first()
        component.cstat = cstat
        component.statts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.add(component)
        db.session.commit()
        if cstat == 'Ok':
            component.cstat = 'протестирован'
            component.conclusion = 'годен'
            component.statts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            db.session.add(component)
            db.session.commit()
        """ if cstat == 'Error':
            component.cstat = 'протестирован'
            component.conclusion = 'He годен'
            component.statts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            db.session.add(component)
            db.session.commit()     """
        print("POST: ", id, cstat)

        getstatus(id)
 
        return jsonify( { 'status' : cstat, 'conclusion': component.conclusion } )

@app.route('/app/getstatus/<int:id>/', methods=['GET', 'POST'])
def getstatus(id):
        component = Components.query.filter_by(id=id).first()
        print("/app/getstatus ", component.cstat)
        cstat = component.cstat

        """ return jsonify(cstat) """
        return jsonify( { 'status' : cstat, 'conclusion': component.conclusion } )

@app.route('/register', methods=['GET', 'POST'])
def register():
        username = request.json['username']
        password = request.json['password']
        print("User: ", username)
        print("PASSWORD:", password)
        user_to_create = User(username=username, password=password)
        print("User to create")
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        return jsonify({
        "status": "success",
        "message": "register successful",
        "data": {
            "id": user_to_create.id,
            "username": username
        }
    }), 200


@app.route('/login', methods=["POST"])
def login():
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter_by(username=username).first()

    print("User: ", user)
    print("PASSWORD", password)
    print("CHECK PASSWORD: ", user.check_password_correction(attempted_password=password))

    if not user or not user.check_password_correction(attempted_password=password):
        return jsonify({
            "status": "failed",
            "message": "Failed getting user"
        }), 401


    login_user(user)


    return jsonify({
        "status": "success",
        "message": "login successful",
        "data": {
            "id": user.id,
            "username": username
        }
    }), 200


@app.route('/logout')
def logout_page():
    logout_user()
    return jsonify({
        "status": "success"
    }), 200

        # sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/app/hand_testing/<int:id>/', methods=['POST'])
def handle_testing(id):

    conclusion = request.json['conclusion']
    print("CONCLUSION: ", conclusion)

    component = Components.query.filter_by(id=id).first()
    component.conclusion = conclusion
    component.cstat = 'протестирован'
    db.session.add(component)
    db.session.commit()
 
    return jsonify(conclusion)

if __name__ == '__main__':
    app.run(host='192.168.75.11', port=5000)
