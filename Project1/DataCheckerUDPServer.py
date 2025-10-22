# Brennan Laing

import socket

def main():
    serverIP = ""
    serverPort = 24454


    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        soc.bind((serverIP, serverPort))
        print(f"Server listening on {serverIP}:{serverPort}")
        while True:
            data, addr = soc.recvfrom(1024)
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

            soc.sendto(response.encode(), addr)
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
