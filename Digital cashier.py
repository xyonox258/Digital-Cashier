import json,time,math,os,sys,shutil,platform
from cryptography.fernet import Fernet,InvalidToken
from datetime import date,timedelta,datetime
from fpdf import FPDF
from pathlib import Path
def check_terminal():
	if platform.system() != "Windows":
		return
	if "WT_SESSION" not in os.environ and not shutil.which("wt.exe"):
			print("\n" + "="*70)
			print("[!] ERROR: 'Windows Terminal' is required to run this software.")
			print("="*70)
			print("\n* If you do not have Windows Terminal installed:")
			print(" Please download and install 'Windows Terminal' from the Microsoft Store.")
			print("* If you already have Windows Terminal installed:")
			print(" Please set it as your 'Default Terminal Emulator' in Windows Settings,")
			print(" or open Windows Terminal and run this application inside it.")
			print("\n"+"="*70)
			input("\nPress Enter to exit...")
			sys.exit(0)
check_terminal()			
if sys.platform == "win32":
	try:
		import ctypes
		hwnd = ctypes.windll.kernel32.GetConsoleWindow()
		if hwnd:
			ctypes.windll.user32.ShowWindow(hwnd,3)
			h_stdout = ctypes.windll.kernel32.GetStdHandle(-11)
			cord = ctypes.windll.kernel32.GetLargestConsoleWindowSize(h_stdout)
			if cord.X > 0 and cord.Y > 0:
				os.system(f'mode con: cols={cord.X} lines={cord.Y}')
	except Exception:
		pass
	try:
		import pyautogui
		time.sleep(0.2)
		pyautogui.hotkey('alt', 'space')
		time.sleep(0.1)
		pyautogui.press('X')
	except Exception:
		pass
time.sleep(0.2)
w = os.get_terminal_size().columns
width = int(w * 0.99)
if not os.path.exists("Database.txt") or not os.path.exists("Dck.key") or not os.path.exists("main_database.txt"):
	print("="*width)
	head = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
	print(head.center(width))
	shead = "XyonixTech"
	print(shead.center(width))
	print("="*width)
	print("\033[31mSOME IMPORTANT FILES MAY BE MISSING OR CORRUPTED WE ARE UNABLE TO OPEN THE SOFTWARE\033[0m".center(width))
	print("   Press any Key for exit: ")
	n = input()
	sys.exit()
with open("Dck.key","rb")as file:
	key = file.read()
fernet = Fernet(key)
def clear_screen():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')		
def Register():
	clear_screen()
	n = 0
	while n<1:
		print("*"*width)
		title = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
		print(title.center(width))
		stitle = "Registration - Panel"
		print(stitle.center(width))
		print("*"*width)
		print("")
		print("            \U0001F6E1  Your Trusted Software.                                       ")
		print("           \U0001F4DD Provide Some Details for Register Yourself.                    ")
		print("_"*width)
		print("")
		notice ="\u26A0\uFE0F IMPORTANT NOTICE"
		print(notice.center(width))
		imp = "The Recovery Pin is essential so do not Forget it."
		print(imp.center(width))
		print("_"*width)
		print("")
		step ="**Steps for Registration**"
		print(step.center(width))
		print("")
		print("    1. Enter Your Full Name: ")
		print("    2. Enter Your Age: ")
		print("    3. Enter Your New User Id: ")
		print("    4. Enter Your New Password: ")
		print("")
		print("     **For Recover Your Account in Future Please Provide This Details Properly**     ")
		print("")
		print("    5. Enter Your Pet Name: ")
		print("    6. Enter Your Childhood Friend Name: ")
		print("    7. Enter Your Recovery Pin: ")
		print("")
		print("_"*width)
		print("="*width)
		print("     Press 1 for Go Back to Main Menu and Press Any Other Key for Exit and 0 for Proceed")
		print("="*width)
		h = input(" Please Select Your Option-> ")
		if h == '0':
			if os.path.getsize("Database.txt") == 0:
				flag = 0
			else:
				with open("Database.txt","rb")as file:
					d_encrypted = file.read()
					d_decrypt = fernet.decrypt(d_encrypted)
					d_string = d_decrypt.decode()
					d = json.loads(d_string)
					flag = 1
			print("")
			name=input("         \U0001F4DB Name: ")
			name = name.upper()
			z = 0
			while z != 2:
				try:
					age=int(input("         \U0001F382 Age: "))
					if age > 0:
						z = 2
					else:
						print("")
						print("_"*width)
						print("           \U0001F6A8 \033[31mPlease Enter Your Age in Positive Numbers\033[0m        ")
						print("_"*width)
				except ValueError:
					print("")
					print("_"*width)
					print("           \U0001F6A8 \033[31mPlease Enter Your Age in Numbers\033[0m        ")
					print("_"*width)
			if flag == 0:
				uid=input("         \U0001F464 User Id: ")
			else:
				while True:
					check = False
					uid_p=input("         \U0001F464 User Id: ")
					index = 0
					while index<len(d):
						if d[index]["uid"] == uid_p:
							time.sleep(1)
							print("")
							print("_"*width)
							print("           \U0001F6A8 \033[31mThis User Id is Taken Try Another!\033[0m        ")
							print("_"*width)
							check = True
						index = index + 1
					if check == True:
						continue
					else:
						uid = uid_p
						break 
			pw=input("         \U0001F511 Password: ")
			pet=input("         \U0001F43E Pet Name: ")
			friend=input("         \U0001F91D Childhood Friend Name: ")
			pet = pet.lower()
			friend = friend.lower()
			if flag == 0:
				rpin=input("         \U0001F504 Recovery PIN: ")
			else:
				while True:
					check1 = False
					rpin_p = input("         \U0001F504 Recovery PIN: ")
					index1 = 0
					while index1<len(d):
						if d[index1]["recover_pin"] == rpin_p:
							time.sleep(1)
							print("")
							print("_"*width)
							print("         \U0001F6A8 \033[31mThis Recovery Pin is Taken Try Another!\033[0m   ")
							print("_"*width)
							check1 = True
						index1 = index1 + 1
					if check1 == True:
						continue
					else:
						rpin = rpin_p
						break
			user_details = {"name":name,"age":age,"uid":uid,"pwd":pw,"pet":pet,"friend":friend,"recover_pin":rpin}
			try:
				with open("Database.txt","rb")as file:
					data_list_encrypted = file.read()
					data_list_decrypt = fernet.decrypt(data_list_encrypted)
					data_list_string = data_list_decrypt.decode()
					data_list = json.loads(data_list_string)
			except (FileNotFoundError,InvalidToken):
				data_list = []
			data_list.append(user_details)
			data_list_string = json.dumps(data_list)
			data_list_encrypted = fernet.encrypt(data_list_string.encode())
			with open("Database.txt","wb")as file:
				file.write(data_list_encrypted)
			print("      \u23F3 Wait for a While...  ")
			time.sleep(3)
			print("")
			print("_"*width)
			sy = "\U0001F6A8 \033[32m**Your Account was Created Sucessfully**\033[0m"
			print(sy.center(width))
			print("_"*width)
			time.sleep(2)
			return 1
		elif h == '1':
			return 6
			break
		else:
			sys.exit()
		n = n + 1
def Login():
	n = 0
	while n<1:
		clear_screen()
		print("="*width)
		title = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
		print(title.center(width))
		lp = "Login - Panel"
		print(lp.center(width))
		print("="*width)
		print("")
		notice = "\u26A0\uFE0F IMPORTANT NOTICE"
		print(notice.center(width))
		n1 = "1.\U0001F512  Registered Users Only: Unauthorized Access is Strictly Prohibited."
		print(n1.center(width))
		n2 = "2.\U0001F520  Case Sensitive: User Id is Strictly Case Sensitive type Carefully."
		n3 =  "3. \U0001F310  100% Offline: Data is Only on this PC."
		n4 = "4. \U0001F4BE  Backup: No Online Backup is Available."
		n5 = "5. \U0001F6A8  Loss Risk: Logging in elsewhere will not Recover Your Data"
		n6 = "6. \U0001F4A1  This System is Currency-Nutral. Treat Figures as Your Preferred Currency"
		print(n2.center(width))
		print(n3.center(width))
		print(n4.center(width))
		print(n5.center(width))
		print(n6.center(width))
		print("_"*width)
		print("")
		st = "**Steps for Login**"
		print(st.center(width))
		print("")
		print("        1. Enter Your User Id                                                        ")
		print("        2. Enter Your Password                                                       ")
		print("_"*width)
		print("="*width)
		print("    Press 1 for Go Back to Main Menu and Press Any Other Key for Exit and 0 for Proceed")
		print("="*width)
		h = input("   Please Select Your Option-> ")
		if h == '0':
			user_id = input("     \U0001F464 User Id: ")
			Password = input("    \U0001F511 Password: ")
			try:
				with open("Database.txt","rb")as file:
					l_encrypted = file.read()
					l_decrypt = fernet.decrypt(l_encrypted)
					l_string = l_decrypt.decode()
					l = json.loads(l_string)
				i = 0
				while i<len(l):
					if user_id == l[i]["uid"] and Password == l[i]["pwd"]:
						return 0,user_id
					i = i+1
				return None,user_id
			except(FileNotFoundError,InvalidToken):
				print("_"*width)
				dt = "\U0001F6A8 \033[31mWe are not Found any User Details Register First!\033[0m"
				print(dt.center(width))
				print("_"*width)
				return 1,user_id
				time.sleep(2)
		elif h == '1':
			return 5,None 
			break
		else:
			sys.exit()
		n = n + 1
