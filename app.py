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
    servers = db.relationship('Servers', backref='user_servers', lazy=True)

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
    owner = db.Column(db.String(length=180), db.ForeignKey('user.username'))
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
    qrcode = db.Column(db.String(length=180), nullable=False, unique=True)
    asts = db.Column(db.DateTime, nullable=False, default=datetime.date)
    vts = db.Column(db.DateTime, default=datetime.date)
    aid = db.Column(db.String(length=180), db.ForeignKey('user.username'))
    """ vid = db.Column(db.Integer(), primary_key=True) """
    cmps = db.relationship('Components', backref='components')
    """ tstts = db.Column(db.DateTime, default=datetime.utcnow) """
    """ tstres = db.Column(db.String(length=2048)) """
    sstat = db.Column(db.String(length=30), default='новый')
    """ snum = db.Column(db.String(length=30), unique=True) """
    cables = db.Column(db.Boolean(), unique=False, default=False)
    fans_140 = db.Column(db.Boolean(), unique=False, default=False)
    indicator_board = db.Column(db.Boolean(), unique=False, default=False)
    fans_40 = db.Column(db.Boolean(), unique=False, default=False)
    fan_control_board = db.Column(db.Boolean(), unique=False, default=False)
    power_management_module = db.Column(db.Boolean(), unique=False, default=False)
    cables_pmm = db.Column(db.Boolean(), unique=False, default=False)
    cables_fcb = db.Column(db.Boolean(), unique=False, default=False)
    memory_and_ssd = db.Column(db.Boolean(), unique=False, default=False)
    network_card = db.Column(db.Boolean(), unique=False, default=False)
    raiser_2U_board = db.Column(db.Boolean(), unique=False, default=False)
    raid_card = db.Column(db.Boolean(), unique=False, default=False)
    cables_mb = db.Column(db.Boolean(), unique=False, default=False)
    motherboard = db.Column(db.Boolean(), unique=False, default=False)
    power_supply_2k6 = db.Column(db.Boolean(), unique=False, default=False)
    disk_basket4 = db.Column(db.Boolean(), unique=False, default=False)
    disk_basket3 = db.Column(db.Boolean(), unique=False, default=False)
    disk_basket2 = db.Column(db.Boolean(), unique=False, default=False)
    disk_basket1 = db.Column(db.Boolean(), unique=False, default=False)


    def __init__(self, qrcode, asts, vts, aid, cmps, sstat, indicator_board, fans_40, cables, fans_140, fan_control_board, power_management_module, cables_pmm, cables_fcb, memory_and_ssd, network_card, raiser_2U_board, raid_card, cables_mb, motherboard, power_supply_2k6, disk_basket4, disk_basket3, disk_basket2, disk_basket1):
        self.qrcode = qrcode
        self.asts = asts
        self.vts = vts
        self.aid = aid
        self.cmps = cmps
        self.sstat = sstat
        self.indicator_board = indicator_board
        self.fans_40 = fans_40
        self.cables = cables
        self.fans_140 = fans_140
        self.fan_control_board = fan_control_board
        self.power_management_module = power_management_module
        self.cables_pmm = cables_pmm
        self.cables_fcb = cables_fcb
        self.memory_and_ssd = memory_and_ssd
        self.network_card = network_card
        self.raiser_2U_board = raiser_2U_board
        self.raid_card = raid_card
        self.cables_mb = cables_mb
        self.motherboard = motherboard
        self.power_supply_2k6 = power_supply_2k6
        self.disk_basket4 = disk_basket4
        self.disk_basket3 = disk_basket3
        self.disk_basket2 = disk_basket2
        self.disk_basket1 = disk_basket1

# schema
class ServerSchema(ma.SQLAlchemySchema):
    class  Meta:
        fields = ("id", "qrcode", "asts", "vts", "aid", "sstat", "indicator_board", "fans_40", "cables", "fans_140", "fan_control_board", "power_management_module", "cables_pmm", "cables_fcb", "memory_and_ssd", "network_card", "raiser_2U_board", "raid_card", "cables_mb", "motherboard", "power_supply_2k6", "disk_basket4", "disk_basket3", "disk_basket2", "disk_basket1")

