# Brennan Laing

import socket
import ssl

serverIP = ""
serverPort = 10443

certFileLoc = "tls/server.crt"
keyFileLoc = "tls/server.key"

def main():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=certFileLoc, keyfile=keyFileLoc)

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

    try:
        soc.bind((serverIP, serverPort))
        soc.listen(1)
        print(f"Server listening on {serverIP}:{serverPort}")

        while True:
            conn, addr = soc.accept()
            print(f"TLS connection established with {addr}")

            try:
                conn = context.wrap_socket(conn, server_side=True)
                data = conn.recv(1024)
                decodedData = data.decode()

                print(f"Received message: {data} from {addr}")

                if decodedData.isdigit():
                    number = int(decodedData)
                    if number % 2 == 0:
                        response = "Even"
                    else:
                        response = "Odd"
                else:
                    response = "Invalid"
                
                conn.sendall(response.encode())
                conn.close()
            except ssl.SSLError as e:
                print(f"SSL error occurred: {e}")
                conn.close()  
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
