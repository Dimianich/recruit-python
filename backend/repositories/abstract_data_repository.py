from abc import ABC, abstractmethod


class AbstractDataRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def save_data(self):
        pass
