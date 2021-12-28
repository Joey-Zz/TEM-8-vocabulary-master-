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

# 统计单词数目，按照词频逆排序，然后从出现个数最多的单词开始记忆，迅速提高学习效率
def count(words):
    words_set = set(words)
    number_words = len(words)  # 六级题总共出现的单词数目，包括重复的单词数目
    number_words_set = len(words_set)  # 需要记忆的单词个数
    print('需要记忆的单词个数', number_words_set)
    print('总共出现的单词数目', number_words)

    # 用hash计算每个单词出现次数
    hash = {}
    for word in words:
        if word not in hash:
            hash[word] = 1
        else:
            hash[word] += 1
    sorted_hash = sorted(hash, reverse=False)  # 按照ABC顺序排列,没有重复单词,只有英文单词
    # sorted_hash = sorted(hash.values(), reverse = True)
    # print(sorted_hash)
    data = sorted(hash.items(), key=lambda x: x[1], reverse=True)  # 按照出现次数排列，没有重复单词
    return data  # 返回列表，每个元素是一个元组，左边是单词，右边是单词出现次数




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

