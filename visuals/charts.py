import matplotlib.pyplot as plt

def plot_disk_usage(usage_dict):
    labels = list(usage_dict.keys())
    sizes = list(usage_dict.values())
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold']

    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.title("Disk Usage Breakdown")
    plt.show()
