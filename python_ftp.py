from ftplib import FTP
import time
import tarfile
import os

from ftplib import FTP

def ftpconnect(host, port, username, password):
    # 设置变量
    ftp = FTP()
    # 连接到给定的主机和端口
    ftp.connect(host, 21) 
    # 以给定的用户登录
    ftp.login(username, password)
    return ftp

# 从 ftp 下载文件
def downloadfile(ftp, remotepath, localpath):
    # 设置缓冲区大小
    bufsize = 1024
    fp = open(localpath, "wb")
    # 在二进制传输模式下检索文件
    ftp.retrbinary("RETP " + remotepath, fp.write, bufsize)
    # 设置实例的调试级别，参数为0，关闭调试模式
    ftp.set_debuglevel(0)
    fp.close()

# 从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, "rb")
    ftp.storbinary("STOR " + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":
    ftp = ftpconnect("ftp.abcdrueser.com", 21, "FTXBAGM", "s2JkUaSl9M")
    # 上传文件，第一个是要上传到ftp服务器路径下的文件，第二个是本地要上传的路径文件
    uploadfile(ftp, "/wwwroot/aaa.txt", "D:/aaa.txt")
    # 下载文件，第一个是ftp服务器路径下的文件，第二个是要下载到本地的路径文件
    downloadfile(ftp, "/wwwroot/aaa.txt", r"D:/vm/bbb.txt")
