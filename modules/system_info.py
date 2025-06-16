import platform
import psutil

def get_system_info():
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Archutecture": platform.machine(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=False),
        "RAM (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2)
    }