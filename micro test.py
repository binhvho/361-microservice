import socket
import time
import pickle

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    example = {1234:0, 5678:0}
    print(f"Inventory to send is {example}!")
    send = pickle.dumps(example)
    s.sendall(send)
    time.sleep(2)

    update = 1234, 60
    print(f"Will add {update[1]} to inventory for item {update[0]}!")
    send = pickle.dumps(update)
    s.sendall(send)
    time.sleep(2)

    update = 1234, 60
    print(f"Will add {update[1]} to inventory for item {update[0]}!")
    send = pickle.dumps(update)
    s.sendall(send)
    time.sleep(2)

    request = 1234
    print(f"Will check quantity for item {request}!")
    send = pickle.dumps(request)
    s.sendall(send)
    time.sleep(2)



    while True:
        quantity = ""
        while True:
            quantity = s.recv(1024)
            if len(quantity) > 0:
                quantity = pickle.loads(quantity)
                print(f"Quantity for item {request} is {quantity}!")
                break


