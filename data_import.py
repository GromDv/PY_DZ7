import model as m

def data_importDB():
    res = []
    tmp = []
    f = open("data.txt", "r")
    for line in f:

        # line = str(line).replace("[","")
        # line = str(line).replace("]","")
        # line = str(line).replace("'","")
        # line = str(line).replace(" ","")
        line = str(line).replace("\n","")
        #print(line)
        tmp = line.split(" ")
        #print(tmp)
        tmp[0] = int(tmp[0])
            
        res.append(tmp)
    f.close

    m.SetDataDB(res)