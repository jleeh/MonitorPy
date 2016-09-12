from abc import ABCMeta, abstractmethod


class BaseInstance(metaclass=ABCMeta):
    @abstractmethod
    def get_response(self):
        pass
