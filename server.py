import random
import threading
import socket

#array of quotes
quotes = ["“All our dreams can come true, if we have the courage to pursue them.” —Walt Disney",
"“If people are doubting how far you can go, go so far that you can’t hear them anymore.” —Michele Ruiz",
"“Everything you can imagine is real.”―Pablo Picasso",
"“Smart people learn from everything and everyone, average people from their experiences, stupid people already have all the answers.” —Socrates",
"“If we have the attitude that it’s going to be a great day it usually is.” —Catherine Pulsifier"]

#random quotes from array and send to client
def handle_client(sockfd):
    quote = random.choice(quotes)
    sockfd.sendall(quote.encode())
    sockfd.close()

def main():
    #server ip and port
    bind_ip = "192.168.56.102" 
    bind_port = 8888

    #create and bind socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((bind_ip, bind_port))

    #listen for client
    server.listen(5)
    print("Listen on %s:%d for request" % (bind_ip, bind_port))

    #start connections and execute handle_client function
    while True:
        client, addr = server.accept()
        print("Accepting connection from %s" % str(addr))
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
        
#call main function
main()