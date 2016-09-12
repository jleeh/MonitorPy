import jsonpickle
import psutil
from django.http import HttpResponse

from monitor.messenger import Messenger
from monitor.module.base_module import BaseInstance


class Usage(BaseInstance):
    def get_response(self):
        cpu_array = []
        for cpu_index in range(psutil.cpu_count()):
            cpu = psutil.cpu_times_percent(interval=1, percpu=False)
            cpu_array.append(Messenger(cpu_index=cpu_index, idle=cpu.idle, user=cpu.user, system=cpu.system))
        return HttpResponse(jsonpickle.encode(Messenger(cpus=cpu_array)))
