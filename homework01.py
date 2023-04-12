def factorial():
    list = []
    number = int(input("Введите число: "))
    result = 1
    for i in range(1,number+1):
        result = result * i
        list.append(result)
    print(list)

factorial()