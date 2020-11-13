from json import load, dump

def load_ticket_data():
	with open(ticket_table_path, "r") as ticketFile:
		data = load(ticketFile)
	return data

def load_user_data():
	with open(user_table_path, "r") as userFile:
		data = load(userFile)
	return data

error = False
ticket_table_path = "data/ticket_table.json"
user_table_path = "data/user_table.json"

tickets = {}
users = {}

###LIBRARY STRING

main_menu = """
APLIKASI TIKET PESAWAT AGENSI LUAR BIASA

[1] Pesan/Booking Tiket Pesawat
[2] Cari Tiket Pesawat
[3] Edit Tiket Pesawat
[4] Batalkan/Hapus Tiket Pesawat
[5] Cetak PDF Tiket Pesawat
[6] Cetak QR Tiket Pesawat
[7] Tentang Aplikasi
"""