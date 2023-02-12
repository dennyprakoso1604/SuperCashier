from tabulate import tabulate
from dataclasses import dataclass
import pandas as pd
import numpy as np

class transaction:
  def __init__(self,transactionID):
    self.transactionID = transactionID

transaction_1 = transaction(1)
transaction_123 = f'TRX {transaction_1.transactionID}'
print(transaction_123)    
    

list_item = ({
    'nama_item':[],
    'jumlah_item' :[],
    'harga_item':[],
    'total_harga':[]
               })

menu1 = 'y'

while menu1 == 'y':
  print(list_item)
  print("choose menu: 1.input item 2.edit item 3.check list 4.delete item 5.total harga 6.exit")
  menu=int(input())
  if menu == 1:
      a=input("masukan nama item ")
      b=int(input("masukan jumlah item "))
      c=int(input("masukan harga item "))
      d= b*c
      df = pd.DataFrame.from_dict(list_item)
      new_row = {'nama_item':a, 'jumlah_item' : b, 'harga_item':c, 'total_harga':d}
      df = df.append(new_row, ignore_index=True)
      list_item = df
  elif menu == 2:
    print("apa yang ingin diganti?")
    print("1. nama item 2.jumlah item 3.harga item 4.back")
    submenu1=int(input())
    if submenu1 == 1:
        a=input("masukan nama item yang ingin diganti ")
        b=input("masukan nama item barua5 ")
        list_item = list_item.replace([a], b)
    elif submenu1 == 2:
        a=int(input("masukan jumlah item yang ingin diganti "))
        b=int(input("masukan jumlah item baru "))
        list_item['jumlah_item'] = list_item['jumlah_item'].replace([a], b)

    elif submenu1 == 3:
        a=int(input("masukan harga item yang ingin diganti "))
        b=int(input("masukan harga item baru "))
        list_item['harga_item'] = list_item['harga_item'].replace([a], b)
    else:
        print("kata kunci salah, kembali ke menu utama")

  elif menu == 3:
    print(list_item)

  elif menu == 4:
    print("apa yang ingin dihapus?")
    print("1. per item 2. semua")
    submenu1=int(input())
    if submenu1 == 1:
      print("index berapa yang ingin dihapus?")
      a=int(input())
      list_item = list_item.drop(list_item.index[a])
    elif submenu1 == 2:
      list_item = list_item.iloc[0:0]
  elif menu == 5:
    Total = list_item['total_harga'].sum()
    print(f'total belanja anda sebesar:{Total}')
    if Total >= 200000 and Total<300000:
          diskon=Total*0.05
          Total=Total-diskon
          print(f'jumlah total belanjaan adalah {Total} dengan diskon 5%')
    elif Total >= 300000 and Total<500000:
          diskon=Total*0.08
          Total=Total-diskon
          print(f'jumlah total belanjaan adalah {Total} dengan diskon 8%')
    elif Total >= 500000:
          diskon=Total*0.1
          Total=Total-diskon
          print(f'jumlah total belanjaan adalah {Total} dengan diskon 101%')

  elif menu == 6:
    menu1 = 'n'
