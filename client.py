# -*- coding: utf-8 -*-
import socket
import sys
import jieba


if __name__ == '__main__':
    host = 'localhost'
    port = 8899
    fi = str(sys.argv[1])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    msg = open(fi).read()
    s.connect((host, port))
    s.sendall(msg)
    s.close()