def forget():
	clear_screen()
	print("="*width)
	title = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
	print(title.center(width))
	stitle = "User Id and Password Recovery - Panel"
	print(stitle.center(width))
	print("="*width)
	print("_"*width)
	print("")
	steps = "**Steps for Recovery**"
	print(steps.center(width))
	print("")
	print("      1. Enter Your Registered Pet Name: ")
	print("      2. Enter Your Registered Childhood riend Name: ")
	print("      3. Enter Your Registered Recovery PIN: ")
	print("      4. Re-Generate User Id: ")
	print("      5. Re-Generate Password: ")
	print("")
	print("="*width)
	print("  Press 1 for Go Back to Main Menu and Press Any Other Key for Exit and 0 for Proceed")
	print("="*width)
	h = input("   Please Select Your Option-> ")
	if h == '0':
		time.sleep(1)
		pet=input("     \U0001F43E Pet Name: ")
		friend=input("     \U0001F91D Childhood Friend Name: ")
		pet = pet.lower()
		friend = friend.lower()
		rl=input("     \U0001F504 Recovery PIN: ")
		with open("Database.txt","rb")as file:
			l_encrypted = file.read()
			l_decrypt = fernet.decrypt(l_encrypted)
			l_string = l_decrypt.decode()
			l = json.loads(l_string)
		i,flag = 0,False 
		while i<len(l):
			if pet == l[i]["pet"] and friend == l[i]["friend"] and l[i]["recover_pin"] == rl:
				past_user_id = l[i]["uid"]
				time.sleep(1)
				dx = 1
				while dx != 0:
					check = False
					uid_p=input("     \U0001F464 New User Id:   ")
					index = 0
					while index<len(l):
						if l[index]["uid"] == uid_p:
							time.sleep(1)
							print("")
							print("_"*width)
							print("         \U0001F6A8 \033[31mThis User Id is Taken Try Another!\033[0m        ")
							print("_"*width)
							check = True
						index = index + 1
					if check == True:
						continue 
					else:
						user_id=uid_p
						dx = 0
						break
				password = input("   \U0001F511 New Password: ")
				l[i]["uid"] = user_id
				l[i]["pwd"] = password
				if os.path.getsize("main_database.txt") != 0:
					with open("main_database.txt","rb")as file:
						main_list_encrypt = file.read()
						main_list_decrypt = fernet.decrypt(main_list_encrypt)
						main_list = json.loads(main_list_decrypt.decode())
					ig = 0
					check = False
					while ig < len(main_list):
						if main_list[ig]["uid"] == past_user_id:
							target = ig
							check = True 
						ig = ig + 1
					if check == True:
						main_list[target]["uid"] = uid_p
						with open("main_database.txt","wb")as file:
							main_list_string = json.dumps(main_list)
							main_list_encrypt = fernet.encrypt(main_list_string.encode())
							file.write(main_list_encrypt)
				with open("Database.txt","wb")as file:
					v = l
					v_string = json.dumps(v)
					v_encrypted=fernet.encrypt(v_string.encode())
					file.write(v_encrypted)
				flag = True 
			i = i + 1
		if flag == True:
			print("    \u23F3 Wait for a While...  ")
			time.sleep(3)
			print("")
			print("_"*width)
			sd = "\033[32mYour User Id and Password have been Updated Sucessfully:\033[0m "
			print(sd.center(width))
			print("_"*width)
			return True 
		else:
			print("*"*width)
			cx = "\033[31mProvided DETAILS do not matched with our Record\033[0m"
			cx1 = "\033[31mWe are Unable to Update User Id and Password\033[0m "
			print(cx.center(width))
			print(cx1.center(width))
			print("*"*width)
			return False
	elif h == '1':
		return 5
	else:
		sys.exit()
def main(user_id):
	with open("Database.txt","rb") as file:
		l_encrypt = file.read()
		l_decrypt = fernet.decrypt(l_encrypt)
		l_string = l_decrypt.decode()
		l = json.loads(l_string)
	if os.path.getsize("main_database.txt") != 0:
		with open("main_database.txt","rb") as file:
			main_list_encrypt = file.read()
			main_list_decrypt = fernet.decrypt(main_list_encrypt)
			main_list_string = main_list_decrypt.decode()
			main_list = json.loads(main_list_string)
		f = 0
		te = 0.0
		tex = 0.0
		er = 0
		ct = "N/A"
		y_ex = 0
		fg = False
		t_list = []
		list(t_list)
		while f< len(main_list):
			if main_list[f]["uid"] == user_id:
				fg = True
				target = f
			f = f + 1
		if fg == True:
			vb = 0
			while vb < len(main_list[target]["details"]):
				if main_list[target]["details"][vb]["Date"]["year"] == date.today().year and main_list[target]["details"][vb]["Date"]["month"] == date.today().month and main_list[target]["details"][vb]["Date"]["day"] == date.today().day:
					ln = 0
					t_list = []
					list(t_list)
					while ln < len(main_list[target]["details"][vb]["expense"]):
						m = main_list[target]["details"][vb]["expense"][ln]["amount"]
						t_list.append(m)
						te = te + m
						ln = ln + 1
				lg = 0
				yesterday = date.today() - timedelta(days=1)
				if main_list[target]["details"][vb]["Date"]["year"] == yesterday.year  and main_list[target]["details"][vb]["Date"]["month"] == yesterday.month and main_list[target]["details"][vb]["Date"]["day"] == yesterday.day:
					while lg < len(main_list[target]["details"][vb]["expense"]):
						x = main_list[target]["details"][vb]["expense"][lg]["amount"]
						y_ex = y_ex + x
						lg = lg + 1
				vb = vb + 1
			if te > 0:
				max_amt = max(t_list)
			else:
				max_amt=0
			vc = 0
			while vc < len(main_list[target]["details"]):
				if main_list[target]["details"][vc]["Date"]["year"] == date.today().year and main_list[target]["details"][vc]["Date"]["month"] == date.today().month and main_list[target]["details"][vc]["Date"]["day"] == date.today().day:
					lm = 0
					while lm < len(main_list[target]["details"][vc]["expense"]):
						if main_list[target]["details"][vc]["expense"][lm]["amount"] == max_amt:
							ct = main_list[target]["details"][vc]["expense"][lm]["category"]
							if ct == '1':
								ct = "Market"
							elif ct == '2':
								ct = "Food"
							elif ct == '3':
								ct = "Travel"
							elif ct == '4':
								ct = "Others"
						lm = lm + 1
				vc = vc + 1
			vk = 0
			while vk < len(main_list[target]["details"]):
				vd = 0
				teb = 0.0
				if main_list[target]["details"][vk]["Date"]["month"] == date.today().month:
					while vd < len(main_list[target]["details"][vk]["expense"]):
						b = main_list[target]["details"][vk]["expense"][vd]["amount"]
						teb = teb + b
						er = er + 1
						vd = vd + 1
					tex = tex + teb
				vk = vk + 1
	else:
		te = 0.0
		tex = 0.0
		ct = "N/A"
		er = 0
		y_ex = 0
	i = 0
	while i < len(l):
		if l[i]["uid"] == user_id:
			u = i
		i = i + 1
	print("="*width)
	print("")
	title = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
	print(title.center(width))
	stitle ="\U0001F4D4  - Your Daily Personal Diary - \U0001F4D4"
	print(stitle.center(width))
	fc = "Main-Dashboard"
	print("")
	print(fc.center(width))
	com = "[ v1.0.0 | \U0001F6E1  Powered by XyonixTech ]"
	print(com.center(width))
	print("="*width)
	if len(l[u]["name"]) > 8:
		name = l[u]["name"][:8]+".."
	else:
		name = l[u]["name"]
	nm = "USER -"+name
	Date = date.today()
	date_string = str(Date)
	d = "| "+"Date - " + date_string
	print(f"\U0001F464 {nm} |",end="")
	print(d,end="")
	check_te = str(int(te))
	check_tex = str(int(tex))
	if len(check_te) >= 6:
		te_r = te
		if te > 1000000000000:
			te = (te/1000000000000)
			te_n = f"{te:.2f}T"
		elif te > 1000000000:
			te = (te/1000000000)
			te_n = f"{te:.2f}B"
		elif te > 1000000:
			te = (te/1000000)
			te_n = f"{te:.2f}M"
		elif te > 1000:
			te = (te/1000)
			te_n = f"{te:.2f}K"
	else:
		te_r = te
		te_n = f"{te:.2f}"
	if len(check_tex) >= 6:
		tex_r = tex
		if tex > 1000000000000:
			tex = (tex/1000000000000)
			tex_n = f"{tex:.2f}T"
		elif tex > 1000000000:
			tex = (tex/1000000000)
			tex_n = f"{tex:.2f}B"
		elif tex > 1000000:
			tex = (tex/1000000)
			tex_n = f"{tex:.2f}M"
		elif tex > 1000:
			tex = (tex/1000)
			tex_n = f"{tex:.2f}K"
	else:
		tex_r = tex
		tex_n = f"{tex:.2f}"
	print(f"  ||  This Month Total Expense: {tex_n}",end="")
	print("  ||  Most Expensive Category: ",ct,end="")
	print(f"  ||  Today's Total Expense: {te_n}")
	print("-"*width)
	print("")
	print("--------------------------\U0001F4A1 Quick Insights \U0001F4A1--------------------------".center(width))
	print("")
	if tex_r > 0:
		bs = float((te_r/tex_r)*100)
	else:
		bs = 0
	check_y_ex = str(int(y_ex))
	if len(check_y_ex) >= 6:
		y_ex_r = y_ex
		if y_ex > 1000000000000:
			y_ex = (y_ex/1000000000000)
			y_ex_n = f"{y_ex:.2f}T"
		elif y_ex > 1000000000:
			y_ex = (y_ex/1000000000)
			y_ex_n = f"{y_ex:.2f}B"
		elif y_ex > 1000000:
			y_ex = (y_ex/1000000)
			y_ex_n = f"{y_ex:.2f}M"
		elif y_ex > 1000:
			y_ex = (y_ex/1000)
			y_ex_n = f"{y_ex:.2f}K"
	else:
		y_ex_r = y_ex
		y_ex_n = f"{y_ex:.2f}"
	check_er = str(er)
	if len(check_er) >= 9:
		er_r = er
		if er > 1000000000000:
			er = (er/1000000000000)
			er_n = f"{er:.0f}T"
		elif er > 1000000000:
			er = (er/1000000000)
			er_n = f"{er:.0f}B"
		elif er > 1000000:
			er = (er/1000000)
			er_n = f"{er:.0f}M"
		elif er > 1000:
			er = (er/1000)
			er_n = f"{er:.0f}K"
	else:
		er_r = er
		er_n = f"{er:.0f}"
	print(f"\t\U0001F4CA Month's Share: {bs:.2f}%  ||",end="  ")
	print(f"\U0001F5D2 Total Entry Records: {er_n} ||",end="  ")
	print(f"\u23F3 Yesterday's Expense: {y_ex_n}","  ||",end="  ")
	if y_ex != 0:
		e_tr = int((te_r - y_ex_r))
		if e_tr > 0:
			e_tr_icon = "\u25b2 Higher(+"
		elif e_tr < 0:
			e_tr_icon = "\u25bc Lower("
		elif e_tr == 0:
			e_tr_icon = "\u25a0 Stable("
		check_e_tr = str(e_tr)
		if len(check_e_tr) >= 8:
			e_tr_r = e_tr
			if e_tr > 1000000000000 or e_tr < -1000000000000:
				e_tr = (e_tr/1000000000000)
				e_tr_n = f"{e_tr:.2f}T"
			elif e_tr > 1000000000 or e_tr < -1000000000:
				e_tr = (e_tr/1000000000)
				e_tr_n = f"{e_tr:.2f}B"
			elif e_tr > 1000000 or e_tr < -1000000:
				e_tr = (e_tr/1000000)
				e_tr_n = f"{e_tr:.2f}M"
			elif e_tr > 1000 or e_tr < -1000:
				e_tr = (e_tr/1000)
				e_tr_n = f"{e_tr:.2f}K"
		else:
			e_tr_r = e_tr
			e_tr_n = f"{e_tr:.2f}"
	else:
		e_tr_n = "N/A"
		e_tr_icon = "("
	print(f"\U0001F4C8 Expense Trend: {e_tr_icon}{e_tr_n})")
	print("")
	print("_"*width)
	print("")
	print("--------------------------\u2699\uFE0F Operations \u2699\uFE0F--------------------------".center(width))
	print("")
	print("\t\t1. Add Today's Expense Records: ",end="\n\n")
	print("\t\t2. Analyze Today's Expense Records: ",end="\n\n")
	print("\t\t3. Search Records: ",end="\n\n")
	print("\t\t4. Profile Settings: ",end="\n\n")
	print("\t\t5. Log Out: ",end="\n\n")
	print("\t\t6. Report Generation(PDF): ",end="\n\n")
	print("\t\t7. Help: ")
	print("")
	print("_"*width)
	print("")
	print("Please Select Your Option(1-7):-> ")
	print("_"*width)
	h=input()
	if h == '1':
		add_exp(user_id)
	elif h == '3':
		search(user_id)
	elif h == '2':
		analyze(user_id)
	elif h == '4':
		settings(user_id)
	elif h == '6':
		report(user_id)
	elif h == '7':
		help(user_id)
	elif h != '1' and h!= '2' and h!= '3' and h!= '4' and h!='5' and h!='6' and h!='7':
		time.sleep(1)
		print("      \U0001F6A8 \033[31mYour Input is Wrong try again!\033[0m")
		print("")
		print("_"*width)
		print("")
		print("      1. Try Again: ")
		print("     **Press any Other Key for Log Out: ")
		print("_"*width)
		print("    Please Select Your Option: ")
		v = input()
		if v == '1':
			clear_screen()
			main(user_id)
