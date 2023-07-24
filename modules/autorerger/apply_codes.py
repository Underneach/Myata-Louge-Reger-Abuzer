async def Apply_Codes(promocode_list, auth_token, phone_number):
    session.headers.update({'Authorization': f'Bearer: {auth_token}'})

    for code in promocode_list:
        json_data = {"code": f"{code}"}
        async with session.post("https://api.myataofficial.com/v6/promo-code/index", json=json_data) as response:
            print(await response.json())
            print(f"[+] +{phone_number}: Промокод {code} успешно активирован")
