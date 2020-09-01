# 将需要备份的文件和文件夹打包成压缩文件，再复制到指定路径下
import os, zipfile, os.path
from shutil import copyfile

def make_zip(source_dir, output_filename):
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)  
            zipf.write(pathfile, arcname)
    zipf.close()


source_dir = input("please input sourcedir: ")
target = input("please input targetdir: ")

tmp_dir = "D:/tmp/"
tmp_file_name = "backup.zip"

if not os.path.exists(source_dir):
    print(source_dir + " 路径不存在")
    exit()

if not os.path.exists(target):
    print(target + " 路径不存在")
    exit()

make_zip(source_dir, tmp_dir + tmp_file_name)
copyfile(tmp_dir + tmp_file_name, target + tmp_file_name)
os.remove(tmp_dir + tmp_file_name)
