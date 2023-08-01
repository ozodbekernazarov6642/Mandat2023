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


		if response.json()['short'][0]['tavsiya'] != '<i>Неоцененный!</i>' and response.json()['block'][0]['block']:
			"""Foydalanuvchining ma'lumotlari"""
			user_id = response.json()['short'][0]['id']
			user_name = response.json()['short'][0]['name']
			user_status = response.json()['short'][0]['tavsiya']
			user_info=(f" 🔰 {user_name} \n\n "
					   f"🆔 {user_id} \n\n"
					   f" 🗣 {user_status}")


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
				   f'________________________\n\n'
				   f'{block_answer}\n'
					f"📌 Umumiy ball-{response.json()['imtiyoz'][0]['Umumiyball']}\n"
					f'________________________\n\n'
					f'{answers}')

		elif response.json()['short'][0]['tavsiya'] == '<i>Неоцененный!</i>' and not(response.json()['block'][0]['block']):

			"""Foydalanuvchining ma'lumotlari"""
			user_id = response.json()['short'][0]['id']
			user_name = response.json()['short'][0]['name']
			user_info = (f" 🔰 {user_name} \n\n"
						 f"🆔 {user_id} \n\n")


			"""Savollarning qaysi biriga to'g'ri yoki noto'g'ri ekanni chiqaradi"""
			lens = len(response.json()['answers'])
			answers = []
			for i in range(0, lens):
				answers.append(
					f"{i + 1}-{response.json()['answers'][i]['answer']}: {response.json()['answers'][i]['check']}")
			answers = '\n'.join(answers)
			return (f'{user_info}\n'
					f'________________________\n'
					f"📌 Umumiy ball-{response.json()['imtiyoz'][0]['Umumiyball']}\n"
					f'________________________\n\n'
					f'{answers}')


		elif response.json()['short'][0]['tavsiya'] != '<i>Неоцененный!</i>' == response.json()['block'][0]['block']:
			"""Foydalanuvchining ma'lumotlari"""
			user_id = response.json()['short'][0]['id']
			user_name = response.json()['short'][0]['name']
			user_info = (f" 🔰 {user_name} \n\n "
						 f"🆔 {user_id} \n\n")


			"""Savollarning qaysi biriga to'g'ri yoki noto'g'ri ekanni chiqaradi"""
			lens = len(response.json()['answers'])
			answers = []
			for i in range(0, lens):
				answers.append(
					f"{i + 1}-{response.json()['answers'][i]['answer']}: {response.json()['answers'][i]['check']}")
			answers = '\n'.join(answers)
			return (f'{user_info}\n'
					f'________________________\n\n'
					f"📌 Umumiy ball-{response.json()['imtiyoz'][0]['Umumiyball']}\n"
					f'________________________\n\n'
					f'{answers}')



		elif response.json()['short'][0]['tavsiya'] == '<i>Неоцененный!</i>' and not(response.json()['block'][0]['block']):
			"""Foydalanuvchining ma'lumotlari"""
			user_id = response.json()['short'][0]['id']
			user_name = response.json()['short'][0]['name']
			user_info = (f" 🔰 {user_name} \n\n "
						 f"🆔 {user_id}")


			return (f'{user_info}\n\n'
					f'________________________\n\n'
					f"📌 Umumiy ball-{response.json()['imtiyoz'][0]['Umumiyball']}\n"
					f'________________________\n\n')

	except:
		return "Bunday talaba topilmadi"




if __name__ == "__main__":
	url = "https://mandat4.p.rapidapi.com/id"

	querystring = dict(id="1596433")

	headers = {
		"X-RapidAPI-Key": "e1138de0bamshf4bab9b76bb7f1ep16ce46jsn30e66de2587d",
		"X-RapidAPI-Host": "mandat4.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	print(response.json())







