import json
from repositories.abstract_data_repository import AbstractDataRepository


class LogRepository(AbstractDataRepository):

    def get_all(self):
        data = []
        with open("log.json", "r", encoding='utf-8') as file:
            for line in file:
                data.append(json.loads(line))
        return data

    def save_data(self, info):
        with open("log.json", "a", encoding='utf-8') as file:
            json.dump(info, file, ensure_ascii=False)
            file.write('\n')
