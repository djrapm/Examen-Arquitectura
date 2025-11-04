from django.shortcuts import render
from django.http import JsonResponse
from . import utils

# Create your views here.

# Integrantes del grupo:
# - Cristhiam Enrique Colindres Zambrano (202310110255)
# - Ricardo Antonio Pineda Méndez (201820110114)


def index(request):
    data = {
        'cpu': utils.get_cpu_usage(),
        'memoria': utils.get_memory_usage(),
        'disco': utils.get_disk_usage(),
        'sistema': utils.get_system_info(),
    }
    return render(request, 'sistema/index.html', data)

def system_api(request):
    data = {
        'cpu': utils.get_cpu_usage(),
        'memoria': utils.get_memory_usage(),
        'disco': utils.get_disk_usage(),
        'sistema': utils.get_system_info(),
    }
    return JsonResponse({'success': True, 'data': data})

