#this is the main project code
import os
# 读取txt文件里的单词
def txt():
    with open(filename) as f:
        raw = f.read().lower()
        words = re.findall('[a-z]+', raw)
    return words
#读取doc文件里的单词
#读取pdf文件里的单词


#main
file_output = r'C:\Users\wang6\Desktop\test.csv'
