import socket

# Function to check if a port is open
def scan_port(ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout after 1 second
        result = sock.connect_ex((ip, port))  # Connect to the target IP and port

        # Check the result of the connection attempt
        if result == 0:
            return True  # Port is open
        else:
            return False  # Port is closed
    except socket.error:
        return False  # In case of an error (e.g., unreachable host)

# Main function
if __name__ == "__main__":
    ip_address = input("Enter the IP address to scan: ")
    port = int(input("Enter the port number to scan: "))  # Scan a single port

    print(f"Scanning {ip_address} for port {port}...\n")

    if scan_port(ip_address, port):
        print(f"Port {port} is open.")
    else:
        print(f"Port {port} is closed.")
