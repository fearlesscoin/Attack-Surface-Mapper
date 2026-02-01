import socket

def scan_ports(host, ports=[21,22,80,443,3306]):
    open_ports = []
    for port in ports:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((host, port))
            open_ports.append(port)
        except:
            pass
        s.close()
    return open_ports