def add_exp(user_id):
	clear_screen()
	with open("Database.txt","rb") as file:
		l_encrypt = file.read()
		l_decrypt = fernet.decrypt(l_encrypt)
		l_string = l_decrypt.decode()
		l = json.loads(l_string)
	if os.path.getsize("main_database.txt") != 0:
		with open("main_database.txt","rb") as file:
			main_list_encrypt = file.read()
			main_list_decrypt = fernet.decrypt(main_list_encrypt)
			main_list_string = main_list_decrypt.decode()
			main_list = json.loads(main_list_string)
		f = 0
		te = 0.0
		tex = 0.0
		ct = "N/A"
		fg = False
		t_list = []
		list(t_list)
		while f< len(main_list):
			if main_list[f]["uid"] == user_id:
				fg = True
				target = f
			f = f + 1
		if fg == True:
			vb = 0
			while vb < len(main_list[target]["details"]):
				if main_list[target]["details"][vb]["Date"]["year"] == date.today().year and main_list[target]["details"][vb]["Date"]["month"] == date.today().month and main_list[target]["details"][vb]["Date"]["day"] == date.today().day:
					ln = 0
					t_list = []
					list(t_list)
					while ln < len(main_list[target]["details"][vb]["expense"]):
						m = main_list[target]["details"][vb]["expense"][ln]["amount"]
						t_list.append(m)
						te = te + m
						ln = ln + 1
				vb = vb + 1
			if te > 0:
				max_amt = max(t_list)
			else:
				max_amt = 0
			vc = 0
			while vc < len(main_list[target]["details"]):
				if main_list[target]["details"][vc]["Date"]["year"] == date.today().year and main_list[target]["details"][vc]["Date"]["month"] == date.today().month and main_list[target]["details"][vc]["Date"]["day"] == date.today().day:
					lm = 0
					while lm < len(main_list[target]["details"][vc]["expense"]):
						if main_list[target]["details"][vc]["expense"][lm]["amount"] == max_amt:
							ct = main_list[target]["details"][vc]["expense"][lm]["category"]
							if ct == '1':
								ct = "Market"
							elif ct == '2':
								ct = "Food"
							elif ct == '3':
								ct = "Travel"
							elif ct == '4':
								ct = "Others"
						lm = lm + 1
				vc = vc + 1
			vk = 0
			while vk < len(main_list[target]["details"]):
				vd = 0
				teb = 0.0
				if main_list[target]["details"][vk]["Date"]["month"] == date.today().month:
					while vd < len(main_list[target]["details"][vk]["expense"]):
						b = main_list[target]["details"][vk]["expense"][vd]["amount"]
						teb = teb + b
						vd = vd + 1
					tex = tex + teb
				vk = vk + 1
	else:
		te = 0.0
		tex = 0.0
		ct = "N/A"
	i = 0
	while i < len(l):
		if l[i]["uid"] == user_id:
			u = i
		i = i + 1
	print("="*width)
	print("")
	title = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
	print(title.center(width))
	stitle ="\U0001F4D4  - Your Daily Personal Diary - \U0001F4D4"
	print(stitle.center(width))
	fc = "Main-Dashboard-Add-Expense-Panel"
	print("")
	print(fc.center(width))
	com = "[ v1.0.0 | \U0001F6E1  Powered by XyonixTech ]"
	print(com.center(width))
	print("="*width)
	if len(l[u]["name"]) > 8:
		name = l[u]["name"][:8]+".."
	else:
		name = l[u]["name"]
	nm = "USER -"+name
	Date = date.today()
	date_string = str(Date)
	d = "| "+"Date - " + date_string
	print(f"\U0001F464 {nm} |",end="")
	print(d,end="")
	check_te = str(int(te))
	check_tex = str(int(tex))
	if len(check_te) >= 6:
		te_r = te
		if te > 1000000000000:
			te = (te/1000000000000)
			te_n = f"{te:.2f}T"
		elif te > 1000000000:
			te = (te/1000000000)
			te_n = f"{te:.2f}B"
		elif te > 1000000:
			te = (te/1000000)
			te_n = f"{te:.2f}M"
		elif te > 1000:
			te = (te/1000)
			te_n = f"{te:.2f}K"
	else:
		te_r = te
		te_n = f"{te:.2f}"
	if len(check_tex) >= 6:
		tex_r = tex
		if tex > 1000000000000:
			tex = (tex/1000000000000)
			tex_n = f"{tex:.2f}T"
		elif tex > 1000000000:
			tex = (tex/1000000000)
			tex_n = f"{tex:.2f}B"
		elif tex > 1000000:
			tex = (tex/1000000)
			tex_n = f"{tex:.2f}M"
		elif tex > 1000:
			tex = (tex/1000)
			tex_n = f"{tex:.2f}K"
	else:
		tex_r = tex
		tex_n = f"{tex:.2f}"
	print(f"  ||  This Month Total Expense: {tex_n}",end="")
	print("  ||  Most Expensive Category: ",ct,end="")
	print(f"  ||  Today's Total Expense: {te_n}")
	print("-"*width)
	print("")
	print("**Add Today's all Expenses**".center(width))
	print("_"*width)
	print("")
	print("***Steps for Add Expenses***".center(width))
	print("")
	print("\t\t1. Choose the Category of the Expense: ")
	print("\t\t2. Enter the Amount of the Expense: ")
	print("\t\t3. Enter the Purpose of the Expense: ")
	print("")
	print("_"*width)
	print("")
	print("Press 1 for Back to Main-Dashboard 2 for Log out 0 for Proceed and Any other Key for Exit: ")
	print("_"*width)
	s=input()
	if s == '0':
		clear_screen()
		print("="*width)
		print("")
		print(title.center(width))
		print(stitle.center(width))
		print("")
		print(fc.center(width))
		print(com.center(width))
		print("="*width)
		print(f"\U0001F464 {nm} |",end="")
		print(d,end="")
		print(f"  ||  This Month Total Expense: {tex_n}",end="")
		print("  ||  Most Expensive Category: ",ct,end="")
		print(f"  ||  Today's Total Expense: {te_n}")
		print("-"*width)
		print("")
		print("**Add Today's all Expenses**".center(width))
		print("_"*width)
		print("")
		print("-"*width)
		while True:
			print("**Category**".center(width))
			print("")
			print("\t\t1. \U0001f6d2 Market: ")
			print("\t\t2. \U0001f354 Food: ")
			print("\t\t3. \U0001f68b Travel: ")
			print("\t\t4. \u2699\ufe0f Others: ")
			print("-"*width)
			print("Choose Your Category(1-4): ")
			print("-"*width)
			cat = input()
			if cat == '1' or cat == '2' or cat == '3' or cat == '4':
				break
			else:
				print("")
				print("_"*width)
				print("         \U0001F6A8 \033[31mPress 1 to 4 Only!\033[0m        ")
				print("_"*width)
		while True:
			try:
				amt = float(input("\t\t \U0001f4b0 Enter the Amount of Expense: "))
				if amt > 0:
					break
				else:
					print("")
					print("_"*width)
					print("         \U0001F6A8 \033[31mWrong Input Enter Only Positive Numbers!\033[0m        ")
					print("_"*width)
			except ValueError:
				print("")
				print("_"*width)
				print("         \U0001F6A8 \033[31mWrong Input Enter Only Positive Numbers!\033[0m        ")
				print("_"*width)
		pur = input("\t\t \U0001f4ac Enter the Purpose of the Expense: ")
		year = date.today().year
		month = date.today().month
		day =  date.today().day
		if os.path.getsize("main_database.txt") == 0:
			date1 = {"year":year,"month":month,"day":day}
			exp_dic = {"amount":amt,"purpose":pur,"category":cat}
			exp_list = [exp_dic]
			dtl_dic = {"Date":date1,"expense":exp_list}
			dtl_list = [dtl_dic]
			main_dic = {"uid":user_id,"details":dtl_list}
			main_list = [main_dic]
			main_string = json.dumps(main_list)
			main_list_encrypt = fernet.encrypt(main_string.encode())
			with open("main_database.txt","wb") as file:
				file.write(main_list_encrypt)
		else:
			with open("main_database.txt","rb")as file:
				main_list_encrypt = file.read()
				main_list_decrypt = fernet.decrypt(main_list_encrypt)
				main_list_string = main_list_decrypt.decode()
				main_list = json.loads(main_list_string)
				iv = 0
				check = False
				cd = False
				mv = False
				while check != True: 
					while iv < len(main_list):
						if main_list[iv]["uid"] == user_id:
							target = iv
							check = True
						iv = iv + 1
					if check == False:
						cd = True
						date1 = {"year":year,"month":month,"day":day}
						exp_dic = {"amount":amt,"purpose":pur,"category":cat}
						exp_list = [exp_dic]
						dtl_dic = {"Date":date1,"expense":exp_list}
						dtl_list = [dtl_dic]
						main_dic = {"uid":user_id,"details":dtl_list}
						main_list.append(main_dic)
				it = 0
				while it < len(main_list[target]["details"]):
					if check == True and main_list[target]["details"][it]["Date"]["year"] == date.today().year and main_list[target]["details"][it]["Date"]["month"] == date.today().month and main_list[target]["details"][it]["Date"]["day"] == date.today().day:
						target1 = it
						flag = 2
					elif check == True:
						flag = 1
					it = it + 1
				if flag == 1:
					date1 = {"year":year,"month":month,"day":day}
					exp_dic = {"amount":amt,"purpose":pur,"category":cat}
					exp_list = [exp_dic]
					dtl_dic = {"Date":date1,"expense":exp_list}
					main_list[target]["details"].append(dtl_dic)
				elif flag == 2 and cd == False:
					exp_dic = {"amount":amt,"purpose":pur,"category":cat}
					main_list[target]["details"][target1]["expense"].append(exp_dic)
				main_list_string = json.dumps(main_list)
				main_list_encrypt = fernet.encrypt(main_list_string.encode())
				with open("main_database.txt","wb")as file:
					file.write(main_list_encrypt)
		print("   \t\t\u23F3 Wait for a While...  ")
		time.sleep(3)
		print("")
		print("_"*width)
		sy = "\U0001F6A8 \033[32m**Your Expense Record was Saved Sucessfully**\033[0m"
		print(sy.center(width))
		print("_"*width)
		print("_"*width)
		print("")
		print("      1. Back To Main Menu: ")
		print("      2.Add More Expense: : ")
		print("      3.**Press any Other Key for Exit:** ")
		print("_"*width)
		print("    Please Select Your Option: ")
		z = input()
		if z == '2':
			add_exp(user_id)
		elif z == '1':
			clear_screen()
			main(user_id)
		else:
			sys.exit()		
	elif s == '1':
		clear_screen()
		main(user_id)
	elif s != '2' and s != '1' and s != '0' :
		sys.exit()
