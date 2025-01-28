import pandas as pd
import csv


def convert():
    excel_file = pd.read_excel("test.xlsx")
    clear_csv("test.csv")
   


def clear_csv(filename):
   csv_file = pd.read_csv(filename, skiprows=1)
   print(csv_file)

   data = pd.DataFrame(csv_file)
   print(data)
  
  # drop first 2 colums
   cf = data.drop(data.columns[[0, 2, 7]], axis=1)
   print(cf)

   # rename columns
   cf = cf.rename(columns={cf.columns[0]: 'date', cf.columns[1]: 'payee', cf.columns[2]: 'memo', cf.columns[3]: 'outflow', cf.columns[4]: 'inflow'})
   print(cf)

   cf.to_csv("test.csv", index=None, header=True)

if __name__ == '__main__':
    convert()
    


