import socket
import speedtest

def get_ip_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {"Hostname": hostname, "IP Address": ip_address}

def run_speed_test():
    st = speedtest.Speedtest()
    return {
        "Download (Mbps)": round(st.download() / 1_000_000, 2),
        "Upload (Mbps)": round(st.upload() / 1_000_000, 2),
        "Ping (ms)": st.results.ping,
    }