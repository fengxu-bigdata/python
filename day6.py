import re, day1

path = input("请输入文件路径：")

word = re.findall('([\u4e00-\u9fa5])', day1.get_str(path))

print("中文字符有：" + str(word) + "除特殊字符外共有：" + str(len(word)))
