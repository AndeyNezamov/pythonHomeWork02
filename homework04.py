def mas():
    number = int(input('Введите число: '))
    list = []
    for i in range(-number, number+1):
        newElement = -number
        list.append(newElement+(i+number))
    print(list)
    for j in range(len(list)):
        list[-1], list[j] = list[j] , list[-1]
        list[-2], list[j] = list[j] , list[-2]
    print(list)
mas()
