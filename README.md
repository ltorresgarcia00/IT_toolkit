# 🛠️ IT Toolkit – System Monitoring & Diagnostics Suite

A modular Python-based IT diagnostic toolkit designed to simulate real-world system monitoring, troubleshooting, and reporting workflows used in IT Support and Help Desk environments.

This project demonstrates practical IT automation skills including:

- System monitoring
- Network diagnostics
- Disk usage analysis
- Process monitoring
- Report generation
- Data visualization
- GUI development

---

## 🚀 Project Overview

The **IT Toolkit** is a desktop application that aggregates multiple IT support utilities into one modular system.

It is designed to mimic tasks performed by:

- IT Support Technicians
- Help Desk Analysts
- Junior System Administrators
- NOC Technicians

---

## 📂 Project Structure

```
IT_toolkit/
│
├── modules/
│   ├── disk_usage.py        # Disk storage analysis
│   ├── network_tools.py     # Network diagnostics (ping, IP, etc.)
│   ├── process_monitor.py   # Running process tracking
│   ├── report_generator.py  # Automated system report generation
│   └── system_info.py       # System information collection
│
├── visuals/
│   └── charts.py            # Data visualization (charts/graphs)
│
├── gui.py                   # Graphical User Interface
├── main.py                  # Application entry point
├── logs/                    # Log storage
├── outputs/                 # Generated reports
├── requirements.txt
└── README.md
```

---

# 🔧 Features

## 🖥️ System Information Module
- Collect OS details
- CPU usage
- Memory usage
- Hostname and network details

## 💾 Disk Usage Analyzer
- Displays disk usage statistics
- Detects low storage warnings
- Helps troubleshoot storage-related issues

## 🌐 Network Tools
- IP configuration retrieval
- Basic connectivity testing
- Network diagnostics simulation

## 📊 Process Monitor
- Lists running processes
- Displays resource consumption
- Identifies high CPU or memory usage processes

## 📑 Report Generator
- Generates system health reports
- Saves reports to `/outputs`
- Useful for documentation & troubleshooting logs

## 📈 Data Visualization
- Charts system metrics
- Graphical performance representation
- Helps visualize system trends

---

# 🧠 How It Works

1. User launches `main.py`
2. GUI loads available IT tools
3. User selects diagnostic module
4. Data is collected from system
5. Results are:
   - Displayed in GUI
   - Logged to `/logs`
   - Exported to `/outputs`
   - Visualized via charts

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/ltorresgarcia00/IT_toolkit.git
cd IT_toolkit
```

---

## 2️⃣ Create Virtual Environment

Mac/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

```bash
python main.py
```

---

# 🛡️ Real-World IT Skills Demonstrated

This project simulates real Help Desk responsibilities:

- Diagnosing performance issues
- Checking disk health
- Investigating network problems
- Monitoring system processes
- Generating support reports
- Logging system data

---

# 📌 Example Use Cases

✔ Troubleshooting slow computer complaints  
✔ Investigating high CPU usage  
✔ Checking available disk storage  
✔ Verifying network connectivity  
✔ Creating documentation reports for tickets  

---

# 🔮 Future Improvements

- Remote system monitoring
- Email alert notifications
- Scheduled automated reporting
- Dark mode UI
- Role-based access control
- Export reports as PDF
- Integration with ticketing systems

---

# 💼 Why This Project Is Portfolio-Ready

This project demonstrates:

- Modular programming architecture
- Separation of concerns
- GUI development
- Logging implementation
- File system management
- Data visualization
- Real-world IT automation

This is highly relevant for:

- IT Support roles
- Help Desk Technician positions
- System Administrator internships
- SOC Analyst (entry-level)
- Technical Support roles

---

# 👤 Author

Leonel Torres Garcia  
Computer Science – Cybersecurity Option  
Kean University  

GitHub: https://github.com/ltorresgarcia00  
LinkedIn: https://www.linkedin.com/in/leoneltorresgarcia/

---

# ⚠️ Note

This toolkit is intended for educational and portfolio purposes to simulate IT diagnostic workflows.