def search(user_id):
	clear_screen()
	with open("Database.txt","rb") as file:
		l_encrypt = file.read()
		l_decrypt = fernet.decrypt(l_encrypt)
		l_string = l_decrypt.decode()
		l = json.loads(l_string)
	if os.path.getsize("main_database.txt") != 0:
		with open("main_database.txt","rb") as file:
			main_list_encrypt = file.read()
			main_list_decrypt = fernet.decrypt(main_list_encrypt)
			main_list_string = main_list_decrypt.decode()
			main_list = json.loads(main_list_string)
		f = 0
		te = 0.0
		tex = 0.0
		ct = "N/A"
		fg = False
		t_list = []
		list(t_list)
		while f< len(main_list):
			if main_list[f]["uid"] == user_id:
				fg = True
				target = f
			f = f + 1
		if fg == True:
			vb = 0
			while vb < len(main_list[target]["details"]):
				if main_list[target]["details"][vb]["Date"]["year"] == date.today().year and main_list[target]["details"][vb]["Date"]["month"] == date.today().month and main_list[target]["details"][vb]["Date"]["day"] == date.today().day:
					ln = 0
					t_list = []
					list(t_list)
					while ln < len(main_list[target]["details"][vb]["expense"]):
						m = main_list[target]["details"][vb]["expense"][ln]["amount"]
						t_list.append(m)
						te = te + m
						ln = ln + 1
				vb = vb + 1
			if te > 0:
				max_amt = max(t_list)
			else:
				max_amt = 0
			vc = 0
			while vc < len(main_list[target]["details"]):
				if main_list[target]["details"][vc]["Date"]["year"] == date.today().year and main_list[target]["details"][vc]["Date"]["month"] == date.today().month and main_list[target]["details"][vc]["Date"]["day"] == date.today().day:
					lm = 0
					while lm < len(main_list[target]["details"][vc]["expense"]):
						if main_list[target]["details"][vc]["expense"][lm]["amount"] == max_amt:
							ct = main_list[target]["details"][vc]["expense"][lm]["category"]
							if ct == '1':
								ct = "Market"
							elif ct == '2':
								ct = "Food"
							elif ct == '3':
								ct = "Travel"
							elif ct == '4':
								ct = "Others"
						lm = lm + 1
				vc = vc + 1
			vk = 0
			while vk < len(main_list[target]["details"]):
				vd = 0
				teb = 0.0
				if main_list[target]["details"][vk]["Date"]["month"] == date.today().month:
					while vd < len(main_list[target]["details"][vk]["expense"]):
						b = main_list[target]["details"][vk]["expense"][vd]["amount"]
						teb = teb + b
						vd = vd + 1
					tex = tex + teb
				vk = vk + 1
	else:
		te = 0.0
		tex = 0.0
		ct = "N/A"
	i = 0
	while i < len(l):
		if l[i]["uid"] == user_id:
			u = i
		i = i + 1
	print("="*width)
	print("")
	title = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
	print(title.center(width))
	stitle ="\U0001F4D4  - Your Daily Personal Diary - \U0001F4D4"
	print(stitle.center(width))
	fc = "Main-Dashboard-Search-Expense-Panel"
	print("")
	print(fc.center(width))
	com = "[ v1.0.0 | \U0001F6E1  Powered by XyonixTech ]"
	print(com.center(width))
	print("="*width)
	if len(l[u]["name"]) > 8:
		name = l[u]["name"][:8]+".."
	else:
		name = l[u]["name"]
	nm = "USER -"+name
	Date = date.today()
	date_string = str(Date)
	d = "| "+"Date - " + date_string
	print(f"\U0001F464 {nm} |",end="")
	print(d,end="")
	check_te = str(int(te))
	check_tex = str(int(tex))
	if len(check_te) >= 6:
		te_r = te
		if te > 1000000000000:
			te = (te/1000000000000)
			te_n = f"{te:.2f}T"
		elif te > 1000000000:
			te = (te/1000000000)
			te_n = f"{te:.2f}B"
		elif te > 1000000:
			te = (te/1000000)
			te_n = f"{te:.2f}M"
		elif te > 1000:
			te = (te/1000)
			te_n = f"{te:.2f}K"
	else:
		te_r = te
		te_n = f"{te:.2f}"
	if len(check_tex) >= 6:
		tex_r = tex
		if tex > 1000000000000:
			tex = (tex/1000000000000)
			tex_n = f"{tex:.2f}T"
		elif tex > 1000000000:
			tex = (tex/1000000000)
			tex_n = f"{tex:.2f}B"
		elif tex > 1000000:
			tex = (tex/1000000)
			tex_n = f"{tex:.2f}M"
		elif tex > 1000:
			tex = (tex/1000)
			tex_n = f"{tex:.2f}K"
	else:
		tex_r = tex
		tex_n = f"{tex:.2f}"
	print(f"  ||  This Month Total Expense: {tex_n}",end="")
	print("  ||  Most Expensive Category: ",ct,end="")
	print(f"  ||  Today's Total Expense: {te_n}")
	print("-"*width)
	print("")
	print("**Search Any Expense Record By Date**".center(width))
	print("_"*width)
	print("")
	print("***Steps for Search Expense Record***".center(width))
	print("")
	print("\t\t1. Enter the Year of the Expense: ")
	print("\t\t2. Enter the Month of the Expense: ")
	print("\t\t3. Enter the Day of the Expense: ")
	print("")
	print("_"*width)
	print("")
	print("Press 1 for Back to Main-Dashboard 2 for Log out 0 for Proceed and Any other Key for Exit: ")
	print("_"*width)
	xsd = input()
	if xsd == '1':
		clear_screen()
		main(user_id)
	elif xsd == '0':
		if os.path.getsize("main_database.txt") == 0:
			print("_"*width)
			dt = "\U0001F6A8 \033[31mNo Expense Record were Saved in Our Database!\033[0m"
			print(dt.center(width))
			print("_"*width)
		else:
			with open("main_database.txt","rb") as file:
				main_list_encrypt = file.read()
				main_list_decrypt = fernet.decrypt(main_list_encrypt)
				main_list_string = main_list_decrypt.decode()
				main_list = json.loads(main_list_string)
			si = 0
			check = False
			while si < len(main_list):
				if main_list[si]["uid"] == user_id:
					check = True
					target2 = si
				si = si + 1
			if check != True:
				print("_"*width)
				dt = "\U0001F6A8 \033[31mNo Expense Record were Saved in Our Database!\033[0m"
				print(dt.center(width))
				print("_"*width)
			else:
				while True:
					try:
						year = int(input("\tEnter the Year of the Expense: "))
						if 2000 <= year <= datetime.now().year:
							break
						else:
							raise ValueError
					except ValueError:
						print("_"*width)
						dt = "\U0001F6A8 \033[31mWrong Input! Please Enter a Valid Year\033[0m"
						print(dt.center(width))
						print("_"*width)
				while True:
					try:
						month = int(input("\tEnter the Month of the Expense: "))
						if 1 <= month <= 12:
							break
						else:
							raise ValueError
					except ValueError:
						print("_"*width)
						dt = "\U0001F6A8 \033[31mWrong Input! Please Enter a Valid Month\033[0m"
						print(dt.center(width))
						print("_"*width)
				while True:
					try:
						day = int(input("\tEnter the Day of the Expense: "))
						if 1 <= day <= 31:
							break
						else:
							raise ValueError
					except ValueError:
						print("_"*width)
						dt = "\U0001F6A8 \033[31mWrong Input! Please Enter a Valid Day\033[0m"
						print(dt.center(width))
						print("_"*width)
				con = False
				inh = 0
				while inh < len(main_list[target2]["details"]):
					if main_list[target2]["details"][inh]["Date"]["year"] == year and main_list[target2]["details"][inh]["Date"]["month"] == month and main_list[target2]["details"][inh]["Date"]["day"] == day:
						target3 = inh
						con = True 
					inh = inh + 1
				if con == True:
					print("\t\u23F3 Wait for a While...  ")
					time.sleep(3)
					print("-"*width)
					print(f"\t \U0001F4C5 Expense Date: {year}-{month}-{day}")
					print("\tAll Expenses: ")
					ing = 0
					while ing < len(main_list[target2]["details"][target3]["expense"]):
						amt = main_list[target2]["details"][target3]["expense"][ing]["amount"]
						pur = main_list[target2]["details"][target3]["expense"][ing]["purpose"]
						print(f"\t \U0001f4b0 Amount: {amt}")
						print(f"\t \U0001f4ac Purpose: {pur}")
						if main_list[target2]["details"][target3]["expense"][ing]["category"] == '1':
							print("\tCategory: \U0001f6d2 Market")
						elif main_list[target2]["details"][target3]["expense"][ing]["category"] == '2':
							print("\tCategory: \U0001f354 Food")
						elif main_list[target2]["details"][target3]["expense"][ing]["category"] == '3':
							print("\tCategory: \U0001f68b Travel")
						elif main_list[target2]["details"][target3]["expense"][ing]["category"] == '4':
							print("\tCategory: \u2699\ufe0f Others")
						print("-"*width)	
						ing = ing + 1
				else:
					print("\t\u23F3 Wait for a While...  ")
					time.sleep(3)
					print("_"*width)
					dt = "\t\U0001F6A8 \033[31mNo Records were Found!\033[0m"
					print(dt.center(width))
					print("_"*width)
		print("")
		print("\tPress 1 for Back to Main-Dashboard 2 for Search More and Any other Key for Log Out: ")
		print("_"*width)
		xsp = input()
		if xsp == '1':
			clear_screen()
			main(user_id)
		elif xsp == '2':
			search(user_id)
