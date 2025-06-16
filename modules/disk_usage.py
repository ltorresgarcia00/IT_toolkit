import psutil

def get_disk_usage():
    usage = psutil.disk_usage('/')
    return {
        "Total (GB)": round(usage.total / (1024 ** 3), 2),
        "Used (GB)": round(usage.used / (1024 ** 3), 2),
        "Free (GB)": round(usage.free / (1024 ** 3), 2),
        "Usage (%)": usage.percent
    }