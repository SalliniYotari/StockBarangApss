from os import system
from json import dump, load
from datetime import datetime

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

def print_data(id_stock=None, ukuran=True, jumlah=True, harga=True, all_data=False):
	if id_stock != None and all_data == False:
		print(f"ID : {id_stock}")
		print(f"NAMA : {stocks[id_stock]['nama']}")
		print(f"UKURAN : {stocks[id_stock]['ukuran']}")
		print(f"JUMLAH : {stocks[id_stock]['jumlah']}")
		print(f"HARGA : {stocks[id_stock]['harga']}")
	elif jumlah == False and all_data == False:
		print(f"ID : {id_stock}")
		print(f"NAMA : {stocks[stock]['nama']}")
		print(f"UKURAN : {stocks[stock]['ukuran']}")
		print(f"HARGA : {stocks[stock]['harga']}")
	elif all_data == True:
		for id_stock in stocks: # lists, string,dict	
			nama = stocks[id_stock]["nama"] #nama = key dari dict-nya
			ukuran = stocks[id_stock]["ukuran"]
			jumlah = stocks[id_stock]["jumlah"]
			harga = stocks[id_stock]["harga"]
			print(f"ID : {id_stock} - NAMA : {nama} - UKURAN : {ukuran} - JUMLAH : {jumlah} - HARGA : {harga} ")

def view_stocks():
	print_header("DAFTAR STOCK BARANG TERSIMPAN")
	if not_empty(stocks):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA Data TERSIMPAN")
	input("Tekan ENTER untuk kembali ke MENU")

def create_id_stock(name):
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day

	counter = len(stocks) + 1
	first= name[0].upper()

	id_stock = ("%04d%02d%02d-Z%03d%s" % (tahun, bulan, hari, counter, first)) 
	return id_stock

def add_stock():
	print_header("MENAMBAHKAN STOCK BARANG BARU")
	nama = input("NAMA \t: ")
	ukuran = input("UKURAN \t: ")
	jumlah = input("JUMLAH \t: ")
	harga = input("HARGA \t: ")
	respon = input(f"Apakah yakin ingin menyimpan Data : {nama} / (Y/N) ")
	if verify_ans(respon):
		id_stock = create_id_stock(name=nama)
		stocks[id_stock] = {
			"nama" : nama,
			"ukuran" : ukuran,
			"jumlah" : jumlah,
			"harga" : harga
		}
		saved = save_data_stocks()
		if saved:
			print("Data Barang Tersimpan")
		else:
			print("kesalahan saat menyimpan")
	else:
		print("Data Batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")

def searching_by_name(stock):
	for id_stock in stocks:
		if stocks[id_stock]['nama'] == stock:
			return id_stock
	else:
		return False

def find_stock():
	print_header("MENCARI STOCK BARANG")
	nama = input("Nama Barang yang Dicari : ")
	exists = searching_by_name(nama)
	if exists:
		print("Data Ditemukan")
		id_stock=nama
		print_data(id_stock=exists)
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def delete_stock():
	print_header("MENGAHAPUS STOCK BARANG")
	nama = input("Nama Barang yang akan Dihapus : ")
	exists = searching_by_name(nama)
	if exists:
		print_data(id_stock=exists)
		respon = input(f"Yakin ingin menghapus {nama} ? (Y/N) ")
		if verify_ans(respon):
			del stocks[exists]
			saved = save_data_stocks()
			if saved:
				print("Data Barang Telah Dihapus")
			else:
				print("kesalahan saat menyimpan")
		else:
			print("Data Barang Batal Dihapus")
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def update_stock_nama(id_stock):
	print(f"Nama Lama : {stocks[id_stock]['nama']}")
	new_name = input("Masukan Nama Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		stocks[id_stock]['nama'] = new_name
		print("Data Telah di simpan")
		print_data(id_stock)
	else:
		print("Data Batal diubah")

def update_stock_ukuran(id_stock):
	print(f"Ukuran Lama : {stocks[id_stock]['ukuran']}")
	new_ukuran = input("Masukan Ukuran Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		stocks[id_stock]['ukuran'] = new_ukuran
		print("Data Telah di simpan")
		print_data(id_stock)
	else:
		print("Data Batal diubah")

def update_stock_jumlah(id_stock):
	print(f"Jumlah Lama : {stocks[stock]['jumlah']}")
	new_jumlah = input("Masukan Jumlah Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		stocks[stock]['jumlah'] = new_jumlah
		print("Data Telah di simpan")
		print_data(id_stock)
	else:
		print("Data Batal diubah")

def update_stock_harga(id_stock):
	print(f"Harga Lama : {stocks[stock]['harga']}")
	new_harga = input("Masukan Harga Baru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		stocks[stock]['harga'] = new_harga
		print("Data Telah di simpan")
		print_data(id_stock)
	else:
		print("Data Batal diubah")

def update_stock():
	print_header("MENGUPDATE STOCK INFO BARANG")
	nama = input("Nama Barang yang akan di-update : ")
	exists = searching_by_name(nama)
	if exists:
		print_data(exists)
		print("EDIT FIELD [1] NAMA - [2] UKURAN - [3] JUMLAH - [4] HARGA")
		respon = input("MASUKKAN PILIHAN (1/2/3/4) : ")
		if respon == "1":
			update_stock_nama(exists)
		elif respon == "2":
			update_stock_ukuran(exists)
		elif respon == "3":
			update_stock_jumlah(exists)
		elif respon == "4":
			update_stock_harga(exists)
		saved = save_data_stocks()
		if saved:
			print("Data Barang Telah di-update.")
		else:
			print("Kesalahan saat menyimpan")
			
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")

def about_apps():
	print_header("TENTANG APP STOCK BARANG")
	print("THIS App Made By SALLINI YOTARI 10 IPA Komp 2")
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
		delete_stock()
	elif char == "5":
		update_stock()
	elif char == "6":
		about_apps()

def load_data_stocks():
	with open(file_path, 'r') as file:
		data = load(file)
	return data

def save_data_stocks():
	with open(file_path, 'w') as file:
		dump(stocks, file)
	return True

stop = False
file_path = "stocks.json"
stocks = load_data_stocks()
while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)