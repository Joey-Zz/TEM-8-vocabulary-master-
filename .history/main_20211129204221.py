#this is the main project code
import os
import re
import pdfplumber 
# 读取txt文件里的单词
def txt():
    with open(filename) as f:
        raw = f.read().lower()
        words = re.findall('[a-z]+', raw)
    return words
#读取doc文件里的单词
#读取pdf文件里的单词
def pdf_file():
    pdf = pdfplumber.open(filename)
    raw_words = ''  # 保存所有的单词
    for page in pdf.pages:
        raw_words = raw_words + str(page.extract_words())  # 两页，两个列表
    raw_words = raw_words.lower()

    words = re.sub('decimal', '', raw_words)  # 删除字符串里面所有的decimal,
    words = re.sub('top', '', words)
    words = re.sub('bottom', '', words)
    # words = re.sub('x', '', words)
    words = re.sub('text', '', words)

    words = re.findall('[a-z]+', words)  # 得到所有的英文单词，排除了汉语单词，各种符号

    while 'x' in words:
        words.remove('x')
    return words




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
    if '.pdf' in filename:
        words = pdf_file()
        print('len_words is :', len(words))
        print(words)

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

