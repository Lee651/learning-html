# 计算文件的大小
import os
import datetime

def toKb(bytesize):
    return f'{bytesize / 1024: .2f} Kb'

def toMb(bytesize):
    return f'{bytesize / 1024 / 1024: .2f} Mb'

def get_time(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

file_name = "D:/test/git.txt"
file_size = os.stat(file_name).st_size
firname = "D:/test"

fileinfo = os.stat(file_name)

print(file_size, toKb(file_size), toMb(file_size))
print("访问时间：", get_time(fileinfo.st_atime))
print("创建时间：", get_time(fileinfo.st_ctime))