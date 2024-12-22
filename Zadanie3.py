import re
import csv

answer = open('Answer3.txt', 'w')

if __name__ == "__main__":
    with open("task3.txt") as text:
        file = text.read()
        search_ID = re.findall(r" \d{0,3} ", file)
        search_Surname = re.findall(r" [A-Z]\w* ", file)
        search_email = re.findall(r" \S+@\S+", file)
        search_date = re.findall(r" \d{4}-\d{2}-\d{2} ", file)
        search_site = re.findall(r" http\S+ ", file)
        for i in range(len(search_ID)):
            t = str(search_ID[i]) + '; '+ str(search_Surname[i]) + '; '+str(search_email[i]) + '; ' + str(search_date[i]) + '; ' + str(search_site[i])
            answer.write(str(t))
            answer.write('\n')

    with open("Answer3.csv", 'w', newline = '') as csvfile:
        answercsv = csv.writer(csvfile, delimiter=';')
        for i in range(len(search_ID)):
            answercsv.writerow([search_ID[i], search_Surname[i], search_email[i], search_date[i], search_site[i]])

