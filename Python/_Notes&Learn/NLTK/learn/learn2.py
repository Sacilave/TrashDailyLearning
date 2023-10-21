### 列表(链表) ###
from nltk.book import *
# 创建
list1 = ["ass", "kick", "back", "shit"]
list2 = ["shut", "beat"]
print(list1, list2)
# 拼接
list3 = list1 + list2
print(list3)
# 追加
list1.append("add")
print(list1)
# 索引
print(text4[173])
print(text4.index("a"))
# 切片
print(text1[1223: 1544])
# 注意索引从0开始
sent = ["word1", "word2", "word3", "word4", "word5"]
print(sent[0])
print(sent[0:2])  # 结果将为：['word1', 'word2']
print(sent[: 3])  # 结果将为：['word1', 'word2', 'word3']
print(sent[0: ])  # 结果将为：['word1', 'word2', 'word3', 'word4', 'word5']
# 计算频率
fdist1 = FreqDist(text1)
fdist1.plot(50, cumulative=True)  # 选取50个词进行绘表（cumulative=True就是设置绘表为真）
fdist1['whale']  # 计算'whale'这个词出现过的次数
fdist1.hapaxes()  # 列出低频次的词语

