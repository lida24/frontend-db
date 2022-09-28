from flask import Flask, jsonify, request, flash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lida:12345678@localhost:5432/db_ps'
app.config['SECRET_KEY'] = '548b2563213f3c0c1bcb915a'

db = SQLAlchemy(app)
ma = Marshmallow(app)

# table
class Components(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    ctype = db.Column(db.String(length=150), db.ForeignKey('comptypes.name'))
    qrcode = db.Column(db.String(length=180), nullable=False, unique=True)
    addts = db.Column(db.DateTime(), nullable=False)
    cstat = db.Column(db.String(length=30), nullable=False, default='новый')
    statts = db.Column(db.DateTime(), nullable=False)
    tests = db.Column(db.String(length=150), default='Отсутствует')
    rem = db.Column(db.String(length=1024), default='Отсутствует')
    #owner = db.Column(db.Integer(), db.ForeignKey('plant.id'))
    conclusion = db.Column(db.String(length=1024), nullable=False, default='-')
    server_id = db.Column(db.Integer(), db.ForeignKey('servers.id'))

    def __init__(self, ctype, qrcode, addts, cstat, statts, tests, rem, conclusion):
        self.ctype = ctype
        self.qrcode = qrcode
        self.addts = addts
        self.cstat = cstat
        self.statts = statts
        self.tests = tests
        self.rem = rem
        self.conclusion = conclusion

# schema
class ComponentSchema(ma.SQLAlchemySchema):
    class  Meta:
        model = Components
        
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
class ComptypeSchema(ma.SQLAlchemyAutoSchema):
    class  Meta:
        model = Comptypes    

# schema obj
comptype_schema = ComptypeSchema() 
comptypes_schema = ComptypeSchema(many=True)

class Servers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    qrcode = db.Column(db.String(length=180))
    asts = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    vts = db.Column(db.DateTime, default=datetime.utcnow)
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
class ServerSchema(ma.SQLAlchemyAutoSchema):
    class  Meta:
        model = Servers   

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
    all_components = Comptypes.query.all()
    return  comptypes_schema.jsonify(all_components)

@app.route('/app/component/<id>/', methods=['GET'])
def component_details(id):

    component_detail = Comptypes.query.get(id)
    data = [{'decoding': component_detail.decoding, 'conclusion': p.conclusion, 'qrcode': p.qrcode, 'cstat': p.cstat, 'tests': p.tests, 'rem': p.rem} for p in component_detail.components]
    if component_detail:
        return jsonify(data)
    else:
        return "No component with that ID"

#  ------------------ post or add new 
@app.route('/app/create_component', methods=['GET', 'POST'])
def add_component():
    ctype = request.json['ctype']
    qrcode = request.json['qrcode']
    addts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cstat = 'новый'
    statts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tests = 'Отсутствует'
    rem = 'Отсутствует'
    conclusion = '-'

    components = Components(ctype, qrcode, addts, cstat, statts, tests, rem, conclusion)
    db.session.add(components)
    db.session.commit()

    comptypes = Comptypes.query.filter_by(name=ctype).first()
    comptypes.count = comptypes.count + 1
    db.session.add(comptypes)
    db.session.commit()
    errors = "asdf"
    return errors

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


        # sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()