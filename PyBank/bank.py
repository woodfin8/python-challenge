#import dependencies 


import csv
import os

#define csv path
csvpath = os.path.join('budget_data.csv')

#read csv file and skip header
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
   
   #set variables to zero

    month = 0 
    total_profit = 0
    sum_change = 0
    max_change = 0 
    min_change = 0 
    
    #run for loop

    for row in csvreader:
        #start counting months
        month = month + 1

        #month one is different

        if month == 1:
            month_profit = int(row[1]) 
            total_profit = total_profit + month_profit
        
        #run for loop for every other month including change in profit and check f change is max or min. 
        else:
            change = int(row[1]) - month_profit 
            sum_change = sum_change + change
            month_profit = int(row[1])
            total_profit = total_profit + month_profit
            if change > max_change:
                max_change = change
                max_date = row[0]
            elif change < min_change:
                min_change = change
                min_date = row[0]
  
    average_change = round(sum_change/(month-1), 2)

    #check results

    # print(month)
    # print(total_profit)
    # print(average_change)
    # print(max_change)
    # print(max_date)
    # print(min_change)
    # print(min_date)

#print out resutls to terminal
print("Financial Analysis")
print("-------------------------")
print("Total Months: ", month)
print("Total: $",total_profit)
print("Average Change: $",average_change)
print("Greatest Increase in Profits: ", max_date, " $", max_change)
print("Greatest Decrease in Profits: ", min_date, " $", min_change)

#export results to text file
f = open("C:/PythonStuff/Fin_Analys.txt","w")

print("Financial Analysis", file=f)
print("-------------------------", file=f)
print("Total Months: ", month, file=f)
print("Total: $",total_profit,file=f)
print("Average Change: $",average_change,file=f)
print("Greatest Increase in Profits: ", max_date, " $", max_change, file=f)
print("Greatest Decrease in Profits: ", min_date, " $", min_change, file=f)
f.close()


