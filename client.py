import pickle
import socket

from crypt_utils import DiffieHellman, FileCrypter

HOST = '127.0.0.1'
PORT = 2000


def main():
    sock = socket.socket()
    sock.connect((HOST, PORT))

    p = 54
    g = 53
    a = 63  # это можно хранить в txt


    sock.send(pickle.dumps((p, g, client_mixed_key)))
    sock.close()

    sock = socket.socket()
    sock.connect((HOST, PORT))
    crypter = FileCrypter(private_key)

    msg = input("Enter msg: ")
    result = crypter.encryption(msg)
    print(result)
    sock.send(pickle.dumps(result))

    result = crypter.encryption(result)
    print(result)

    sock.close()


if __name__ == "__main__":
    main()