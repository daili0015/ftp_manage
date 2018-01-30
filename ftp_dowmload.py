# !/usr/bin/python
# -*- coding: utf-8 -*-
from ftplib import FTP

ftp_port = 2121
ftp_address = "127.0.0.1"
USER = 'zcy_ftp_download'
PWD = '529932zcy_0xy'

def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, ftp_port)
    ftp.login(username, password)
    return ftp

#从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

#下载
ftp = ftpconnect(ftp_address, USER, PWD)
downloadfile(ftp, "ftp_server.py", "C:/Users/zcy/Desktop/Desktop/ftp_server.py")
ftp.quit()

# os.system('start "C:\Program Files\Windows Media Player\wmplayer.exe" "C:/Users/Administrator/Desktop/test.mp4"')
#上传
ftp = ftpconnect(ftp_address, USER, PWD)
uploadfile(ftp, "/zcy/ftp_server2.py", "C:/Users/zcy/Desktop/Desktop/ftp_server.py")
ftp.quit()