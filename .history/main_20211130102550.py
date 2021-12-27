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




