import socket
import time
import pickle
from collections.abc import Mapping

HEADERSIZE = 10
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

inventory = {}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            received = ""
            while True:
                received = conn.recv(1024)
                if len(received) > 0:
                    received = pickle.loads(received)
                    print(f"Received {received}!")
                    if isinstance(received, Mapping):
                        inventory = received
                        print(f"Inventory is {inventory}")
                        received = ""
                    elif isinstance(received, tuple) and len(received) == 2:
                        inventory[received[0]] = inventory[received[0]] + received[1]
                        print(f"Inventory is {inventory}")
                        received = ""
                    elif isinstance(received, int) and received in inventory:
                        print(f"Item {received} has {inventory[received]} quantity.")
                        send = pickle.dumps(inventory[received])
                        conn.sendall(send)
                        received = ""

