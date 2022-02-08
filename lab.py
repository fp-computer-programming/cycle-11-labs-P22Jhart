lab_py = open("alma_mater.txt", "r")
while True:
     line = lab_py.readline()
     if len(line) == 0:
           break
     print (line, end="")
lab_py.close()