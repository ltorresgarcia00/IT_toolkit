from modules.system_info import get_system_info
from modules.network_tools import get_ip_info, run_speed_test
from modules.disk_usage import get_disk_usage
from modules.report_generator import save_report

all_data = {
    "System Info": get_system_info(),
    "IP Info": get_ip_info(),
    "Speed Test": run_speed_test(),
    "Disk Usage": get_disk_usage(),
}

for section, data in all_data.items():
    print(f"\n--- {section} ---")
    for k, v in data.items():
        print(f"{k}: {v}")

save_report(all_data)