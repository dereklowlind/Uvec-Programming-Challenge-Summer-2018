#https://stackoverflow.com/questions/6871016/adding-5-days-to-a-date-in-python

import datetime
import csv
calender = [] # contains the activity at index i
for i in range(0,77):
    calender.append("none")

calender[2] = "elecA1"  
calender[76] = "chem midterm"  
    

calenderCSV = []
# csvFirstLine = []
# csvFirstLine.append("Subject")
# csvFirstLine.append("Start Date")
calenderCSV.append("Subject,Start Date")
septStart = datetime.datetime(2018, 9,10)

for i in range(0,77):
    #print(calender[i])
    # no eventssaturday or sunday
    #if (i%7!=6) or (i%7!=7):
    if calender[i] != "none":
        eventDate = septStart + datetime.timedelta(days=i)
        eventStr = calender[i] + "," + eventDate.strftime('%m/%d/%Y')
        calenderCSV.append(eventStr)
        # print(eventStr)
        
with open('googleCalender.csv', 'w') as csv_file:
    #writer = csv.writer(csv_file, delimiter=',')    
    for line in calenderCSV:
        #writer.writerow(line)
        csv_file.write(line)
        csv_file.write('\n')
        print(line)