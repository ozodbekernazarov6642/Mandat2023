import requests
import requests as requests


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
			"""  aliernazarov192@gmail.com """
			url = "https://mandat-api.p.rapidapi.com/mandat/result/"
			querystring = {"id": f"{id}", "year": "2023"}
			headers = {
				"X-RapidAPI-Key": "5bbf0e5359msh5642f9358f9ea88p132830jsnaa59a66fca3f",
				"X-RapidAPI-Host": "mandat-api.p.rapidapi.com"
			}
			response = requests.get(url, headers=headers, params=querystring)


		except:
			""" birnimabirnima107@gmail.com """

			url = "https://mandat-api.p.rapidapi.com/mandat/result/"

			querystring = {"id": f"{id}", "year": "2023"}

			headers = {
				"X-RapidAPI-Key": "bf39d5286dmsh17a6fa492ae8408p1ae422jsn507e8f83aa24",
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

		#elif response.json()["status"] == False:
		#	return ("Bunday talaba topilmadi")

	except:
		return ("Xatolik 404❌\n"
			  "Serverda nosozlik\n"
				"Tez orada xatoliklar to'g'irlnadi!\n"
				"Admin:@Ozodbek_Ernazarov")

if __name__ == "__main__":
	import requests

	url = "https://mandat-api.p.rapidapi.com/mandat/result/"

	querystring = {"id": "<REQUIRED>", "year": "2022"}

	headers = {
		"X-RapidAPI-Key": "bf39d5286dmsh17a6fa492ae8408p1ae422jsn507e8f83aa24",
		"X-RapidAPI-Host": "mandat-api.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	print(response.json())