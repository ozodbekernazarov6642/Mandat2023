import requests


def return_id_pprint(id):
	try:
		url = "https://mandat4.p.rapidapi.com/id"

		querystring = dict(id=f"{id}")

		headers = {
			"X-RapidAPI-Key": "e1138de0bamshf4bab9b76bb7f1ep16ce46jsn30e66de2587d",
			"X-RapidAPI-Host": "mandat4.p.rapidapi.com"
		}
		response = requests.get(url, headers=headers, params=querystring)

		if response.json()['block'][0]['block'] != '':
			"""Foydalanuvchining ma'lumotlari"""
			user_id = response.json()['short'][0]['id']
			user_name = response.json()['short'][0]['name']
			user_status = response.json()['short'][0]['tavsiya']
			user_info=(f" 🔰 {user_name} \n\n "
					   f"🆔 {user_id} \n\n"
					   f" 🗣 {user_status}")

			"""Foydalanuvchilarni Imtiyoz Ma'lumptlarini olish"""
			imtiyozball = f"IMTIYOZ  BALL - {response.json()['imtiyoz'][0]['Imtiyozball']}"
			Cefr_ball = f"CEFR BALL - {response.json()['imtiyoz'][0]['CEFRball']}"
			ijod_ball = f"IJODIY BALL - {response.json()['imtiyoz'][0]['Ijodiyball']}"
			privilege_info = f"I M T I Y O Z L I    B A L L A R\n\n" \
							 f"♿  {imtiyozball}\n" \
							 f"🌐  {Cefr_ball}\n" \
							 f"📄  {ijod_ball}\n\n"


			"""Block fan nomlari, blockning savol va javob sonlari, block umumiy bali """
			block_answer = []
			len_ = len(response.json()['block'])
			for i in range(0, len_):
				block_answer.append(
					f"📚{response.json()['block'][i]['block'].split(')')[1]}: {response.json()['block'][i]['savol']}/{response.json()['block'][i]['answer']}  ball-{response.json()['block'][i]['ball']}")
			block_answer = '\n'.join(block_answer)

			"""Savollarning qaysi biriga to'g'ri yoki noto'g'ri ekanni chiqaradi"""
			lens = len(response.json()['answers'])
			answers = []
			for i in range(0, lens):
				answers.append(f"{i+1}-{response.json()['answers'][i]['answer']}: {response.json()['answers'][i]['check']}")
			answers = '\n'.join(answers)
			return (f'{user_info}\n'
				   f'<b>__________________________________________</b>\n'
					f'B L O C K    F A N    B A L L A R I\n\n'
				   f'{block_answer}\n\n'
					f'<b>__________________________________________</b>\n'
					f'{privilege_info}'
					f'<b>__________________________________________</b>\n\n'
					f"📌 Umumiy ball - {response.json()['imtiyoz'][0]['Umumiyball']}\n"
					f'<b>__________________________________________</b>\n\n'
					f'{answers}\n\n'
					f'<b>__________________________________________</b>\n\n'
					f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")
		else:
			"""Foydalanuvchining ma'lumotlari"""
			user_id = response.json()['short'][0]['id']
			user_name = response.json()['short'][0]['name']
			user_status = response.json()['short'][0]['tavsiya']
			user_info = (f" 🔰 {user_name} \n\n "
						 f"🆔 {user_id} \n\n"
						 f" 🗣 {user_status}\n\n"
						 f"<b>__________________________________________</b>\n\n"
						 f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>")

			return f'{user_info}'

	except:
		return "Bunday Abituriyent topilmadi"




if __name__ == "__main__":
	url = "https://mandat4.p.rapidapi.com/id"

	querystring = dict(id="3907823")

	headers = {
		"X-RapidAPI-Key": "e1138de0bamshf4bab9b76bb7f1ep16ce46jsn30e66de2587d",
		"X-RapidAPI-Host": "mandat4.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	print(response.json())







