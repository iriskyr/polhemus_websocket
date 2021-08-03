import time
import socket
import codecs


for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = b'test'
    #addr = ("127.0.0.1", 12000)
    addr = ("localhost", 5123)

    start = time.time()
    #client_socket.sendto(message, addr)
    client_socket.bind(addr)
    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print(f'{data} {pings} {elapsed}')
        u = unicode(data, 'UTF-8')
        print(codecs.decode(data))
    except socket.timeout:
        print('REQUEST TIMED OUT')


# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(consume(hostname="localhost", port=5123))
#     loop.run_forever()


# import socket
#
# # Number of bytes to get
#
# numBytes2Get = 2048
#
# # Create a UDP socket. UDP is datagram based.
#
# destination = ("192.168.1.1", 5123)
#
# udpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # Send quote request
#
# sentBytesCount = udpClientSocket.sendto("boo".encode(), destination)
# print(sentBytesCount)
#
#
# # Use receivefrom() to get quote
#
# receivedBytes = udpClientSocket.recvfrom(numBytes2Get)
#
# # Print the quote
#
# print(receivedBytes[0].decode())

#
# import websocket
# hostname = "localhost"
# port = 5123
# ws = websocket.WebSocketApp(f"ws://{hostname}:{port}") #create_connection("ws://localhost:8080/websocket")
# print("Sending 'Hello, World'...")
# ws.send("Hello, World")
# print("Sent")
# print("Receiving...")
# result =  ws.recv()
# print("Received '%s'" % result)
# ws.close()