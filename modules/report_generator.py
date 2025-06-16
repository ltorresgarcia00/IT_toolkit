import os
from datetime import datetime

def save_report(data_dict, filename="report.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"ouput/{filename.replace('.txt', '')}_{timestamp}.txt"
    with open(path, "w") as f:
        for section, data in data_dict.items():
            f.write(f"--- {section} ---\n")
            for key, val in data.items():
                f.write(f"{key}: {val}\n")
            f.write("\n")
    return path