def analyze(user_id):
	clear_screen()
	with open("Database.txt","rb") as file:
		l_encrypt = file.read()
		l_decrypt = fernet.decrypt(l_encrypt)
		l_string = l_decrypt.decode()
		l = json.loads(l_string)
	if os.path.getsize("main_database.txt") != 0:
		with open("main_database.txt","rb") as file:
			main_list_encrypt = file.read()
			main_list_decrypt = fernet.decrypt(main_list_encrypt)
			main_list_string = main_list_decrypt.decode()
			main_list = json.loads(main_list_string)
		f = 0
		te = 0.0
		tex = 0.0
		ct = "N/A"
		fg = False
		t_list = []
		list(t_list)
		while f< len(main_list):
			if main_list[f]["uid"] == user_id:
				fg = True
				target = f
			f = f + 1
		if fg == True:
			vb = 0
			while vb < len(main_list[target]["details"]):
				if main_list[target]["details"][vb]["Date"]["year"] == date.today().year and main_list[target]["details"][vb]["Date"]["month"] == date.today().month and main_list[target]["details"][vb]["Date"]["day"] == date.today().day:
					ln = 0
					t_list = []
					list(t_list)
					while ln < len(main_list[target]["details"][vb]["expense"]):
						m = main_list[target]["details"][vb]["expense"][ln]["amount"]
						t_list.append(m)
						te = te + m
						ln = ln + 1
				vb = vb + 1
			if te > 0:
				max_amt = max(t_list)
			else:
				max_amt = 0
			vc = 0
			while vc < len(main_list[target]["details"]):
				if main_list[target]["details"][vc]["Date"]["year"] == date.today().year and main_list[target]["details"][vc]["Date"]["month"] == date.today().month and main_list[target]["details"][vc]["Date"]["day"] == date.today().day:
					lm = 0
					while lm < len(main_list[target]["details"][vc]["expense"]):
						if main_list[target]["details"][vc]["expense"][lm]["amount"] == max_amt:
							ct = main_list[target]["details"][vc]["expense"][lm]["category"]
							if ct == '1':
								ct = "Market"
							elif ct == '2':
								ct = "Food"
							elif ct == '3':
								ct = "Travel"
							elif ct == '4':
								ct = "Others"
						lm = lm + 1
				vc = vc + 1
			vk = 0
			while vk < len(main_list[target]["details"]):
				vd = 0
				teb = 0.0
				if main_list[target]["details"][vk]["Date"]["month"] == date.today().month:
					while vd < len(main_list[target]["details"][vk]["expense"]):
						b = main_list[target]["details"][vk]["expense"][vd]["amount"]
						teb = teb + b
						vd = vd + 1
					tex = tex + teb
				vk = vk + 1
	else:
		te = 0.0
		tex = 0.0
		ct = "N/A"
	i = 0
	while i < len(l):
		if l[i]["uid"] == user_id:
			u = i
		i = i + 1
	print("="*width)
	print("")
	title = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
	print(title.center(width))
	stitle ="\U0001F4D4  - Your Daily Personal Diary - \U0001F4D4"
	print(stitle.center(width))
	fc = "Main-Dashboard-Analyze-Today's-Expense-Panel"
	print("")
	print(fc.center(width))
	com = "[ v1.0.0 | \U0001F6E1  Powered by XyonixTech ]"
	print(com.center(width))
	print("="*width)
	if len(l[u]["name"]) > 8:
		name = l[u]["name"][:8]+".."
	else:
		name = l[u]["name"]
	nm = "USER -"+name
	Date = date.today()
	date_string = str(Date)
	d = "| "+"Date - " + date_string
	print(f"\U0001F464 {nm} |",end="")
	print(d,end="")
	check_te = str(int(te))
	check_tex = str(int(tex))
	if len(check_te) >= 6:
		te_r = te
		if te > 1000000000000:
			te = (te/1000000000000)
			te_n = f"{te:.2f}T"
		elif te > 1000000000:
			te = (te/1000000000)
			te_n = f"{te:.2f}B"
		elif te > 1000000:
			te = (te/1000000)
			te_n = f"{te:.2f}M"
		elif te > 1000:
			te = (te/1000)
			te_n = f"{te:.2f}K"
	else:
		te_r = te
		te_n = f"{te:.2f}"
	if len(check_tex) >= 6:
		tex_r = tex
		if tex > 1000000000000:
			tex = (tex/1000000000000)
			tex_n = f"{tex:.2f}T"
		elif tex > 1000000000:
			tex = (tex/1000000000)
			tex_n = f"{tex:.2f}B"
		elif tex > 1000000:
			tex = (tex/1000000)
			tex_n = f"{tex:.2f}M"
		elif tex > 1000:
			tex = (tex/1000)
			tex_n = f"{tex:.2f}K"
	else:
		tex_r = tex
		tex_n = f"{tex:.2f}"
	print(f"  ||  This Month Total Expense: {tex_n}",end="")
	print("  ||  Most Expensive Category: ",ct,end="")
	print(f"  ||  Today's Total Expense: {te_n}")
	print("-"*width)
	print("")
	if os.path.getsize("main_database.txt") == 0:
			print("_"*width)
			dt = "\U0001F6A8 \033[31mNo Expense Record have been Saved in Our Database Yet Today!\033[0m"
			print(dt.center(width))
			print("_"*width)
	else:
		with open("main_database.txt","rb") as file:
			main_list_encrypt = file.read()
			main_list_decrypt = fernet.decrypt(main_list_encrypt)
			main_list_string = main_list_decrypt.decode()
			main_list = json.loads(main_list_string)
		si = 0
		check = False
		while si < len(main_list):
			if main_list[si]["uid"] == user_id:
				check = True
				target2 = si
			si = si + 1
		if check != True or te == 0:
			print("_"*width)
			dt = "\U0001F6A8 \033[31mNo Expense Record have been Saved in Our Database Yet Today!\033[0m"
			print(dt.center(width))
			print("_"*width)
		else:
			print("-"*width)
			print("Todays Expense Analysis".center(width))
			print("")
			print("-"*width)
			igk = 0
			flag = False 
			while igk < len(main_list[target2]["details"]):
				if main_list[target2]["details"][igk]["Date"]["year"] == date.today().year and main_list[target2]["details"][igk]["Date"]["month"] == date.today().month and main_list[target2]["details"][igk]["Date"]["day"] == date.today().day:
					flag = True
					target3 = igk
				igk = igk + 1
			if flag == True:
				igt = 0
				cat_market_amt = 0
				cat_food_amt = 0
				cat_travel_amt = 0
				cat_other_amt = 0
				while igt < len(main_list[target2]["details"][target3]["expense"]):
					amt = main_list[target2]["details"][target3]["expense"][igt]["amount"]
					cat = main_list[target2]["details"][target3]["expense"][igt]["category"]
					if cat == '1':
						cat_market_amt = amt + cat_market_amt
					elif cat == '2':
						cat_food_amt = amt + cat_food_amt
					elif cat == '3':
						cat_travel_amt = amt + cat_travel_amt
					elif cat == '4':
						cat_other_amt = amt + cat_other_amt
					igt = igt + 1
				print(f"\t\t\tCategory: \U0001f6d2 Market({(cat_market_amt/te)*100:.0f}%)-{cat_market_amt}\n\n")
				print(f"\t\t\tCategory: \U0001f354 Food({(cat_food_amt/te)*100:.0f}%)-{cat_food_amt}\n\n")
				print(f"\t\t\tCategory: \U0001f68b Travel({(cat_travel_amt/te)*100:.0f}%)-{cat_travel_amt}\n\n")
				print(f"\t\t\tCategory: \u2699\ufe0f Others({(cat_other_amt/te)*100:.0f}%)-{cat_other_amt}")
				print("\t\t-----------------------------------------------------------------------------------")
				print(f"\t\tTotal Expense:                                 {te:.2f}                         ")
	print("-"*width)
	print("\tPress 1 For Back To Main Dashboard or Any Other Key for Log Out")
	print("-"*width)
	xsd = input()
	if xsd == '1':
		clear_screen()
		main(user_id)
