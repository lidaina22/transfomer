import re

file_path = "/Users/lidaina/PycharmProjects/Transfomer/demo/the-verdict.txt"

with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

'''
Step1: 分词器
'''
base_pattern = r'[\u4e00-\u9fa5]|[a-zA-Z0-9]+|[，。！？,.:;!?()（）]'
result = re.findall(base_pattern, raw_text)
result = [item.strip() for item in result if item.strip()]

"""
Step2: 构建词汇表
"""
all_words = sorted(set(result))
vocab = {token: integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
'''
Step3: 转化词元ID
'''


def encode():
    ids = [vocab[s] for s in result]
    print(ids)


encode()

'''
Optional Step4: 还原词元ID回文本格式
'''


def decode(ids):
    int_to_str = {index: s for s, index in vocab.items()}
    text = "".join(int_to_str[i] for i in ids)
    print(text)


ids = [vocab[s] for s in result]
decode(ids)

"""
Step5: 引入特殊上下文词元 
       用特殊次元让模型处理未知的词元以及上下文的边界
       
       模型不认识的词元使用 <|unk|> 代替
       上下文使用 <|endoftext|> 标记
"""
#all_words.extend("<|endoftext|>", "<|unk|>")


def encodeOptimized():
    tokens = re.findall(base_pattern, raw_text)
    processed = [item.strip() for item in tokens if item.strip()]
    processed = [item if item in vocab
              else "<|unk|>" for item in processed]
    ids = [vocab[s] for s in processed]
    print(ids)