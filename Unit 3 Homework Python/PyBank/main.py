# Unit 3 | Assignment - Py Me Up, Charlie
# ## PyBank
import os
import csv
import statistics

output_path = os.path.join("..", "PyBank", "budget_output.csv")
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

totalMonths = []
total = 0
average = []
months = []
dateList = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        total += int(row[1])
        totalMonths.append(row[0])
        average.append(int(row[1]))
        months.append(int(row[1]))
        dateList.append(row[0]) 
        
    faverage = round(statistics.mean(average),2)
    totalMonths = int(len(totalMonths))
    maxNum = max(months)
    minNum = min(months)
    increaseIndex = months.index(max(months))
    decreaseIndex = months.index(min(months))
    
    print("""Financial Analysis
----------------------------""")
    print(f"Total: {total}")
    print(f"Total Months: {totalMonths}")
    print(f"AverageChange: ${faverage}")  
    print(f"Greatest Increase in Profits: {dateList[increaseIndex]} ({max(months)})")
    print(f"Greatest Decrease in Profits: {dateList[decreaseIndex]} ({min(months)})")

    file = open("bankTextFile", "w")   
    file.write(f"Total: {total}\nTotal Months: {totalMonths}\nAverageChange: ${faverage}\nGreatest Increase in Profits: {dateList[increaseIndex]} ({max(months)})\nGreatest Decrease in Profits: {dateList[decreaseIndex]} ({min(months)}) ")
    file.close()