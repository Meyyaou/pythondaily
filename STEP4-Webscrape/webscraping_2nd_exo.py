
import csv

with open("input.csv", "r") as file:
  reader = csv.DictReader(file, delimiter=",")
  for line in reader:
    datas.append(line)
    
with open('ouput.csv', 'w') as file:
  writer = csv.writer(file, delimiter=',')
  writer.writerow(['nom', 'salaire'])

  for data in datas:
    if data.isdigit():
      writer.writerow(data*15)
    else:
      writer.writerow(data)
