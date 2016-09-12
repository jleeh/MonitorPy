import jsonpickle
import psutil
from django.http import HttpResponse

from monitor.messenger import Messenger
from monitor.module.base_module import BaseInstance


class Virtual(BaseInstance):
    def get_response(self):
        memory_usage = psutil.virtual_memory()
        response = Messenger(
            total=memory_usage.total,
            free=memory_usage.free,
            used=memory_usage.used,
            percent=memory_usage.percent
        )
        return HttpResponse(jsonpickle.encode(response))


class Swap(BaseInstance):
    def get_response(self):
        memory_usage = psutil.swap_memory()
        response = Messenger(
            total=memory_usage.total,
            free=memory_usage.free,
            used=memory_usage.used,
            percent=memory_usage.percent
        )
        return HttpResponse(jsonpickle.encode(response))