from translate import Translator
import day1

translator = Translator(to_lang="Chinese")

path = input("请输入文件路径：")
text = day1.get_str(path)
translation = translator.translate(text)
print(translation)
