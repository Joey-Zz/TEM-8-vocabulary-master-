#this is the main project code
import os
import re
import pdfplumber 
import docx
# 读取txt文件里的单词
def txt():
    with open(filename) as f:
        raw = f.read().lower()
        words = re.findall('[a-z]+', raw)
    return words
#读取doc文件里的单词
def doc():
    file = docx.Document(filename)
    raw_words = '' 
    for para in file.paragraphs:
        raw_words += para.text 
    raw_words = raw_words.lower()
    words = re.findall('[a-z]+', raw_words) 
    return words

#读取pdf文件里的单词
def pdf():
    pdf = pdfplumber.open(filename)
    raw_words = '' 
    for page in pdf.pages:
        raw_words = raw_words + str(page.extract_words())  
    raw_words = raw_words.lower()

    words = re.sub('decimal', '', raw_words) 
    words = re.sub('top', '', words)
    words = re.sub('bottom', '', words)
 
    words = re.sub('text', '', words)

    words = re.findall('[a-z]+', words) 

    while 'x' in words:
        words.remove('x')
    return words




#main
filenames = os.listdir(os.getcwd())
all_words = []
words = []
for filename in filenames:

 
    if '.csv' in filename:
        continue
    if '.py' in filename:
        continue
    print(filename)

    # 读取pdf文件，并将所有英文单词放到列表里
    if '.pdf' in filename:
        words = pdf()
        print('len_words is :', len(words))
        # print(words)

    # 读取word文件，并将所有英文单词放到列表里
    if '.docx' in filename:
        words = doc()
        print('len_words is :', len(words))

    # 读取txt文件，并将所有英文单词放到列表里
    if '.txt' in filename:
        words = txt()
        print('len_words is :', len(words))

    # 统计所有文件里的所有单词
    all_words = all_words + words
    print('len_all_words is :', len(all_words))

