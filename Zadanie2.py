import re

Answer = open('Answer2.txt', 'w')

if __name__ == "__main__":
    with open('task2.txt', 'r', encoding="utf-8") as text:
        file = text.read()
        search_style = re.findall(r"font-style: \w{,8}", file)
        search_weight = re.findall(r"font-weight: \d{,8}", file)
        for i in range (len(search_style)):
            a = str(search_style[i]) + '; ' + str(search_weight[i])
            Answer.write(a)
            Answer.write('\n')
        