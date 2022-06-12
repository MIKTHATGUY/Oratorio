import os,json, openpyxl
import time
import itertools
import shelve
import numpy as np


grandi = 0
piccoli = 0


def chunks(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


blu = []
rossi = []
gialli = []
verdi = []


a2016 = []
a2015 = []
a2014 = []
a2013 = []
a2012 = []
a2011 = []
a2010 = []
a2009 = []
a2008 = []
wb = openpyxl.load_workbook(r'Cartel1.xlsx')
sheet = wb.active

maxro = len(sheet['A'])

n = 0
for item in os.listdir("./Bambini/"):
    n += 1    
    with open(f"./Bambini/{item}/{item}.json", "r") as jsonFile:
        data = json.load(jsonFile)

    
    globals()[data["anno"]].append(data["nome"])




    

    


print(f"2016 : {len(a2016)}")
print(f"2015 : {len(a2015)}")
print(f"2014 : {len(a2014)}")
print(f"2013 : {len(a2013)}")
print(f"2012 : {len(a2012)}")
print(f"2011 : {len(a2011)}")
print(f"2010 : {len(a2010)}")
print(f"2009 : {len(a2009)}")
print(f"2008 : {len(a2008)}")
print(f"Totale : {n}")



print(chunks(a2015,4))
rossi.append(chunks(a2016, 4)[0])
blu.append(chunks(a2016, 4)[1])
verdi.append(chunks(a2016, 4)[2])
gialli.append(chunks(a2016, 4)[3])


rossi.append(chunks(a2015, 4)[0])
blu.append(chunks(a2015, 4)[1])
verdi.append(chunks(a2015, 4)[2])
gialli.append(chunks(a2015, 4)[3])


rossi.append(chunks(a2014, 4)[0])
blu.append(chunks(a2014, 4)[1])
verdi.append(chunks(a2014, 4)[2])
gialli.append(chunks(a2014, 4)[3])


rossi.append(chunks(a2013, 4)[0])
blu.append(chunks(a2013, 4)[1])
verdi.append(chunks(a2013, 4)[2])
gialli.append(chunks(a2013, 4)[3])


rossi.append(chunks(a2012, 4)[0])
blu.append(chunks(a2012, 4)[1])
verdi.append(chunks(a2012, 4)[2])
gialli.append(chunks(a2012, 4)[3])


rossi.append(chunks(a2011, 4)[0])
blu.append(chunks(a2011, 4)[1])
verdi.append(chunks(a2011, 4)[2])
gialli.append(chunks(a2011, 4)[3])


rossi.append(chunks(a2010, 4)[0])
blu.append(chunks(a2010, 4)[1])
verdi.append(chunks(a2010, 4)[2])
gialli.append(chunks(a2010, 4)[3])


rossi.append(chunks(a2009, 4)[0])
blu.append(chunks(a2009, 4)[1])
verdi.append(chunks(a2009, 4)[2])
gialli.append(chunks(a2009, 4)[3])


rossi.append(chunks(a2008, 4)[0])
blu.append(chunks(a2008, 4)[1])
verdi.append(chunks(a2008, 4)[2])
gialli.append(chunks(a2008, 4)[3])

rossi = list(itertools.chain(*rossi))
blu = list(itertools.chain(*blu))
verdi = list(itertools.chain(*verdi))
gialli = list(itertools.chain(*gialli))
print("-----------------------------------------------------")
print(len(rossi))
print(len(blu))
print(len(verdi))
print(len(gialli))

print(len(verdi)+len(gialli)+len(blu)+len(rossi))



bambini = [rossi, blu, verdi, gialli]
n = 0

print(maxro)

start_time = time.time()
for i in rossi:
    for x in range(0,maxro):
        if i == sheet['A'][x].value:
            sheet['D'][x].value = "rosso"
print("--- %s seconds ---" % (time.time() - start_time))



for i in blu:
    for x in range(0,maxro):
        if i == sheet['A'][x].value:
            sheet['D'][x].value = "blu"


for i in verdi:
    for x in range(0,maxro):
        if i == sheet['A'][x].value:
            sheet['D'][x].value = "verde"


for i in gialli:
    for x in range(0,maxro):
        if i == sheet['A'][x].value:
            sheet['D'][x].value = "giallo"









wb.save(r'Cartel1.xlsx')


    
        





 

print(f"Grandi: {grandi}")
print(f"Piccoli: {piccoli}")