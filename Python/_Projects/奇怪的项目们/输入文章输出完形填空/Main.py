import re

for i in range(0, 26):
    fileName = chr(97+i) + '.txt'
    with open(fileName, 'r', encoding='UTF-8') as f:
        english = re.sub(re.compile(r'[\u4e00-\u9fa5]'), '', f.read())  # 去除中文
        words = re.split(r'\W+', english)
        result = [word.lower() for word in words if len(word) > 0]
        for i in result:
            if len(i) < 3:
                result.remove(i)
    with open(fileName+'_list', 'w', encoding='UTF-8') as f:
        for i in result:
            f.write(i+'\n')



def getEnter():
    file = input("Enter the txt file name or content: ")
    if file.endswith('.txt'):
        with open(file, 'r') as f:
            return f.read()
    else:
        return file

result = re.split(r'\W+', getEnter())
result2 = [word.lower() for word in result if len(word) > 0]

print(result2)


