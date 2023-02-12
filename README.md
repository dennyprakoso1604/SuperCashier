SUPER CASHIER
LATAR BELAKANG
Script  ini gunakan untuk membantu customer untuk melakukan self service di kasir supermarket. User dapat menambahkan, mengedit, menghapus item dari list. User juga dapat mengecek item yang ada dilist dan juga mengetahui berapa total harga dari item item yang ada di list
Requirement
•	Transaction ID
Per transaction User will generate Transaction ID
•	Add Item
User can add name item, amount item, and price per item to the list
•	Edit Item
User can edit specific Item without delete the item, which can be edited:
-	User can edit name item
-	User can edit amount item
-	User can edit price item
•	Remove Item
User can remove the item from the list with 2 choices:
-	User can remove specific item
-	User can remove all item at once
•	Check Order
User can check all the item in the cart/list that user has been input
-	User can check whether input file is correct or not
-	User can check list of all item in the cart
•	Total Price
This will be show the user the total amount of all item in the cart
User will got the discount:
-	More than 200.000 discount 5%
-	More than 300.000 discount 8%
-	More than 300.000 discount 10%

Flowchart/Flowcode
Flowchart dari code ini dapat dilihat dibawah:
 

Function/Attributes & hasil code
Create Transaction ID
class transaction:
  def __init__(self,transactionID):
    self.transactionID = transactionID

transaction_1 = transaction(1)
transaction_123 = f'TRX {transaction_1.transactionID}'
print(transaction_123)    
code tersebut ada lah code yang membuat kode transaksi dengan ditambahkan tulisan TRX pada code transaksinya
Create table
list_item = ({
    'nama_item':[],
    'jumlah_item' :[],
    'harga_item':[],
    'total_harga':[]
               })
Function berikut digunakan untuk membuat tabel yang akan di pakai dalam script ini
Add item
      a=input("masukan nama item ")
      b=int(input("masukan jumlah item "))
      c=int(input("masukan harga item "))
      d= b*c
      df = pd.DataFrame.from_dict(list_item)
      new_row = {'nama_item':a, 'jumlah_item' : b, 'harga_item':c, 'total_harga':d}
      df = df.append(new_row, ignore_index=True)
      list_item = df
function berikut digunakan untuk menambahkan item ke dalam list keranjang belanja
Hasil:
 

Edit item
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
berikut adalah code yang digunakan untuk mengubah nilai dari salah satu kolom/komponen yang ingin diganti dari barang dalam keranjang belanja
Hasil:
 
Melihat List item
print(list_item)
berikut adalah perintah untuk melihat list dari item yang ada dikeranjang
 
Menghapus Item
    print("apa yang ingin dihapus?")
    print("1. per item 2. semua")
    submenu1=int(input())
    if submenu1 == 1:
      print("index berapa yang ingin dihapus?")
      a=int(input())
      list_item = list_item.drop(list_item.index[a])
    elif submenu1 == 2:
      list_item = list_item.iloc[0:0]
code berikut adalah digunakan menghapus salah satu atau semua dari keranjang belanja
 
Total Harga
 Total = list_item['total_harga'].sum()
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

berikut adalah code dari total harga yang dimana mendapatkan diskon yang berbeda sesuai dengan requirement dari user
 

Conclusion
Script ini masih kurang dari sempurna, yang dimana masih ada hal yang terlewat dari requirement.
Hal yang terlewat adalah saat mengecek list keranjang ada notif seperti berikut:
 
Yang dimana requirement tersebut belum masuk ke dalam code. Karena waktu jadi tidak sempat untuk di recompile lagi mohon maaf yaa :D. Untuk secara keseluruhan, code ini sudah berjalan sebagaimana penulis tangkap dari segi requirementnya. Penulis berharap code ini dapat berguna untuk orang yang menggunakannya :D
