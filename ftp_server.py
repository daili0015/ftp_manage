#-*-coding:utf-8-*-
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer  # <-
from pyftpdlib.authorizers import DummyAuthorizer

ftp_port = 2121
ftp_address = "127.0.0.1"
ftp_root = 'C:\Users\zcy\Desktop\Desktop\server'
USER = 'zcy_ftp_download'
PWD = '529932zcy_0xy'

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user(USER, PWD, ftp_root, perm='elradfmw')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = ThreadedFTPServer((ftp_address, ftp_port), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()