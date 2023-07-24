import json
from jsonpath_ng import parse
from modules.autorerger.captcha_solver import Captcha_Solver


async def Send_Code(phone_number, captcha_key, sms_code):
    captcha_key = await Captcha_Solver(captcha_key)
    full_phone_number = f"+{phone_number}"
    cut_phone_number = phone_number[1:]
    print(f"[+] {full_phone_number}: Решаю капчу на отправке SMS")

    step_error = "true"
    while step_error != "true":
        json_data = {"phone": f"{cut_phone_number}",
                     "full_phone": f"{full_phone_number}",
                     "locale": "RU",
                     "code": f"{sms_code}",
                     "captcha": f"{captcha_key}",
                     }

        async with session.post("https://api.myataofficial.com/v6/auth/token", json=json_data) as response:
            step_error = await response.json()["error"]

            data_dict = await json.loads(str(response.json))
            # Определение JPATP
            jsonpath_expr = parse('$.data.auth')
            # Использование JPATP для получения значения
            matches = [match.value for match in jsonpath_expr.find(data_dict)]
            # Печать результата
            auth_token = matches[0]
            print(f"[+] {full_phone_number}: получен токен авторизации: {auth_token}")
            # сохранить все куки в переменную
            return auth_token
