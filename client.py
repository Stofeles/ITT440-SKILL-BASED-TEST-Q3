import socket

def main():
    #IP and port of the server
    server_ip = "192.168.56.102"
    server_port = 8888

    # Create socket 
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    sockfd.connect((server_ip, server_port))

    # Request a quote from server
    quote = sockfd.recv(1024)
    print("                    WELCOME TO THE QUOTES OF THE DAY!                     ")
    print("--------------------------------------------------------------------------")
    print("Today quotes is -> %s" % quote.decode())

    # Close socket 
    sockfd.close()

#execute main
main()