# schema obj
server_schema = ServerSchema() 
servers_schema = ServerSchema(many=True)

#  ------------------ get all servers
@app.route('/app/server_list', methods=['GET'])
def get_servers():
    all_servers = Servers.query.all()
    return  servers_schema.jsonify(all_servers)

#  ------------------ get all components
@app.route('/app/component_list', methods=['GET'])
def get_components():
    """ all_components = Comptypes.query.all() """
    all_components = [Comptypes.query.filter_by(name='chassis').first(), Comptypes.query.filter_by(name='motherboard').first(), Comptypes.query.filter_by(name='hdd_backplane').first(), Comptypes.query.filter_by(name='raiser_board').first(), Comptypes.query.filter_by(name='power_management_module').first()]
    return  comptypes_schema.jsonify(all_components)

#  ------------------ get all components of one type
@app.route('/app/component/<id>/', methods=['GET'])
def component_details(id):
    component_detail = Comptypes.query.get(id)
    data = [{'id': p.id, 'decoding': component_detail.decoding, 'conclusion': p.conclusion, 'qrcode': p.qrcode, 'cstat': p.cstat, 'addts': p.addts, 'statts': p.statts, 'tests': p.tests, 'rem': p.rem} for p in component_detail.components]
    return jsonify(data)

#  ------------------ get current component
@app.route('/app/current_component/<id>/', methods=['GET'])
def current_component(id):
    current_component = Components.query.filter_by(id=id).first()
    current_comptype = Comptypes.query.filter_by(name=current_component.ctype).first()
    data = {'id': current_component.id, 'conclusion': current_component.conclusion, 'qrcode': current_component.qrcode, 'cstat': current_component.cstat, 'tests': current_component.tests, 'rem': current_component.rem, 'ctype_id': current_comptype.id, 'ctype_name': current_comptype.name, 'decoding': current_comptype.decoding }
    return jsonify(data)

#  ------------------ get current server
@app.route('/app/current_server/<id>/', methods=['GET'])
def current_server(id):
    current_server = Servers.query.filter_by(id=id).first()
    return server_schema.jsonify(current_server)

#  ------------------ create new component
@app.route('/app/create_component/<username>/', methods=['GET', 'POST'])
def add_component(username):
    ctype = request.json['ctype']
    qrcode = request.json['qrcode']
    errors = ""
    if qrcode == "":
        errors = '500'
        return errors
    if ctype == "":
        errors = '510'
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
    owner = user.username
    conclusion = '-'

    components = Components(ctype, qrcode, addts, cstat, statts, tests, rem, owner, conclusion)
    db.session.add(components)
    db.session.commit()

    comptypes = Comptypes.query.filter_by(name=ctype).first()
    comptypes.count = comptypes.count + 1
    db.session.add(comptypes)
    db.session.commit()

    return component_schema.jsonify(components)

