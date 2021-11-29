#this is the main project code
import os
import re
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
filenames = os.listdir(os.getcwd())
all_words = []
words = []
for filename in filenames:

    # 排除多余的文件，防止重复计数
    if '.csv' in filename:
        continue
    if '.py' in filename:
        continue
    print(filename)

    # 统计每个pdf文件里面的单词，并且放到一个列表words里面
    # if '.pdf' in filename:
    #     words = pdf_file()
    #     print('len_words is :', len(words))

    # 统计每个Word文件里面的单词，并且放到一个列表words里面
    # if '.docx' in filename:
    #     words = docx_file()
    #     print('len_words is :', len(words))

    # 统计每个TXT文件里面的单词，并且放到一个列表words里面
    if '.txt' in filename:
        words = txt()
        print('len_words is :', len(words))

    # 统计所有文件中的英文单词，并且放进列表里
    # all_words = all_words.extend(words)
    all_words = all_words + words
    print('len_all_words is :', len(all_words))

