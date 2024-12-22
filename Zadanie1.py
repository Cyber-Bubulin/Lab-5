import re


answer = open('Answer1.txt', 'w')

if __name__ == "__main__":
    with open('task1-en.txt', "r") as text:
        file = text.read()
        search_fig = re.findall(r"Fig. \d{,3}", file)
        search_word = re.findall(r"\b[a-zA-Z]{4}\b", file)
        for i in search_fig:
            answer.write(str(i))
            answer.write('\n')
        for i in search_word:

            answer.write(str(i))
            answer.write('\n')
        
        