#  ------------------ create new server
@app.route('/app/add_chassis/<username>/', methods=['GET', 'POST'])
def add_chassis(username):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        if request.json['qrcode'] == '':
                errors = '520'
                return jsonify({'error': errors, 'other': ''})
        if result == None:
                errors = '500'
                return jsonify({'error': errors, 'other': ''})
        if result.ctype != 'chassis':
                errors = '525'
                return jsonify({'error': errors, 'other': ''})
        if result.cstat == 'забракован':
                errors = '505'
                return jsonify({'error': errors, 'other': ''})
        """ if result.cstat == 'новый':
                errors = '510'
                return jsonify({'error': errors, 'other': ''}) """
        if result.cstat == 'установлен в изделие':
                errors = '515'
                server = Servers.query.filter_by(id=result.server_id).first()
                qr = server.qrcode
                return jsonify({'error': errors, 'other': qr})
        user = User.query.filter_by(username=username).first()
        server_to_create = Servers(qrcode=request.json['qrcode'],
                                   asts=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                   vts =datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                   aid=user.username,
                                   sstat='новый',
                                   cmps=[result],
                                   cables=False,
                                   fans_140=False,
                                   indicator_board=False,
                                   fans_40=False,
                                   fan_control_board=False,
                                   power_management_module=False,
                                   cables_fcb=False,
                                   cables_pmm=False,
                                   memory_and_ssd=False,
                                   network_card=False,
                                   raiser_2U_board=False,
                                   raid_card=False,
                                   cables_mb=False,
                                   motherboard=False,
                                   power_supply_2k6=False,
                                   disk_basket4=False,
                                   disk_basket3=False,
                                   disk_basket2=False,
                                   disk_basket1=False,
                                  )
        server_to_create.sstat = 'в сборке'
        result.cstat = 'установлен в изделие'
        db.session.add(server_to_create)
        db.session.add(result)
        db.session.commit()

        return jsonify({'error': '', 'other': server_to_create.id})

