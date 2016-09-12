import importlib
import jsonpickle
from django.http import HttpResponse
from rest_framework import status

from monitor.messenger import Messenger
from monitor.module.base_module import BaseInstance


def index(request, module_name, module_instance_name):
    module_instance_names = [
        module_instance_name.title(),
        module_instance_name.upper()
    ]
    for (i, instance_name_formatted) in enumerate(module_instance_names):
        try:
            module_ = importlib.import_module("monitor.module.{}".format(module_name))
            monitor_instance_ = getattr(module_, instance_name_formatted)
            assert issubclass(monitor_instance_, BaseInstance)
            response = monitor_instance_().get_response()
            assert isinstance(response, HttpResponse)
            return response
        except ImportError:
            return HttpResponse(jsonpickle.encode(Messenger(
                message='Monitor module {} doesn\'t exist'.format(module_name))),
                status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            if i == module_instance_names.__len__() - 1:
                return HttpResponse(jsonpickle.encode(Messenger(
                    message='Monitor module instance {} doesn\'t exist'.format(module_instance_name))),
                    status=status.HTTP_400_BAD_REQUEST)
        except AssertionError:
            return HttpResponse(jsonpickle.encode(Messenger(
                message='Monitor module {} not a valid module/instance'.format(module_instance_name))),
                status=status.HTTP_400_BAD_REQUEST)
