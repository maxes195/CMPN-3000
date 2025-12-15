# Brennan Laing

import socket
import ssl

serverIP = "150.136.35.130"
serverPort = 10443
certFileLoc = "tls/server.crt"

def main():
    
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.load_verify_locations(certFileLoc)
        soc = context.wrap_socket(soc, server_hostname=serverIP)
        soc.connect((serverIP, serverPort))
        message = input("Enter a number to send: ")
        soc.sendall(message.encode())

        data = soc.recv(1024)
        print(f"The number is {data.decode()}")

    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except KeyboardInterrupt:
        print("\nConnection interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        soc.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
