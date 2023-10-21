# 这是一个关于文件路径的库
from pathlib import Path

path01 = Path("a")
print(path01.exists())    # 判断当前目录下是否存在名为"a"的路径

path02 = Path("testDir1")
path02.mkdir()  # 创建一个文件路径(文件夹)

path03 = Path("testDir2")
path03.rmdir()  # 删除一个文件路径(文件夹)

path04 = Path()
path04.glob('*.*')  # 查找文件
# 当前查找方式为'*.*'(全部格式的所有文件)，除此之外还有'*'(查找所有文件和文件夹), '*.py'(查找所有后缀为py的所有文件)，以此类推'*.txt'(查找所有后缀为txt的文件)
for file in path04.glob('*.*'):  # 不过使用for循环遍历一下才能输出所有文件名呢
    print(file)


