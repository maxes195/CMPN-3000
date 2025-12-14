# Brennan Laing

import socket

def main():
    serverIP = "150.136.144.166"
    serverPort = 10011

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        soc.connect((serverIP, serverPort))
        message = input("Enter a number to send: ")
        soc.sendall(message.encode())

        data = soc.recv(1024)
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
