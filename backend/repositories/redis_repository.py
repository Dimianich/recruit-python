from repositories.abstract_data_repository import AbstractDataRepository
from redis_db import redis


class RedisRepository(AbstractDataRepository):

    def get_all(self):
        result = redis.lrange('info', 0, -1)
        data = []
        for item in result:
            data.append({"info": item})
        return data

    def save_data(self, info):
        redis.rpush('info', info)