def settings(user_id):
	clear_screen()
	with open("Database.txt","rb") as file:
		l_encrypt = file.read()
		l_decrypt = fernet.decrypt(l_encrypt)
		l_string = l_decrypt.decode()
		l = json.loads(l_string)
	if os.path.getsize("main_database.txt") != 0:
		with open("main_database.txt","rb") as file:
			main_list_encrypt = file.read()
			main_list_decrypt = fernet.decrypt(main_list_encrypt)
			main_list_string = main_list_decrypt.decode()
			main_list = json.loads(main_list_string)
		f = 0
		te = 0.0
		tex = 0.0
		ct = "N/A"
		fg = False
		t_list = []
		list(t_list)
		while f< len(main_list):
			if main_list[f]["uid"] == user_id:
				fg = True
				target = f
			f = f + 1
		if fg == True:
			vb = 0
			while vb < len(main_list[target]["details"]):
				if main_list[target]["details"][vb]["Date"]["year"] == date.today().year and main_list[target]["details"][vb]["Date"]["month"] == date.today().month and main_list[target]["details"][vb]["Date"]["day"] == date.today().day:
					ln = 0
					t_list = []
					list(t_list)
					while ln < len(main_list[target]["details"][vb]["expense"]):
						m = main_list[target]["details"][vb]["expense"][ln]["amount"]
						t_list.append(m)
						te = te + m
						ln = ln + 1
				vb = vb + 1
			if te > 0:
				max_amt = max(t_list)
			else:
				max_amt = 0
			vc = 0
			while vc < len(main_list[target]["details"]):
				if main_list[target]["details"][vc]["Date"]["year"] == date.today().year and main_list[target]["details"][vc]["Date"]["month"] == date.today().month and main_list[target]["details"][vc]["Date"]["day"] == date.today().day:
					lm = 0
					while lm < len(main_list[target]["details"][vc]["expense"]):
						if main_list[target]["details"][vc]["expense"][lm]["amount"] == max_amt:
							ct = main_list[target]["details"][vc]["expense"][lm]["category"]
							if ct == '1':
								ct = "Market"
							elif ct == '2':
								ct = "Food"
							elif ct == '3':
								ct = "Travel"
							elif ct == '4':
								ct = "Others"
						lm = lm + 1
				vc = vc + 1
			vk = 0
			while vk < len(main_list[target]["details"]):
				vd = 0
				teb = 0.0
				if main_list[target]["details"][vk]["Date"]["month"] == date.today().month:
					while vd < len(main_list[target]["details"][vk]["expense"]):
						b = main_list[target]["details"][vk]["expense"][vd]["amount"]
						teb = teb + b
						vd = vd + 1
					tex = tex + teb
				vk = vk + 1
	else:
		te = 0.0
		tex = 0.0
		ct = "N/A"
	i = 0
	while i < len(l):
		if l[i]["uid"] == user_id:
			u = i
		i = i + 1
	print("="*width)
	print("")
	title = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
	print(title.center(width))
	stitle ="\U0001F4D4  - Your Daily Personal Diary - \U0001F4D4"
	print(stitle.center(width))
	fc = "Main-Dashboard-Profile-Settings-Panel"
	print("")
	print(fc.center(width))
	com = "[ v1.0.0 | \U0001F6E1  Powered by XyonixTech ]"
	print(com.center(width))
	print("="*width)
	if len(l[u]["name"]) > 8:
		name = l[u]["name"][:8]+".."
	else:
		name = l[u]["name"]
	nm = "USER -"+name
	Date = date.today()
	date_string = str(Date)
	d = "| "+"Date - " + date_string
	print(f"\U0001F464 {nm} |",end="")
	print(d,end="")
	check_te = str(int(te))
	check_tex = str(int(tex))
	if len(check_te) >= 6:
		te_r = te
		if te > 1000000000000:
			te = (te/1000000000000)
			te_n = f"{te:.2f}T"
		elif te > 1000000000:
			te = (te/1000000000)
			te_n = f"{te:.2f}B"
		elif te > 1000000:
			te = (te/1000000)
			te_n = f"{te:.2f}M"
		elif te > 1000:
			te = (te/1000)
			te_n = f"{te:.2f}K"
	else:
		te_r = te
		te_n = f"{te:.2f}"
	if len(check_tex) >= 6:
		tex_r = tex
		if tex > 1000000000000:
			tex = (tex/1000000000000)
			tex_n = f"{tex:.2f}T"
		elif tex > 1000000000:
			tex = (tex/1000000000)
			tex_n = f"{tex:.2f}B"
		elif tex > 1000000:
			tex = (tex/1000000)
			tex_n = f"{tex:.2f}M"
		elif tex > 1000:
			tex = (tex/1000)
			tex_n = f"{tex:.2f}K"
	else:
		tex_r = tex
		tex_n = f"{tex:.2f}"
	print(f"  ||  This Month Total Expense: {tex_n}",end="")
	print("  ||  Most Expensive Category: ",ct,end="")
	print(f"  ||  Today's Total Expense: {te_n}")
	print("-"*width)
	print("")
	print("***Change Your Profile Details***".center(width))
	print("-"*width)
	print("\t\t1. Change Your Name: ")
	print("\t\t2. Change Your Age: ")
	print("\t\t3. Edit Your Pet Name: ")
	print("\t\t4. Edit Your Childhood Friend Name: ")
	print("-"*width)
	print("")
	print("-"*width)
	print("\t\tPlease Enter (1-4) For Proceed And 5 for Go Back Main_Dashboard and Any Other Key For Log Out: ")
	print("-"*width)
	with open("Database.txt","rb")as file:
		li_encrypt = file.read()
		li_decrypt = fernet.decrypt(li_encrypt)
		li = json.loads(li_decrypt.decode())
	ic = 0
	while ic < len(li):
		if li[ic]["uid"] == user_id:
			target3 = ic
		ic = ic + 1
	xsx = input()
	if xsx == '5':
		clear_screen()
		main(user_id)
	elif xsx == '1':
		name = input("\t\t Enter New Name: ")
		name = name.upper()
		li[target3]["name"] = name
		with open("Database.txt","wb")as file:
			li_string = json.dumps(li)
			li_encrypt = fernet.encrypt(li_string.encode())
			file.write((li_encrypt))
	elif xsx == '2':
		age = input("\t\tEnter New Age: ")
		li[target3]["age"] = age
		with open("Database.txt","wb")as file:
			li_string = json.dumps(li)
			li_encrypt = fernet.encrypt(li_string.encode())
			file.write((li_encrypt))
	elif xsx == '3':
		pet = input("\t\tEnter New Pet Name: ")
		li[target3]["pet"] = pet
		with open("Database.txt","wb")as file:
			li_string = json.dumps(li)
			li_encrypt = fernet.encrypt(li_string.encode())
			file.write((li_encrypt))
	elif xsx == '4':
		ch_friend = input("\t\tEnter New Childhood Friend Name: ")
		li[target3]["friend"] = ch_friend
		with open("Database.txt","wb")as file:
			li_string = json.dumps(li)
			li_encrypt = fernet.encrypt(li_string.encode())
			file.write((li_encrypt))
	print("")
	print("_"*width)
	sy = "\U0001F6A8 \033[32m**Your Record was Changed Sucessfully**\033[0m"
	print(sy.center(width))
	print("_"*width)
	print("_"*width)
	print("")
	print("")
	print("-"*width)
	print("\t\tPress 1 For Back To Main Dashboard and Any Other Key For Log Out:")
	print("-"*width)
	xsd = input()
	if xsd == '1':
		clear_screen()
		main(user_id)
def help(user_id):
	clear_screen()
	with open("Database.txt","rb") as file:
		l_encrypt = file.read()
		l_decrypt = fernet.decrypt(l_encrypt)
		l_string = l_decrypt.decode()
		l = json.loads(l_string)
	if os.path.getsize("main_database.txt") != 0:
		with open("main_database.txt","rb") as file:
			main_list_encrypt = file.read()
			main_list_decrypt = fernet.decrypt(main_list_encrypt)
			main_list_string = main_list_decrypt.decode()
			main_list = json.loads(main_list_string)
		f = 0
		te = 0.0
		tex = 0.0
		ct = "N/A"
		fg = False
		t_list = []
		list(t_list)
		while f< len(main_list):
			if main_list[f]["uid"] == user_id:
				fg = True
				target = f
			f = f + 1
		if fg == True:
			vb = 0
			while vb < len(main_list[target]["details"]):
				if main_list[target]["details"][vb]["Date"]["year"] == date.today().year and main_list[target]["details"][vb]["Date"]["month"] == date.today().month and main_list[target]["details"][vb]["Date"]["day"] == date.today().day:
					ln = 0
					t_list = []
					list(t_list)
					while ln < len(main_list[target]["details"][vb]["expense"]):
						m = main_list[target]["details"][vb]["expense"][ln]["amount"]
						t_list.append(m)
						te = te + m
						ln = ln + 1
				vb = vb + 1
			if te > 0:
				max_amt = max(t_list)
			else:
				max_amt = 0
			vc = 0
			while vc < len(main_list[target]["details"]):
				if main_list[target]["details"][vc]["Date"]["year"] == date.today().year and main_list[target]["details"][vc]["Date"]["month"] == date.today().month and main_list[target]["details"][vc]["Date"]["day"] == date.today().day:
					lm = 0
					while lm < len(main_list[target]["details"][vc]["expense"]):
						if main_list[target]["details"][vc]["expense"][lm]["amount"] == max_amt:
							ct = main_list[target]["details"][vc]["expense"][lm]["category"]
							if ct == '1':
								ct = "Market"
							elif ct == '2':
								ct = "Food"
							elif ct == '3':
								ct = "Travel"
							elif ct == '4':
								ct = "Others"
						lm = lm + 1
				vc = vc + 1
			vk = 0
			while vk < len(main_list[target]["details"]):
				vd = 0
				teb = 0.0
				if main_list[target]["details"][vk]["Date"]["month"] == date.today().month:
					while vd < len(main_list[target]["details"][vk]["expense"]):
						b = main_list[target]["details"][vk]["expense"][vd]["amount"]
						teb = teb + b
						vd = vd + 1
					tex = tex + teb
				vk = vk + 1
	else:
		te = 0.0
		tex = 0.0
		ct = "N/A"
	i = 0
	while i < len(l):
		if l[i]["uid"] == user_id:
			u = i
		i = i + 1
	print("="*width)
	print("")
	title = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
	print(title.center(width))
	stitle ="\U0001F4D4  - Your Daily Personal Diary - \U0001F4D4"
	print(stitle.center(width))
	fc = "Main-Dashboard-Help-Panel"
	print("")
	print(fc.center(width))
	com = "[ v1.0.0 | \U0001F6E1  Powered by XyonixTech ]"
	print(com.center(width))
	print("="*width)
	if len(l[u]["name"]) > 8:
		name = l[u]["name"][:8]+".."
	else:
		name = l[u]["name"]
	nm = "USER -"+name
	Date = date.today()
	date_string = str(Date)
	d = "| "+"Date - " + date_string
	print(f"\U0001F464 {nm} |",end="")
	print(d,end="")
	check_te = str(int(te))
	check_tex = str(int(tex))
	if len(check_te) >= 6:
		te_r = te
		if te > 1000000000000:
			te = (te/1000000000000)
			te_n = f"{te:.2f}T"
		elif te > 1000000000:
			te = (te/1000000000)
			te_n = f"{te:.2f}B"
		elif te > 1000000:
			te = (te/1000000)
			te_n = f"{te:.2f}M"
		elif te > 1000:
			te = (te/1000)
			te_n = f"{te:.2f}K"
	else:
		te_r = te
		te_n = f"{te:.2f}"
	if len(check_tex) >= 6:
		tex_r = tex
		if tex > 1000000000000:
			tex = (tex/1000000000000)
			tex_n = f"{tex:.2f}T"
		elif tex > 1000000000:
			tex = (tex/1000000000)
			tex_n = f"{tex:.2f}B"
		elif tex > 1000000:
			tex = (tex/1000000)
			tex_n = f"{tex:.2f}M"
		elif tex > 1000:
			tex = (tex/1000)
			tex_n = f"{tex:.2f}K"
	else:
		tex_r = tex
		tex_n = f"{tex:.2f}"
	print(f"  ||  This Month Total Expense: {tex_n}",end="")
	print("  ||  Most Expensive Category: ",ct,end="")
	print(f"  ||  Today's Total Expense: {te_n}")
	print("-"*width)
	print("")
	print("*"*width)
	print("")
	print("\U0001F3E2 ABOUT XyonixTech".center(width))
	print("-"*width)
	print("XyonixTexh is an emerging software devolopment firm dedicated to building".center(width))
	print("practical, secure, and offline tech solutions for everyday challenges.\n".center(width))
	print("Our flagship product, Digital Cashier Software, is designed specifically".center(width))
	print(" for middle-class families and students to simplify daily financial tracking".center(width))
	print("with absolute data integrity.\n".center(width))
	print("Founded & Directed by lead Devoloper Sayan Ghosh.".rjust(width))
	print("")
	print("\u2699\ufe0f QUICK SYSTEM MANUAL".center(width))
	print("")
	print("Data Privacy:\n".center(width))
	print("Your records are stored 100% locally. No internet required.\n".center(width))
	print("Strict Policy:\n".center(width))
	print("To ensure financial discipline, completed transactions cannot be edited or deleted\n".center(width))
	print("OFFICIAL SUPPORT".center(width))
	print("For technical support, bugs, or business inquiries, feedback contact our helpdesk.".center(width))
	print("OFFICIAL EMAIL: xyonixtech@gmail.com".center(width))
	print("-"*width)
	print("*"*width)
	print("")
	print("-"*width)
	print("\t\tPress [M] for Back To Main Dashboard and Any Other Key for Log Out")
	print("-"*width)
	xsd = input()
	if xsd == 'M':
		clear_screen()
		main(user_id)
