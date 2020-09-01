# 给定一系列大小不同的文件，用 python 计算出每个文件的大小，然后按照文件大小从小到大批量命名为1，2，3..... 
import os

rootdir = "D:/test/"
file_names = os.listdir(rootdir)
file_sizes = dict()
for file_name in file_names:
    path = os.path.join(rootdir, file_name)
    file_size = os.stat(path).st_size
    file_sizes[file_name] = file_size

sorted_file_sizes = sorted(file_sizes.items(), key = lambda item:item[1])
for i in range(1, len(sorted_file_sizes) + 1):
    old = rootdir + sorted_file_sizes[i - 1][0]
    suffix = os.path.splitext(old)[1]
    new = rootdir + str(i) + suffix
    os.rename(old, new)
    



