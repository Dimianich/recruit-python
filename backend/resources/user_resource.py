from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from repositories.user_repository import UserRepository

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username", help="Поле не может быть пустым", required=True)
_user_parser.add_argument(
    "password", help="Поле не может быть пустым", required=True)


class UserRegistration(Resource):
    
    def post(self):
        data = _user_parser.parse_args()

        if UserRepository.find_by_username(data["username"]):
            return {"message": "Пользователь {} уже существует.".format(data["username"])}, 400

        try:
            password = generate_password_hash(data["password"])
            UserRepository.save_to_db(data["username"], password)
            access_token = create_access_token(identity=data["username"])
            return {"message": "Пользователь {} был создан".format(data["username"]),
                    "access_token": access_token
                    }, 201
        except:
            app.logger.error("Ошибка при сохранении пользователя в базу")
            return {"message": "Ошибка сервера"}, 500


class UserLogin(Resource):

    def post(self):
        data = _user_parser.parse_args()
        current_user = UserRepository.find_by_username(data["username"])
        if not current_user:
            app.logger.error(
                "Ошибка: Пользователя {} не существует".format(data['username']))
            return {"message": "Пользователя {} не существует".format(data['username'])}, 400

        if check_password_hash(current_user.password, data["password"]):
            access_token = create_access_token(identity=data["username"])
            app.logger.info("Пользователь {} вошел в систему".format(
                current_user.username))
            return {"message": "Пользователь {} вошел в систему".format(current_user.username),
                    "access_token": access_token
                    }, 200
        else:
            app.logger.error("Ошибка при идентификации пользователя")
            return {"message": "Ошибка доступа"}, 403
