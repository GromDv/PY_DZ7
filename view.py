import model as m
import data_export as de

def Prompt():
    inpt = int(input(cRed('Что делаем?\n')+cGreen('1 - Вывести справочник на экран\n2 - Ввести новую запись\n3 - Сохранить справочник в файл\n4 - Загрузить справочник из файла\n5 - Вывести имя/фамилию на экран\n6 - Сортировать по имени\n7 - Сортировать по id\n8 - Сортировать по фамилии\n9 - Закончить работу\n: ')))
    return inpt

esc = lambda code: f'\033[{code}m'
cGreen = lambda y: esc('32')+y+esc('0')
cRed = lambda y: esc('31')+y+esc('0')

# Строка содержит id,имя,фамилию,номер телефона, комментрий - символ разделитель на выбор(можно использовать пробел или запятые)
# id будем присваивать автоматически
def NewData():
    data_in = input(cRed("Укажите последовательно через пробел - имя, фамилию, номер телефона, комментрий: "))
    m.data_add(data_in)

def PrintDB():
    sps = m.GetDataDB()
    for i in sps:
        for j in range(len(i)):
            if j == len(i)-1:
                print(f'{i[j]}', end="")
            else:
                print(f'{i[j]:12} ', end="")
        print()
    print()
        
def DB2str():
    sps = m.GetDataDB()
    res = ""
    for i in sps:
        for j in range(len(i)):
            if j == len(i)-1:
                res += str(i[j])
            else:
                res += str(i[j]) + " "
        res += "\n"
    return res

def PrintNF():
    sps = m.GetDataDB()
    for i in sps:
        for j in range(1,3):
            print(str(i[j]), end=" ")
        print()