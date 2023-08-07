import requests


#def return_id_pprint(id):
#	try:
#		url = "https://mandat4.p.rapidapi.com/id"
#
#		querystring = dict(id=f"{id}")
#
#		headers = {
#			"X-RapidAPI-Key": "e1138de0bamshf4bab9b76bb7f1ep16ce46jsn30e66de2587d",
#			"X-RapidAPI-Host": "mandat4.p.rapidapi.com"
#		}
#		response = requests.get(url, headers=headers, params=querystring)
#
#		if response.json()['block'][0]['block'] != '':
#			"""Foydalanuvchining ma'lumotlari"""
#			user_id = response.json()['short'][0]['id']
#			user_name = response.json()['short'][0]['name']
#			user_status = response.json()['short'][0]['tavsiya']
#			user_info=(f" 🔰 {user_name} \n\n "
#					   f"🆔 {user_id} \n\n"
#					   f" 🗣 {user_status}")
#
#			"""Foydalanuvchilarni Imtiyoz Ma'lumptlarini olish"""
#			imtiyozball = f"IMTIYOZ  BALL - {response.json()['imtiyoz'][0]['Imtiyozball']}"
#			Cefr_ball = f"CEFR BALL - {response.json()['imtiyoz'][0]['CEFRball']}"
#			ijod_ball = f"IJODIY BALL - {response.json()['imtiyoz'][0]['Ijodiyball']}"
#			privilege_info = f"I M T I Y O Z L I    B A L L A R\n\n" \
#							 f"♿  {imtiyozball}\n" \
#							 f"🌐  {Cefr_ball}\n" \
#							 f"📄  {ijod_ball}\n\n"
#
#
#			"""Block fan nomlari, blockning savol va javob sonlari, block umumiy bali """
#			block_answer = []
#			len_ = len(response.json()['block'])
#			for i in range(0, len_):
#				block_answer.append(
#					f"📚{response.json()['block'][i]['block'].split(')')[1]}: {response.json()['block'][i]['savol']}/{response.json()['block'][i]['answer']}  ball-{response.json()['block'][i]['ball']}")
#			block_answer = '\n'.join(block_answer)
#
#			"""Savollarning qaysi biriga to'g'ri yoki noto'g'ri ekanni chiqaradi"""
#			lens = len(response.json()['answers'])
#			answers = []
#			for i in range(0, lens):
#				answers.append(f"{i+1}-{response.json()['answers'][i]['answer']}: {response.json()['answers'][i]['check']}")
#			answers = '\n'.join(answers)
#			return (f'{user_info}\n'
#				   f'<b>__________________________________________</b>\n'
#					f'B L O C K    F A N    B A L L A R I\n\n'
#				   f'{block_answer}\n\n'
#					f'<b>__________________________________________</b>\n'
#					f'{privilege_info}'
#					f'<b>__________________________________________</b>\n\n'
#					f"📌 Umumiy ball - {response.json()['imtiyoz'][0]['Umumiyball']}\n"
#					f'<b>__________________________________________</b>\n\n'
#					f'{answers}\n\n'
#					f'<b>__________________________________________</b>\n\n'
#					f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")
#		else:
#			"""Foydalanuvchining ma'lumotlari"""
#			user_id = response.json()['short'][0]['id']
#			user_name = response.json()['short'][0]['name']
#			user_status = response.json()['short'][0]['tavsiya']
#			user_info = (f" 🔰 {user_name} \n\n "
#						 f"🆔 {user_id} \n\n"
#						 f" 🗣 {user_status}\n\n"
#						 f"<b>__________________________________________</b>\n\n"
#						 f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")
#
#			return f'{user_info}'
#
#	except:
#		return "Bunday Abituriyent topilmadi"

