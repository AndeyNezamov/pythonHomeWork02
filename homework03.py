firstString = input('Введите первую строку: ')
secondString = input('Введите вторую строку: ')
for i in range(len(firstString)):
    count = 0
    for j in range(len(secondString)):
        if firstString[i] == secondString[j]:
            count+=1
    print(firstString[i],'-', count)