def report(user_id):
	clear_screen()
	with open("Database.txt","rb") as file:
		l_encrypt = file.read()
		l_decrypt = fernet.decrypt(l_encrypt)
		l_string = l_decrypt.decode()
		l = json.loads(l_string)
	if os.path.getsize("main_database.txt") != 0:
		with open("main_database.txt","rb") as file:
			main_list_encrypt = file.read()
			main_list_decrypt = fernet.decrypt(main_list_encrypt)
			main_list_string = main_list_decrypt.decode()
			main_list = json.loads(main_list_string)
		f = 0
		te = 0.0
		tex = 0.0
		ct = "N/A"
		fg = False
		t_list = []
		list(t_list)
		while f< len(main_list):
			if main_list[f]["uid"] == user_id:
				fg = True
				target = f
			f = f + 1
		if fg == True:
			vb = 0
			while vb < len(main_list[target]["details"]):
				if main_list[target]["details"][vb]["Date"]["year"] == date.today().year and main_list[target]["details"][vb]["Date"]["month"] == date.today().month and main_list[target]["details"][vb]["Date"]["day"] == date.today().day:
					ln = 0
					t_list = []
					list(t_list)
					while ln < len(main_list[target]["details"][vb]["expense"]):
						m = main_list[target]["details"][vb]["expense"][ln]["amount"]
						t_list.append(m)
						te = te + m
						ln = ln + 1
				vb = vb + 1
			if te > 0:
				max_amt = max(t_list)
			else:
				max_amt = 0
			vc = 0
			while vc < len(main_list[target]["details"]):
				if main_list[target]["details"][vc]["Date"]["year"] == date.today().year and main_list[target]["details"][vc]["Date"]["month"] == date.today().month and main_list[target]["details"][vc]["Date"]["day"] == date.today().day:
					lm = 0
					while lm < len(main_list[target]["details"][vc]["expense"]):
						if main_list[target]["details"][vc]["expense"][lm]["amount"] == max_amt:
							ct = main_list[target]["details"][vc]["expense"][lm]["category"]
							if ct == '1':
								ct = "Market"
							elif ct == '2':
								ct = "Food"
							elif ct == '3':
								ct = "Travel"
							elif ct == '4':
								ct = "Others"
						lm = lm + 1
				vc = vc + 1
			vk = 0
			while vk < len(main_list[target]["details"]):
				vd = 0
				teb = 0.0
				if main_list[target]["details"][vk]["Date"]["month"] == date.today().month:
					while vd < len(main_list[target]["details"][vk]["expense"]):
						b = main_list[target]["details"][vk]["expense"][vd]["amount"]
						teb = teb + b
						vd = vd + 1
					tex = tex + teb
				vk = vk + 1
	else:
		te = 0.0
		tex = 0.0
		ct = "N/A"
	i = 0
	while i < len(l):
		if l[i]["uid"] == user_id:
			u = i
		i = i + 1
	print("="*width)
	print("")
	title = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
	print(title.center(width))
	stitle ="\U0001F4D4  - Your Daily Personal Diary - \U0001F4D4"
	print(stitle.center(width))
	fc = "Main-Dashboard-Report-Generation-Panel"
	print("")
	print(fc.center(width))
	com = "[ v1.0.0 | \U0001F6E1  Powered by XyonixTech ]"
	print(com.center(width))
	print("="*width)
	if len(l[u]["name"]) > 8:
		name = l[u]["name"][:8]+".."
	else:
		name = l[u]["name"]
	nm = "USER -"+name
	Date = date.today()
	date_string = str(Date)
	d = "| "+"Date - " + date_string
	print(f"\U0001F464 {nm} |",end="")
	print(d,end="")
	check_te = str(int(te))
	check_tex = str(int(tex))
	if len(check_te) >= 6:
		te_r = te
		if te > 1000000000000:
			te = (te/1000000000000)
			te_n = f"{te:.2f}T"
		elif te > 1000000000:
			te = (te/1000000000)
			te_n = f"{te:.2f}B"
		elif te > 1000000:
			te = (te/1000000)
			te_n = f"{te:.2f}M"
		elif te > 1000:
			te = (te/1000)
			te_n = f"{te:.2f}K"
	else:
		te_r = te
		te_n = f"{te:.2f}"
	if len(check_tex) >= 6:
		tex_r = tex
		if tex > 1000000000000:
			tex = (tex/1000000000000)
			tex_n = f"{tex:.2f}T"
		elif tex > 1000000000:
			tex = (tex/1000000000)
			tex_n = f"{tex:.2f}B"
		elif tex > 1000000:
			tex = (tex/1000000)
			tex_n = f"{tex:.2f}M"
		elif tex > 1000:
			tex = (tex/1000)
			tex_n = f"{tex:.2f}K"
	else:
		tex_r = tex
		tex_n = f"{tex:.2f}"
	print(f"  ||  This Month Total Expense: {tex_n}",end="")
	print("  ||  Most Expensive Category: ",ct,end="")
	print(f"  ||  Today's Total Expense: {te_n}")
	print("-"*width)
	print("")
	print("-"*width)
	print("Generate Report Of Your Expense Records".center(width))
	print("")
	print("\t\t1. Generate Report Of Today's Expense Records:")
	print("\t\t2. Generate Report Of This Month's Total Expense Records:")
	print("\t\t3. Generate Report Of Any Day's Expense Records: ")
	print("\t\t4. Back To Main-Dashboard: ")
	print("\t\t**. Any Other key for Log Out:  ")
	print("")
	print("-"*width)
	print("\t\tPlease Enter Your Choice: (1-4) or Any Other Key:")
	xzs = input()
	if xzs == '1':
		print("\t\u23F3 Wait for a While...  \n")
		time.sleep(3)
		TodayReport(user_id)
	elif xzs == '2':
		print("\t\u23F3 Wait for a While...  \n")
		time.sleep(3)
		MonthReport(user_id,tex)
	elif xzs == '3':
		print("\t\u23F3 Wait for a While...  \n")
		time.sleep(3)
		DayReport(user_id)
	elif xzs == '4':
		clear_screen()
		main(user_id)
def TodayReport(user_id):
	with open("main_database.txt","rb")as file:
		main_list_encrypt = file.read()
		main_list_decrypt = fernet.decrypt(main_list_encrypt)
		main_list = json.loads(main_list_decrypt.decode())
	index = 0
	check = False 
	while index < len(main_list):
		if main_list[index]["uid"] == user_id:
			target = index
			check = True
		index = index + 1
	if os.path.getsize("main_database.txt") == 0 or check == False:
		print("_"*width)
		dt = "\U0001F6A8 \033[31mYou Have No Expense Record!\033[0m"
		print(dt.center(width))
		print("_"*width)
		print("-"*width)
		print("\t\tPress [M] for Back To Main Menu Or Any Other Key for Log Out: ")
		print("-"*width)
		sdf = input()
		if sdf == 'M':
			clear_screen()
			main(user_id)
	else:
		i = 0
		flag = False 
		while i < len(main_list[target]["details"]):
			if main_list[target]["details"][i]["Date"]["year"] == date.today().year and main_list[target]["details"][i]["Date"]["month"] == date.today().month and main_list[target]["details"][i]["Date"]["day"] == date.today().day:
				target1 = i
				flag = True 
			i = i + 1
		j = 0
		if flag == True:
			pdf = FPDF()
			pdf.add_page()
			pdf.set_font("Helvetica",style="B",size=25)
			pdf.cell(200,10, text = "TODAY'S EXPENSE RECORDS REPORT",align="C",new_x="LMARGIN",new_y="NEXT")
			while j < len(main_list[target]["details"][target1]["expense"]):
				pdf.set_font("Helvetica",style="",size=16)
				cat_p = main_list[target]["details"][target1]["expense"][j]["category"]
				if cat_p == '1':
					cat = "Market"
				elif cat_p == '2':
					cat = "Food"
				elif cat_p == '3':
					cat = "Travel"
				elif cat_p == '4':
					cat = "Others"
				amt = main_list[target]["details"][target1]["expense"][j]["amount"]
				pur = main_list[target]["details"][target1]["expense"][j]["purpose"]
				pdf.write(h=20,text = f"Category: {cat}\n")
				pdf.write(h=10,text = f"Amount: {amt}\n")
				pdf.write(h=10,text = f"Purpose: {pur}\n\n")
				j = j + 1
			desktop_path = Path.home() / "Desktop" / "Expense Report.pdf"
			pdf.output(desktop_path)
			print("")
			print("_"*width)
			sy = "\U0001F6A8 \033[32m**Your Record was Generated Sucessfully**\033[0m"
			print(sy.center(width))
			print("_"*width)
			print("-"*width)
			print("\t\tPress [M] for Back To Main Menu [S] for Show Report Or Any Other Key for Log Out: ")
			print("-"*width)
			sdf = input()
			if sdf == 'M':
				clear_screen()
				main(user_id)
			elif sdf == 'S':
				os.startfile(desktop_path)
				print("-"*width)
				print("\t\tPress [M] for Back To Main Menu Or Any Other Key for Log Out: ")
				print("-"*width)
				sdv = input()
				if sdv == 'M':
					clear_screen()
					main(user_id)
		else:
			print("_"*width)
			dt = "\U0001F6A8 \033[31mNoExpense Record have been Saved in Our Database Yet Today!\033[0m"
			print(dt.center(width))
			print("_"*width)
			print("-"*width)
			print("\t\tPress [M] for Back To Main Menu Or Any Other Key for Log Out: ")
			print("-"*width)
			sdf = input()
			if sdf == 'M':
				clear_screen()
				main(user_id)
