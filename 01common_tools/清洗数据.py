import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def text_clean(text):
    # 去掉html标签
    text1 = re.sub(r'\&\w*; | #\w* | @\w*', '', text)

    # 去掉价值符号
    text2 = re.sub(r'\$\w*', '', text1)

    # 去掉超链接
    text3 = re.sub(r'https?:\/\/.*\/\w*', '', text2)

    # 去掉专门的名词缩写
    text4 = re.sub(r'\bw{1, 2}\b', '', text3)

    # 去掉多余空格
    text5 = re.sub(r'\s{1, }', ' ', text4 )
    text5 = text5.lstrip()

    # 分词
    tokens = word_tokenize(text5)

    # 去掉停用词
