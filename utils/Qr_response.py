from utils.misc.upload_telegraph import photo_link
import requests
from aiogram import types


async def Qr_answer(photo: types.photo_size.PhotoSize) -> str:

    link_photo = photo_link(photo)
    try:
        url = "https://qr-scanner-api.p.rapidapi.com/api/QR/scanimageurl"

        querystring = {"imageUrl": f"{link_photo}"}

        headers = {
        	"X-RapidAPI-Key": "e1138de0bamshf4bab9b76bb7f1ep16ce46jsn30e66de2587d",
        	"X-RapidAPI-Host": "qr-scanner-api.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        try:
            return response.json()['result']
        except:
            return 'Xato'

    except:
        return False

if __name__ =="__main__":
    url = "https://qr-scanner-api.p.rapidapi.com/api/QR/scanimageurl"

    querystring = {"imageUrl": f"http://telegra.ph//file/8f8b3b33df3a498189342.jpg"}

    headers = {
        "X-RapidAPI-Key": "e1138de0bamshf4bab9b76bb7f1ep16ce46jsn30e66de2587d",
        "X-RapidAPI-Host": "qr-scanner-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    print(response.json())