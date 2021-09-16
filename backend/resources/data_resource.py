from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt

from repositories.db_repository import DbRepository
from repositories.redis_repository import RedisRepository
from repositories.log_repository import LogRepository


class DataDB(Resource):

    _db_parser = reqparse.RequestParser()
    _db_parser.add_argument("info", type=str, required=True,
                            help="Поле не может быть пустым")
    
    @jwt_required()
    def get(self):
        try:
            data = DbRepository().get_all()
            return {'data': data}, 200
        except:
            app.logger.error("Ошибка при извлечении данных из базы")
            return {"message": "Ошибка при извлечении данных из базы"}, 404
    
    @jwt_required()
    def post(self):
        claims = get_jwt()
        if not claims["is_admin"]:
            return {"message": "Доступно только Администратору"}, 401

        data = self._db_parser.parse_args()

        try:
            DbRepository().save_data(data["info"])
            LogRepository().save_data(data)
        except:
            app.logger.error("Ошибка при сохранении данных в базу")
            return {"message": "Ошибка при сохранении данных в базу"}, 500

        return {"message": "Данные были сохранены в базу"}, 201


class DataRedis(Resource):

    _redis_parser = reqparse.RequestParser()
    _redis_parser.add_argument(
        "info", type=str, required=True, help="Поле не может быть пустым")
    
    @jwt_required()
    def get(self):
        try:
            data = RedisRepository().get_all()
            return {'data': data}, 200
        except:
            app.logger.error("Ошибка при извлечении данных из Redis")
            return {"message": "Ошибка при извлечении данных из Redis"}, 404
    
    @jwt_required()
    def post(self, message):
        claims = get_jwt()
        if not claims["is_admin"]:
            return {"message": "Доступно только Администратору"}, 401

        data = self._redis_parser.parse_args()

        try:
            RedisRepository().save_data(data["info"])
            LogRepository().save_data(data)
        except:
            app.logger.error("Ошибка при сохранении данных в Redis")
            return {"message": "Ошибка сохранения данных в Redis"}, 500

        return {"message": "Данные были сохранены в Redis"}, 201


class DataLog(Resource):
    
    @jwt_required()
    def get(self):
        try:
            data = LogRepository().get_all()
            return {'data': data}, 200
        except:
            app.logger.error("Ошибка при извлечении данных из log.json")
            return {"message": "Ошибка при извлечении данных из log.json"}, 404
