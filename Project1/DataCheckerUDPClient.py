# Brennan Laing

import socket

def main():
    serverIP = "150.136.144.166"
    serverPort = 24454

    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        soc.connect((serverIP, serverPort))
        message = input("Enter a number to send: ")
        soc.sendto(message.encode(), (serverIP, serverPort))
        
        data, addr = soc.recvfrom(1024)
        print(f"The number is {data.decode()}")
    
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