#  ------------------ get chassis
@app.route('/app/get_chassis/<int:server_id>/', methods=['GET', 'POST'])
def get_chassis(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        if (server.indicator_board and server.fans_40 and server.cables and server.fans_140 and server.fan_control_board and server.power_management_module and server.cables_pmm and server.cables_fcb and server.memory_and_ssd and server.network_card and server.raiser_2U_board and server.raid_card and server.cables_mb and server.motherboard and server.power_supply_2k6 and server.disk_basket4 and server.disk_basket3 and server.disk_basket2 and server.disk_basket1):
                server.sstat = 'собран'
                db.session.add(server)
                db.session.commit()
        return server_schema.jsonify(server)

@app.route('/app/add_cables/<int:server_id>/', methods=['GET', 'POST'])
def add_cables(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.cables = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.cables)

@app.route('/app/add_fan140/<int:server_id>/', methods=['GET', 'POST'])
def add_fan140(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.fans_140 = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.fans_140)

@app.route('/app/add_fan_control_board/<int:server_id>/', methods=['GET', 'POST'])
def add_fan_control_board(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.fan_control_board = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.fan_control_board)

@app.route('/app/add_cables_fcb/<int:server_id>/', methods=['GET', 'POST'])
def add_cables_fcb(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.cables_fcb = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.cables_fcb)

@app.route('/app/add_fan40/<int:server_id>/', methods=['GET', 'POST'])
def add_fan40(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.fans_40 = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.fans_40)

@app.route('/app/add_indicator_board/<int:server_id>/', methods=['GET', 'POST'])
def add_indicator_board(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.indicator_board = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.indicator_board)

@app.route('/app/add_power_management_module/<int:server_id>/', methods=['GET', 'POST'])
def add_power_management_module(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.power_management_module = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.power_management_module)

@app.route('/app/add_cables_pmm/<int:server_id>/', methods=['GET', 'POST'])
def add_cables_pmm(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.cables_pmm = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.cables_pmm)

@app.route('/app/add_memory_and_ssd/<int:server_id>/', methods=['GET', 'POST'])
def add_memory_and_ssd(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.memory_and_ssd = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.memory_and_ssd)

@app.route('/app/add_motherboard/<int:server_id>/', methods=['GET', 'POST'])
def add_motherboard(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        if request.json['qrcode'] == '':
                errors = '520'
                return jsonify({'error': errors, 'other': ''})
        if result == None:
                errors = '500'
                return jsonify({'error': errors, 'other': ''})
        if result.ctype != 'motherboard':
                errors = '535'
                return jsonify({'error': errors, 'other': ''})
        if server.motherboard == True:
                errors = '530'
                return jsonify({'error': errors, 'other': ''})
        if result.cstat == 'забракован':
                errors = '505'
                return jsonify({'error': errors, 'other': ''})
        """ if result.cstat == 'новый':
                errors = '510'
                return jsonify({'error': errors, 'other': ''}) """
        if result.cstat == 'установлен в изделие':
                errors = '515'
                server = Servers.query.filter_by(id=result.server_id).first()
                qr = server.qrcode
                return jsonify({'error': errors, 'other': qr})
        server.cmps += [result]
        server.motherboard = True
        result.cstat = 'установлен в изделие'
        result.statts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.motherboard)    

@app.route('/app/add_raiser_2U_board/<int:server_id>/', methods=['GET', 'POST'])
def add_raiser_2U_board(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.raiser_2U_board = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.raiser_2U_board)

@app.route('/app/add_network_card/<int:server_id>/', methods=['GET', 'POST'])
def add_network_card(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.network_card = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.network_card)

@app.route('/app/add_cables_mb/<int:server_id>/', methods=['GET', 'POST'])
def add_cables_mb(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.cables_mb = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.cables_mb)

@app.route('/app/add_raid_card/<int:server_id>/', methods=['GET', 'POST'])
def add_raid_card(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.raid_card = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.raid_card)

@app.route('/app/add_disk_basket4/<int:server_id>/', methods=['GET', 'POST'])
def add_disk_basket4(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        if request.json['qrcode'] == '':
                errors = '520'
                return jsonify({'error': errors, 'other': ''})
        if result == None:
                errors = '500'
                return jsonify({'error': errors, 'other': ''})
        if result.ctype != 'hdd_backplane':
                errors = '535'
                return jsonify({'error': errors, 'other': ''})
        if server.disk_basket4 == True:
                errors = '530'
                return jsonify({'error': errors, 'other': ''})
        if result.cstat == 'забракован':
                errors = '505'
                return jsonify({'error': errors, 'other': ''})
        """ if result.cstat == 'новый':
                errors = '510'
                return jsonify({'error': errors, 'other': ''}) """
        if result.cstat == 'установлен в изделие':
                if result.server_id == server.id:
                        errors = '525'
                        return jsonify({'error': errors, 'other': ''})
                errors = '515'
                server = Servers.query.filter_by(id=result.server_id).first()
                qr = server.qrcode
                return jsonify({'error': errors, 'other': qr})
        server.disk_basket4 = True
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        result.statts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.disk_basket4)

@app.route('/app/add_disk_basket3/<int:server_id>/', methods=['GET', 'POST'])
def add_disk_basket3(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        if request.json['qrcode'] == '':
                errors = '520'
                return jsonify({'error': errors, 'other': ''})
        if result == None:
                errors = '500'
                return jsonify({'error': errors, 'other': ''})
        if result.ctype != 'hdd_backplane':
                errors = '535'
                return jsonify({'error': errors, 'other': ''})
        if server.disk_basket3 == True:
                errors = '530'
                return jsonify({'error': errors, 'other': ''})
        if result.cstat == 'забракован':
                errors = '505'
                return jsonify({'error': errors, 'other': ''})
        """ if result.cstat == 'новый':
                errors = '510'
                return jsonify({'error': errors, 'other': ''}) """
        if result.cstat == 'установлен в изделие':
                if result.server_id == server.id:
                        errors = '525'
                        return jsonify({'error': errors, 'other': ''})
                errors = '515'
                server = Servers.query.filter_by(id=result.server_id).first()
                qr = server.qrcode
                return jsonify({'error': errors, 'other': qr})
        server.disk_basket3 = True
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        result.statts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.disk_basket3)

@app.route('/app/add_disk_basket2/<int:server_id>/', methods=['GET', 'POST'])
def add_disk_basket2(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        if request.json['qrcode'] == '':
                errors = '520'
                return jsonify({'error': errors, 'other': ''})
        if result == None:
                errors = '500'
                return jsonify({'error': errors, 'other': ''})
        if result.ctype != 'hdd_backplane':
                errors = '535'
                return jsonify({'error': errors, 'other': ''})
        if server.disk_basket2 == True:
                errors = '530'
                return jsonify({'error': errors, 'other': ''})
        if result.cstat == 'забракован':
                errors = '505'
                return jsonify({'error': errors, 'other': ''})
        """ if result.cstat == 'новый':
                errors = '510'
                return jsonify({'error': errors, 'other': ''}) """
        if result.cstat == 'установлен в изделие':
                if result.server_id == server.id:
                        errors = '525'
                        return jsonify({'error': errors, 'other': ''})
                errors = '515'
                server = Servers.query.filter_by(id=result.server_id).first()
                qr = server.qrcode
                return jsonify({'error': errors, 'other': qr})
        server.disk_basket2 = True
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        result.statts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.disk_basket2)

@app.route('/app/add_disk_basket1/<int:server_id>/', methods=['GET', 'POST'])
def add_disk_basket1(server_id):
        result = Components.query.filter_by(qrcode=request.json['qrcode']).first()
        server = Servers.query.filter_by(id=server_id).first()
        if request.json['qrcode'] == '':
                errors = '520'
                return jsonify({'error': errors, 'other': ''})
        if result == None:
                errors = '500'
                return jsonify({'error': errors, 'other': ''})
        if result.ctype != 'hdd_backplane':
                errors = '535'
                return jsonify({'error': errors, 'other': ''})
        if server.disk_basket1 == True:
                errors = '530'
                return jsonify({'error': errors, 'other': ''})
        if result.cstat == 'забракован':
                errors = '505'
                return jsonify({'error': errors, 'other': ''})
        """ if result.cstat == 'новый':
                errors = '510'
                return jsonify({'error': errors, 'other': ''}) """
        if result.cstat == 'установлен в изделие':
                if result.server_id == server.id:
                        errors = '525'
                        return jsonify({'error': errors, 'other': ''})
                errors = '515'
                server = Servers.query.filter_by(id=result.server_id).first()
                qr = server.qrcode
                return jsonify({'error': errors, 'other': qr})
        server.disk_basket1 = True
        server.cmps += [result]
        result.cstat = 'установлен в изделие'
        result.statts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.session.add(server)
        db.session.add(result)
        db.session.commit()

        return jsonify(server.disk_basket1)

@app.route('/app/add_power_supply_2k6/<int:server_id>/', methods=['GET', 'POST'])
def add_power_supply_2k6(server_id):
        server = Servers.query.filter_by(id=server_id).first()
        server.power_supply_2k6 = True
        db.session.add(server)
        db.session.commit()

        return jsonify(server.power_supply_2k6)

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
        error = request.json['error']
        print(error)
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
        if cstat == 'Error':
            if error == None:
                error = 'Ошибка'
            component.cstat = 'забракован'
            component.conclusion = 'нe годен'
            component.rem = error
            component.statts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            db.session.add(component)
            db.session.commit()
        print("POST: ", id, cstat)

        getstatus(id)
 
        return jsonify( { 'status' : cstat, 'conclusion': component.conclusion, 'rem': component.rem } )

@app.route('/app/getstatus/<int:id>/', methods=['GET', 'POST'])
def getstatus(id):
        component = Components.query.filter_by(id=id).first()
        print("/app/getstatus ", component.cstat)
        cstat = component.cstat

        return jsonify( { 'status' : cstat, 'conclusion': component.conclusion, 'rem': component.rem } )

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

@app.route('/app/hand_testing/<int:id>/', methods=['POST'])
def handle_testing(id):

    conclusion = request.json['conclusion']

    component = Components.query.filter_by(id=id).first()
    component.conclusion = conclusion
    if conclusion == 'годен':
        component.cstat = 'протестирован'
    elif conclusion == 'нe годен':
        component.cstat = 'забракован'
    db.session.add(component)
    db.session.commit()
    return jsonify(conclusion)

if __name__ == '__main__':
    app.run(host='185.129.98.66', port=5000)
