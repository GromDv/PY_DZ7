import data_import as di

dataDB = []

def data_init():
    return

def GetDataDB():
    return dataDB

def data_add(data):
#    print(data)
    dataList = data.split(" ")
    ind = len(dataDB)
    dataList.insert(0,ind+1)
    dataDB.append(dataList)
    print(dataDB)

def SetDataDB(data):
    global dataDB
    dataDB = data

nam = lambda x: x[1]
ind = lambda x: x[0]

def Sorting(pos):
    global dataDB
    for k in range(len(dataDB)):
        temp = dataDB[k]
        ti = k
        for i in range(k,len(dataDB)):
            if temp[pos] > dataDB[i][pos]:
                temp = dataDB[i]
                ti = i
        dataDB[ti] = dataDB[k]
        dataDB[k] = temp

