#fixed some bad patterns
#ETL
import csv

def extract():
  datas=[]
  with open("input.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=",")
    for line in reader:
      datas.append(line)
  return datas
  
def transform(da):
  d=[]
  for data in da:
    trans_data={}
    trans_data['nom']=data['nom']
    data['heures_travaillees']=int(data['heures_travaillees'])*15
    trans_data['salaire']=str(data['heures_travaillees'])
    d.append(trans_data)
  return d
  
def load(d):
  with open('ouput.csv', 'w') as file:
   # writer = csv.writer(file, delimiter=',')
   # writer.writerow(['nom', 'salaire']) next line is better:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
  for data in d:
    if data.isdigit(): # this is VERY unspecific => BAD
      writer.writerow(data*15)
    else:
      writer.writerow(data)
""" better structure of code
def main():
  d_to_trans=extract()
  d_to_load=transform(d_to_trans)
  load(d_to_load)

if __name__=="__main__":
  main()
"""
