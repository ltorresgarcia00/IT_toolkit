import tkinter as tk
from tkinter import scrolledtext
from modules.system_info import get_system_info
from modules.network_tools import get_ip_info, run_speed_test
from modules.disk_usage import get_disk_usage

def generate_report():
    report_text.delete(1.0, tk.END)

    all_data = {
        "System Info": get_system_info(),
        "IP Info": get_ip_info(),
        "Speed Test": get_system_info(),
        "Disk Usage": get_disk_usage(),
    }

    for section, data in all_data.items():
        report_text.insert(tk.END, f"--- {section} ---\n")
        for key, val in data.items():
            report_text.insert(tk.END, f"{key}: {val}\n")
        report_text.insert(tk.END, "\n")

root = tk.Tk()
root.title("SupportHero")
root.geometry("600x600")

generate_button = tk.Button(root, text="Run Diagnsotic", command=generate_report)
generate_button.pack(pady=10)

report_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=30)
report_text.pack(padx=10, pady=10)

root.mainloop()