import psutil
import platform

# Integrantes del grupo:
# - Cristhiam Enrique Colindres Zambrano (202310110255)
# - Ricardo Antonio Pineda Méndez (201820110114)

def get_cpu_usage():
    try:
        return psutil.cpu_percent(interval=0.1)
    except Exception:
        return None

def get_memory_usage():
    try:
        mem = psutil.virtual_memory()
        total = round(mem.total / (1024 ** 3), 2)
        used = round((mem.total - mem.available) / (1024 ** 3), 2)
        return {'total': total, 'used': used, 'percent': mem.percent}
    except Exception:
        return None

def get_disk_usage():
    try:
        disk = psutil.disk_usage('/')
        total = round(disk.total / (1024 ** 3), 2)
        used = round(disk.used / (1024 ** 3), 2)
        free = round(disk.free / (1024 ** 3), 2)
        return {'total': total, 'used': used, 'free': free, 'percent': disk.percent}
    except Exception:
        return None

def get_system_info():
    try:
        return {
            'so': platform.system(),
            'version': platform.version(),
            'release': platform.release(),
            'cpu_fisicos': psutil.cpu_count(logical=False),
            'cpu_logicos': psutil.cpu_count(logical=True),
            'procesador': platform.processor()
        }
    except Exception:
        return None
