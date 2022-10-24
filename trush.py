#Метод Цезаря
vocablurary = 'abcdefhgijklmnopqrstuwxyz'
step = int(input("step : "))
message = input('Сообщение для дешифровки ').lower()
result = ''

for i in message:
    area = vocablurary.find(i)
    new_area = area + step
    if i in vocablurary:
        result += vocablurary[new_area]
    else:
        result += 1

print(result)
deresult = ''

for i in result:
    area = vocablurary.find(i)
    new_area = area - step
    if i in vocablurary:
        deresult += vocablurary[new_area]
    else:
        deresult += 1

print(deresult)