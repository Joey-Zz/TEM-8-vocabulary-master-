#this is the main project code
# 读取txt文件里的单词
def txt():
    with open(filename) as f:
        raw = f.read().lower()
        words = re.findall('[a-z]+', raw_words)
#读取doc文件里的单词
#读取pdf文件里的单词

