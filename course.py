import sys
import string
import re
import datetime
import csv

def readLines():
    input = []
    for line in sys.stdin:
        input.append(line.strip("\n"))
    return input
    
def insertLabs(x, courses):
    for course in courses:
        indexer = -4
        if int(course[1]) == 0:
            continue    
        z = 1
        y = int(52/(int(course[1])+1))
        while z <= int(course[1]): 
            indexer = indexer + y
            while(x[indexer] is not None):
                indexer = (indexer + 3)%52
            x[indexer] = course[0] + " Lab" + str(z)
            z = z + 1
    return x        
        

def insertMidterms(x, courses):
    for course in courses:
        indexer = 1
        if int(course[3]) == 0:
            continue    
        z = 1
        y = int(52/(int(course[3]) + 1))
        while z <= int(course[3]): 
            indexer = indexer + y
            while(x[indexer] is not None):
                indexer = (indexer + 3)%52
            x[indexer] = course[0] + " Midterm" + str(z)
            z = z + 1
    return x
    
def insertAssignments(x, courses):
    for course in courses:
        indexer = -3
        if int(course[2]) == 0:
            continue    
        z = 1
        y = int(52/(int(course[2]) + 1))
        while z <= int(course[2]): 
            indexer = (indexer + y)%52
            while((x[indexer] is not None)):
                    indexer = (indexer + 3)%52
            x[indexer] = course[0] + " Assignment"
            z = z + 1
    return x

def toGoogleCalender(calender, finals):
    calenderCSV = []
    calenderCSV.append("Subject,Start Date")
    septStart = datetime.datetime(2018, 9,10)
    finalsStart = datetime.datetime(2018, 12,3)

    for i in range(0,77):
        if calender[i] != None and calender[i] != "weekend":
            eventDate = septStart + datetime.timedelta(days=i)
            eventStr = calender[i] + "," + eventDate.strftime('%m/%d/%Y')
            calenderCSV.append(eventStr)
            # print(eventStr)
    
    for i in range(0,15):
        if finals[i] != None:
            eventDate = finalsStart + datetime.timedelta(days=i)
            eventStr = finals[i] + "," + eventDate.strftime('%m/%d/%Y')
            calenderCSV.append(eventStr)

    
    with open('googleCalender.csv', 'w') as csv_file:
        #writer = csv.writer(csv_file, delimiter=',')    
        for line in calenderCSV:
            #writer.writerow(line)
            csv_file.write(line)
            csv_file.write('\n')
            print(line)
            
def convertTo77(calender52):
    # 52 to 55 conversion
    nov12 = 45 #check for off by one
    nov13 = 46
    nov14 = 47
    calender55 = []
    dayIn52 = 0
    for i in range(55):
        if (i!=nov12) and (i!=nov13) and (i!=nov14) :
            calender55.append(calender52[dayIn52])
            dayIn52 += 1
            #print(dayIn52)
        else:
            calender55.append("reading break")
    #print(calender55)
    
    calender77 = []
    dayIn55 = 0
    for i in range(77):
        #if saturday or sunday print weekend
        if (i%7!=5) and (i%7!=6) :
            calender77.append(calender55[dayIn55])
            dayIn55 += 1
        else:
            calender77.append("weekend")
    # print(calender77)
    return calender77


def main():
    splitLine = []
    input = readLines()
    for line in input:
        splitLine.append( line.split())
    for line in splitLine:
        numLabs = re.match(r'L(\d+)', line[1])
        numAssign = re.match(r'A(\d+)', line[2])
        numMidterm = re.match(r'M(\d+)', line[3])
        line.append(numLabs.group(1))
        line.append(numAssign.group(1))
        line.append(numMidterm.group(1))
    courses = []
    for x in splitLine:
        courses.append([x[0],x[6],x[7],x[8]])
    
    x = [None] * 52
    
    x = insertLabs(x, courses)
    x = insertMidterms(x, courses)
    x = insertAssignments(x, courses)
    #print(x)
    
    for line in splitLine:
        weightFinals = re.match(r'PA(\d+)', line[5])
        line.append(weightFinals.group(1))
    finalOrder = [(q[-1],q[0])   for q in splitLine]
    finalOrder.sort(key=lambda tup: tup[0])
    finalOrder.reverse()
    exams = [None] * 15
    t = int(15/(len(finalOrder) + 1))
    counter = 0;
    for exam in finalOrder:
        counter = counter + t
        exams[counter] = exam[1] + " Final"
    #print(exams)

    
    calender77 = convertTo77(x)  
    # print(calender77)
    toGoogleCalender(calender77, exams)
        
if __name__ == "__main__":
    main()


