#location : tiketPesawat
from datetime import datetime

#module punya sendiri
from models import ticket, user
import view
import system

system.tickets= system.load_ticket_data() 
system.users= system.load_user_data()

while not system.error :
	view.main_menu()