def return_id_pprint(id):
	try:
		try:
			url = "https://mandat-api.p.rapidapi.com/mandat/result/"

			querystring = {"id": f"{id}", "year": "2023"}

			headers = {
				"X-RapidAPI-Key": "26c3feb67amsh6ce49b2cd1d9c02p128ddbjsnd16361994887",
				"X-RapidAPI-Host": "mandat-api.p.rapidapi.com"
			}

			response = requests.get(url, headers=headers, params=querystring)

			if response.json()['status'] != False:
				if response.json()['result'][0]["To'plagan ball"] != 'Qiymatlanmagan!':
					student_name = response.json()['result'][0]['F.I.SH']
					student_id = response.json()['result'][0]['Abituriyent ID raqami']
					total_ball = response.json()['result'][0]["To'plagan ball"]
					lang = response.json()['result'][0]["Ta'lim tili"]
					return (f"🔰 Abituriyent F. I. SH : {student_name}\n\n" \
						  f"🆔 Abituriyent ID raqami: {student_id}\n\n" \
						  f"🌐 Ta'lim tili: {lang}\n\n" \
						  f"<b>__________________________________________</b>\n\n" \
						  f"📌 Umumiy ball - {total_ball}\n\n" \
						  f"<b>__________________________________________</b>\n\n" \
						  f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")
				elif response.json()['result'][0]["To'plagan ball"] == 'Qiymatlanmagan!':
					student_name = response.json()['result'][0]['F.I.SH']
					student_id = response.json()['result'][0]['Abituriyent ID raqami']
					lang = response.json()['result'][0]["Ta'lim tili"]
					return (f"🔰 Abituriyent F.I.SH: {student_name}\n\n"
						  f"🆔 Abituriyent ID raqami: {student_id}\n\n"
						  f"🌐 Ta'lim tili: {lang}\n\n"
						  f"<b>__________________________________________</b>\n\n"
						  f"🗣 TEST SINOVLARIDA ISHTIROK ETMAGANSIZ!\n\n"
						  f"<b>__________________________________________</b>\n\n"
						  f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")

			elif response.json()["status"] == False:
				return ("Bunday talaba topilmadi")
		except:

			url = "https://mandat-api.p.rapidapi.com/mandat/result/"

			querystring = {"id": f"{id}", "year": "2023"}

			headers = {
				"X-RapidAPI-Key": "b5339b1c37mshefba3e47e8e3fc1p1a1d24jsn550e98c9f85e",
				"X-RapidAPI-Host": "mandat-api.p.rapidapi.com"
			}

			response = requests.get(url, headers=headers, params=querystring)

			if response.json()['status'] != False:
				if response.json()['result'][0]["To'plagan ball"] != 'Qiymatlanmagan!':
					student_name = response.json()['result'][0]['F.I.SH']
					student_id = response.json()['result'][0]['Abituriyent ID raqami']
					total_ball = response.json()['result'][0]["To'plagan ball"]
					lang = response.json()['result'][0]["Ta'lim tili"]
					return (f"🔰 Abituriyent F. I. SH : {student_name}\n\n" 
						  f"🆔 Abituriyent ID raqami: {student_id}\n\n" 
						  f"🌐 Ta'lim tili: {lang}\n\n" 
						  f"<b>__________________________________________</b>\n\n" 
						  f"📌 Umumiy ball - {total_ball}\n\n" 
						  f"<b>__________________________________________</b>\n\n" 
						  f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")
				elif response.json()['result'][0]["To'plagan ball"] == 'Qiymatlanmagan!':
					student_name = response.json()['result'][0]['F.I.SH']
					student_id = response.json()['result'][0]['Abituriyent ID raqami']
					lang = response.json()['result'][0]["Ta'lim tili"]
					return (f"🔰 Abituriyent F.I.SH: {student_name}\n\n"
						  f"🆔 Abituriyent ID raqami: {student_id}\n\n"
						  f"🌐 Ta'lim tili: {lang}\n\n"
						  f"<b>__________________________________________</b>\n\n"
						  f"🗣 TEST SINOVLARIDA ISHTIROK ETMAGANSIZ!\n\n"
						  f"<b>__________________________________________</b>\n\n"
						  f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")
	except:
		return ("Xatolik ❌\n"
			  "Birozdan song urinib ko'ring!")

if __name__ == "__main__":
	try:
		try:
			url = "https://mandat-api.p.rapidapi.com/mandat/result/"

			querystring = {"id": "", "year": "2023"}

			headers = {
				"X-RapidAPI-Key": "26c3feb67amsh6ce49b2cd1d9c02p128ddbjsnd16361994887",
				"X-RapidAPI-Host": "mandat-api.p.rapidapi.com"
			}

			response = requests.get(url, headers=headers, params=querystring)

			if response.json()['status'] != False:
				if response.json()['result'][0]["To'plagan ball"] != 'Qiymatlanmagan!':
					student_name = response.json()['result'][0]['F.I.SH']
					student_id = response.json()['result'][0]['Abituriyent ID raqami']
					total_ball = response.json()['result'][0]["To'plagan ball"]
					lang = response.json()['result'][0]["Ta'lim tili"]
					print( f"🔰 Abituriyent F. I. SH : {student_name}\n\n" \
						   f"🆔 Abituriyent ID raqami: {student_id}\n\n" \
						   f"🌐 Ta'lim tili: {lang}\n\n" \
						   f"<b>__________________________________________</b>\n\n" \
						   f"📌 Umumiy ball - {total_ball}\n\n" \
						   f"<b>__________________________________________</b>\n\n" \
						   f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")
				elif response.json()['result'][0]["To'plagan ball"] == 'Qiymatlanmagan!':
					student_name = response.json()['result'][0]['F.I.SH']
					student_id = response.json()['result'][0]['Abituriyent ID raqami']
					lang = response.json()['result'][0]["Ta'lim tili"]
					print (f"🔰 Abituriyent F.I.SH: {student_name}\n\n" 
						   f"🆔 Abituriyent ID raqami: {student_id}\n\n" 
						   f"🌐 Ta'lim tili: {lang}\n\n" 
						   f"<b>__________________________________________</b>\n\n" 
						   f"🗣 TEST SINOVLARIDA ISHTIROK ETMAGANSIZ!\n\n"
						   f"<b>__________________________________________</b>\n\n" 
						   f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")

			elif response.json()["status"] == False:
				print("Bunday talaba topilmadi")
		except:

			url = "https://mandat-api.p.rapidapi.com/mandat/result/"

			querystring = {"id": f"bhfgjnf", "year": "2023"}

			headers = {
				"X-RapidAPI-Key": "b5339b1c37mshefba3e47e8e3fc1p1a1d24jsn550e98c9f85e",
				"X-RapidAPI-Host": "mandat-api.p.rapidapi.com"
			}

			response = requests.get(url, headers=headers, params=querystring)

			if response.json()['status'] != False:
				if response.json()['result'][0]["To'plagan ball"] != 'Qiymatlanmagan!':
					student_name = response.json()['result'][0]['F.I.SH']
					student_id = response.json()['result'][0]['Abituriyent ID raqami']
					total_ball = response.json()['result'][0]["To'plagan ball"]
					lang = response.json()['result'][0]["Ta'lim tili"]
					print(f"🔰 Abituriyent F. I. SH : {student_name}\n\n" \
						  f"🆔 Abituriyent ID raqami: {student_id}\n\n" \
						  f"🌐 Ta'lim tili: {lang}\n\n" \
						  f"<b>__________________________________________</b>\n\n" \
						  f"📌 Umumiy ball - {total_ball}\n\n" \
						  f"<b>__________________________________________</b>\n\n" \
						  f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")
				elif response.json()['result'][0]["To'plagan ball"] == 'Qiymatlanmagan!':
					student_name = response.json()['result'][0]['F.I.SH']
					student_id = response.json()['result'][0]['Abituriyent ID raqami']
					lang = response.json()['result'][0]["Ta'lim tili"]
					print(f"🔰 Abituriyent F.I.SH: {student_name}\n\n"
						  f"🆔 Abituriyent ID raqami: {student_id}\n\n"
						  f"🌐 Ta'lim tili: {lang}\n\n"
						  f"<b>__________________________________________</b>\n\n"
						  f"🗣 TEST SINOVLARIDA ISHTIROK ETMAGANSIZ!\n\n"
						  f"<b>__________________________________________</b>\n\n"
						  f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")
	except:
		print("Xatolik ❌\n" 
			   "Birozdan song urinib ko'ring!")


