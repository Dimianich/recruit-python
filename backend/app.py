from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flaskext.mysql import MySQL
from redis import Redis

from resources.data import (
    DataDB,
    DataRedis,
    DataLog
)
from resources.user import (
    UserRegistration,
    UserLogin
)

import init_db

app = Flask(__name__)
app.config.from_pyfile('settings.cfg', silent=True)

redis = Redis(host='redis', port=6379)
jwt = JWTManager(app)
api = Api(app)
CORS(app)
mysql = MySQL()
mysql.init_app(app)


@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    if (identity == "admin"):
        return {"is_admin": True}
    return {"is_admin": False}


api.add_resource(UserRegistration, '/registration')
api.add_resource(UserLogin, '/login')
api.add_resource(DataDB, '/db')
api.add_resource(DataRedis, '/redis')
api.add_resource(DataLog, '/log')


@app.before_first_request
def create_table():
    try:
        init_db.create_tables()
    except:
        app.logger.error("Ошибка при создании таблиц в бд")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
