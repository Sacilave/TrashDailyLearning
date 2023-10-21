### 入门 ###
from nltk.book import *
# 查找词语
text5.concordance("lol")
# 搜索相似词
text1.similar("monstrous")
# 搜索共同上下文
text1.common_contexts(["monstrous", "stupid"])
# 词汇分布图
text4.dispersion_plot(["democracy", "citizens", "freedom", "duties", "America"])
# 词语统计
len(text1)  # 计算所有对象(包括词语和标点)
sorted(set(text1))  # 不重复的返回所有的词语
len(set(text1))  # 不重复的统计全部词语数量
# 重复词密度
len(text1) / len(set(text1))  # text1的词语数量除以text1的不重复词语的数量
# 关键词数量。。。（这他妈还要写注释吗。。）
text1.len("stupid")
# 关键词密度
100 * text1.count("smoke") / len(text1)
