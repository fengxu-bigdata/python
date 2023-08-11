import hashlib, os


def getMD5(filepath):
    f = open(filepath, 'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    f.close()
    return str(hash).upper()


path = input("请输入存在重复文件的文件夹路径：")
file_list = os.listdir(path)
file_md5 = []
for filename in file_list:
    md5 = getMD5(path + "\\" + filename)
    if md5 in file_md5:
        os.remove(path+"\\"+filename)
    else:
        file_md5.append(md5)
print("重复文件处理完毕...")