def MonthReport(user_id,tex):
	with open("main_database.txt","rb")as file:
		main_list_encrypt = file.read()
		main_list_decrypt = fernet.decrypt(main_list_encrypt)
		main_list = json.loads(main_list_decrypt.decode())
	index = 0
	check = False 
	while index < len(main_list):
		if main_list[index]["uid"] == user_id:
			target = index
			check = True
		index = index + 1
	if os.path.getsize("main_database.txt") == 0 or check == False or tex == 0:
		print("_"*width)
		dt = "\U0001F6A8 \033[31mYou Have No Expense Record!\033[0m"
		print(dt.center(width))
		print("_"*width)
		print("-"*width)
		print("\t\tPress [M] for Back To Main Menu Or Any Other Key for Log Out: ")
		print("-"*width)
		sdv = input()
		if sdv == 'M':
			clear_screen()
			main(user_id)
	else:
		i = 0
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font("Helvetica",style="B",size=25)
		pdf.cell(200,10, text = "THIS MONTH'S EXPENSE RECORDS REPORT",align="C")
		while i < len(main_list[target]["details"]):
			if main_list[target]["details"][i]["Date"]["month"] == date.today().month:
				year = main_list[target]["details"][i]["Date"]["year"]
				month = main_list[target]["details"][i]["Date"]["month"]
				day = main_list[target]["details"][i]["Date"]["day"]
				pdf.set_font("Helvetica",style="B",size=16)
				pdf.write(h = 20,text=f"Date: {year}-{month}-{day}\n")
				j = 0
				while j < len(main_list[target]["details"][i]["expense"]):
					amt = main_list[target]["details"][i]["expense"][j]["amount"]
					cat_p = main_list[target]["details"][i]["expense"][j]["category"]
					pur = main_list[target]["details"][i]["expense"][j]["purpose"]
					if cat_p == '1':
						cat = "Market"
					elif cat_p == '2':
						cat = "Food"
					elif cat_p == '3':
						cat = "Travel"
					elif cat_p == '4':
						cat = "Others"
					pdf.set_font("Helvetica",style="",size=16)
					pdf.write(h=10,text = f"Category: {cat}\n")
					pdf.write(h=10,text = f"Amount: {amt}\n")
					pdf.write(h=10,text = f"Purpose: {pur}\n\n")
					j = j + 1
			i = i + 1
		desktop_path = Path.home() / "Desktop" / "Expense Report Of Month.pdf"
		pdf.output(desktop_path)
		print("")
		print("_"*width)
		sy = "\U0001F6A8 \033[32m**Your Record was Generated Sucessfully**\033[0m"
		print(sy.center(width))
		print("_"*width)
		print("-"*width)
		print("\t\tPress [M] for Back To Main Menu [S] for Show Report Or Any Other Key for Log Out: ")
		print("-"*width)
		sdf = input()
		if sdf == 'M':
			clear_screen()
			main(user_id)
		elif sdf == 'S':
			os.startfile(desktop_path)
			print("-"*width)
			print("\t\tPress [M] for Back To Main Menu Or Any Other Key for Log Out: ")
			print("-"*width)
			sdv = input()
			if sdv == 'M':
				clear_screen()
				main(user_id)
def DayReport(user_id):
	while True:
		try:
			year = int(input("\tEnter the Year of the Expense: "))
			if 2000 <= year <= datetime.now().year:
				break
			else:
				raise ValueError
		except ValueError:
			print("_"*width)
			dt = "\U0001F6A8 \033[31mWrong Input! Please Enter a Valid Year\033[0m"
			print(dt.center(width))
			print("_"*width)
	while True:
		try:
			month = int(input("\tEnter the Month of the Expense: "))
			if 1 <= month <= 12:
				break
			else:
				raise ValueError
		except ValueError:
			print("_"*width)
			dt = "\U0001F6A8 \033[31mWrong Input! Please Enter a Valid Month\033[0m"
			print(dt.center(width))
			print("_"*width)
	while True:
		try:
			day = int(input("\tEnter the Day of the Expense: "))
			if 1 <= day <= 31:
				break
			else:
				raise ValueError
		except ValueError:
			print("_"*width)
			dt = "\U0001F6A8 \033[31mWrong Input! Please Enter a Valid Day\033[0m"
			print(dt.center(width))
			print("_"*width)
	with open("main_database.txt","rb")as file:
		main_list_encrypt = file.read()
		main_list_decrypt = fernet.decrypt(main_list_encrypt)
		main_list = json.loads(main_list_decrypt.decode())
	index = 0
	check = False 
	while index < len(main_list):
		if main_list[index]["uid"] == user_id:
			target = index
			check = True
		index = index + 1
	if os.path.getsize("main_database.txt") == 0 or check == False:
		print("_"*width)
		dt = "\U0001F6A8 \033[31mYou Have No Expense Record!\033[0m"
		print(dt.center(width))
		print("_"*width)
		print("-"*width)
		print("\t\tPress [M] for Back To Main Menu Or Any Other Key for Log Out: ")
		print("-"*width)
		sdv = input()
		if sdv == 'M':
			clear_screen()
			main(user_id)
	else:
		i = 0
		flag = False 
		while i < len(main_list[target]["details"]):
			if main_list[target]["details"][i]["Date"]["year"] == year and main_list[target]["details"][i]["Date"]["month"] == month and main_list[target]["details"][i]["Date"]["day"] == day:
				target1 = i
				flag = True 
			i = i + 1
		j = 0
		if flag == True:
			pdf = FPDF()
			pdf.add_page()
			pdf.set_font("Helvetica",style="B",size=25)
			pdf.cell(200,10, text = "EXPENSE RECORDS REPORT",align="C",new_x="LMARGIN",new_y="NEXT")
			pdf.set_font("Helvetica",style="B",size=16)
			pdf.cell(200,10, text = f"Date: {year}-{month}-{day}",align="C",new_x="LMARGIN",new_y="NEXT")
			while j < len(main_list[target]["details"][target1]["expense"]):
				pdf.set_font("Helvetica",style="",size=16)
				cat_p = main_list[target]["details"][target1]["expense"][j]["category"]
				if cat_p == '1':
					cat = "Market"
				elif cat_p == '2':
					cat = "Food"
				elif cat_p == '3':
					cat = "Travel"
				elif cat_p == '4':
					cat = "Others"
				amt = main_list[target]["details"][target1]["expense"][j]["amount"]
				pur = main_list[target]["details"][target1]["expense"][j]["purpose"]
				pdf.write(h=10,text = f"Category: {cat}\n")
				pdf.write(h=10,text = f"Amount: {amt}\n")
				pdf.write(h=10,text = f"Purpose: {pur}\n\n")
				j = j + 1
			desktop_path = Path.home() / "Desktop" / "Expense Report Of Day.pdf"
			pdf.output(desktop_path)
			print("\t\u23F3 Wait for a While...  \n")
			time.sleep(3)
			print("")
			print("_"*width)
			sy = "\U0001F6A8 \033[32m**Your Record was Generated Sucessfully**\033[0m"
			print(sy.center(width))
			print("_"*width)
			print("-"*width)
			print("\t\tPress [M] for Back To Main Menu [S] for Show Report Or Any Other Key for Log Out: ")
			print("-"*width)
			sdf = input()
			if sdf == 'M':
				clear_screen()
				main(user_id)
			elif sdf == 'S':
				os.startfile(desktop_path)
				print("-"*width)
				print("\t\tPress [M] for Back To Main Menu Or Any Other Key for Log Out: ")
				print("-"*width)
				sdv = input()
				if sdv == 'M':
					clear_screen()
					main(user_id)
		else:
			print("_"*width)
			dt = "\U0001F6A8 \033[31mNoExpense Record have been Found in Our Database in This Date!\033[0m"
			print(dt.center(width))
			print("_"*width)
			print("-"*width)
			print("\t\tPress [M] for Back To Main Menu Or Any Other Key for Log Out: ")
			print("-"*width)
			sdf = input()
			if sdf == 'M':
				clear_screen()
				main(user_id)
while True:
	clear_screen()
	print("="*width)
	title = "\U0001F512 DIGITAL CASHIER SOFTWARE \U0001F512"
	print(title.center(width))
	stitle ="\U0001F4D4  - Your Daily Personal Diary - \U0001F4D4"
	print(stitle.center(width))
	print("="*width)
	print("")
	print("   Welcome to your trusted financial companion.                      ")
	print("")
	print("          1.\U0001F510 Log in to Your Account ")
	print("          2.\U0001F4DD Register New Account ")
	print("          3.\u274c Exit Software ")
	print("")
	print("="*width)
	com = "[ v1.0.0 | \U0001F6E1  Powered by XyonixTech ]"
	print(com.center(width))
	print("="*width)
	print("     Please Select Your Option(1-3)-> ")
	lr = input()
	if lr == '1':
		enter,user_id=Login()
		if enter == 0:
			#main dashboard
			print("    \u23F3 Wait for a While...  ")
			time.sleep(3)
			clear_screen()
			main(user_id) 
		elif enter == 5:
			clear_screen()
			continue 
		else:
			time.sleep(1)
			if os.path.getsize("Database.txt") != 0:
				print("    \u23F3 Wait for a While...  ")
				time.sleep(3)
				clear_screen()
				print("")
				print("_"*width)
				print("")
				alert ="\u26A0\uFE0F \033[31mINVALID USER!!\033[0m"
				print(alert.center(width))
				print("_"*width)
				print("")
				print("="*width)
				print("")
				inc = "Incorrect User Id and Password"
				print(inc.center(width))
				print("")
				print("         1. \U0001F519 Back To Main Menu ")
				print("         2. \u2753 Forgot User Id / Password: ")
				print("         **  Press any Other Key for Exit : \n")
				print("="*width)
				print(       "Please Select Your Option--> ")
				s = input()
				if s == '1':
					clear_screen()
					continue
				elif s == '2':
					xc = forget()
					if xc == 5:
						clear_screen()
						continue 
				else:
					break
			print("")
			print("_"*width)
			print("")
			print("      1. Back To Main Menu: ")
			print("      **Press any Other Key for Exit: ")
			print("_"*width)
			print("   Please Select Your Option: ")
			n = input()
			if n == '1':
				clear_screen()
				continue
			else:
				break
	elif lr == '2':
		k = Register()
		if k == 1:
			print("")
			print("_"*width)
			print("")
			print("      1. Back To Main Menu: ")
			print("      **Press any Other Key for Exit: ")
			print("_"*width)
			print("   Please Select Your Option: ")
			t = input()
			if t == '1':
				clear_screen()
				continue
			else:
				break
		elif k == 6:
			clear_screen()
			continue 
	elif lr == '3':
		break 
	else:
		time.sleep(1)
		print("      \U0001F6A8 \033[31mYour Input is Wrong try again!\033[0m")
		print("")
		print("_"*width)
		print("")
		print("      1. Back To Main Menu: ")
		print("     **Press any Other Key for Exit: ")
		print("_"*width)
		print("    Please Select Your Option: ")
		v = input()
		if v == '1':
			clear_screen()
			continue
		else:
			break