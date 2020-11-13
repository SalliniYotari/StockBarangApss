from os import system
from time import sleep

def print_menu():
	system("cls")
	print("""
	Penyimpanan Stock Spring Bed Sederhana
	[1]. Lihat Semua Barang
	[2]. Tambah Barang Baru
	[3]. Cari Barang
	[4]. Hapus Barang
	[5]. Update Barang
	[6]. Tentang Aplikasi
	[Q]. Keluar
		""")

def print_header(msg):
	system("cls")
	print(msg)

def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False

def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False

def print_data(stock=None, nama=True, ukuran=True, jumlah=True, harga=True, all_data=False):
	if stock != None and all_data == False:
		print(f"CODE : {stocks}")
		print(f"NAMA : {stocks[stock]['nama']}")
		print(f"UKURAN : {stocks[stock]['ukuran']}")
		print(f"JUMLAH : {stocks[stock]['jumlah']}")
		print(f"HARGA : {stocks[stock]['harga']}")
	elif jumlah == False and all_data == False:
		print(f"CODE : {stock}")
		print(f"NAMA : {stocks[stock]['nama']}")
	elif all_data == True:
		for every_stock in stocks: # lists, string,dict	
			code = stock #nama = key dari dict-nya
			nama = stocks[every_stock]['nama']
			ukuran = stocks[every_stock]['ukuran']
			jumlah = stocks[every_stock]['jumlah']
			harga = stocks[every_stock]['harga']
			print(f"CODE : {code} - NAMA : {nama} - UKURAN : {ukuran} - JUMLAH : {jumlah} - HARGA : {harga}")

def view_stocks():
	print_header("DAFTAR BARANG TERSIMPAN")
	if not_empty(stocks):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA Data TERSIMPAN")
	input("Tekan ENTER untuk kembali ke MENU")

def add_stock():
	print_header("MENAMBAHKAN BARANG BARU")
	code = input("CODE \t: ")
	nama = input("NAMA \t: ")
	ukuran = input("UKURAN \t: ")
	jumlah = input("JUMLAH \t: ")
	harga = input("HARGA \t: ")
	respon = input(f"Apakah yakin ingin menyimpan Data : {nama} / (Y/N) ")
	if verify_ans(respon):
		stocks[code] = {
			"nama" : nama, 
			"ukuran" : ukuran,
			"jumlah" : jumlah,
			"harga" : harga
		}
		print("Data Barang Tersimpan")
	else:
		print("Data Batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def searching(stock):
	if stock in stocks:
		return True
	else:
		return False

def find_stock():
	print_header("MENCARI STOCK BARANG")
	nama = input("Nama Barang yang Dicari : ")
	exists = searching(nama)
	if exists:
		print("Data Ditemukan")
		print_data(stock=nama)
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def check_user_input(char):
	char = char.upper()
	if char == "Q":
		print("BYE !!")
		return True
	elif char == "1":
		view_stocks()
	elif char == "2":
		add_stock()
	elif char == "3":
		find_stock()
	elif char == "4":
		pass
	elif char == "5":
		pass
	elif char == "6":
		pass

stocks = {
	"001" : {
		"nama" : "single size",
		"ukuran" : "90 cm x 200 cm",
		"jumlah" : "30",
		"harga" : "3.000.000"
	},
	"002" : {
		"nama" : "full size",
		"ukuran" : "120 cm x 200 cm",
		"jumlah" : "15",
		"harga" : "6.000.000"
	}
}

stop = False

while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)