import csv

#one time use only to create .csv file for calorie==============================

with open('fruit_calorie.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Fruit", "calorie"])
    writer.writerow(["Apple", "52"])
    writer.writerow(["Banana", "89"])
    writer.writerow(["Grape", "82"])
