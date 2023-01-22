import model as m
import view as w

def data_append(data):
    res = []
    f = open("data.txt", "a")
    f.write('\n')
    f.write(data)
    
    f.close
    return res

def data_exportDB():
    f = open("data.txt", "w")
    data = w.DB2str()
    f.write(data)
    # for line in data:
    #     f.write(str(line))
    #     f.write('\n')
    f.close
