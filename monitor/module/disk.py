import jsonpickle
import psutil
from django.http import HttpResponse

from monitor.messenger import Messenger
from monitor.module.base_module import BaseInstance


class Usage(BaseInstance):
    def get_response(self):
        disk_usages_array = []
        for disk_partition in psutil.disk_partitions():
            if "fixed" in disk_partition.opts:
                disk_usage = psutil.disk_usage(disk_partition.device)
                disk_usages_array.append(Messenger(
                    partion=disk_partition.device,
                    total=disk_usage.total,
                    free=disk_usage.free,
                    used=disk_usage.used)
                )
        return HttpResponse(jsonpickle.encode(Messenger(disk_usages=disk_usages_array)))
