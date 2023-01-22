import model as m
import view as w
import data_export as de
import data_import as di


while True:
    op = w.Prompt()
    if op == 1:
        w.PrintDB()
    elif op == 2:
        w.NewData()
        w.PrintDB()
    elif op == 3:
        de.data_exportDB()
    elif op == 4:
        di.data_importDB()
    elif op == 5:
        w.PrintNF()   
    elif op == 6:
        m.Sorting(1)
        w.PrintDB()
    elif op == 7:
        m.Sorting(0)
        w.PrintDB()
    elif op == 8:
        m.Sorting(2)
        w.PrintDB()
    elif op == 9:
        break

def start():
    m.data_init()



