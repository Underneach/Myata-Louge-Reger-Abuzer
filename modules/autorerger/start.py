from modules.autorerger.captcha_solver import Captcha_Solver


async def Start(phone_number, captcha_key):
    captcha_key = await Captcha_Solver(captcha_key)
    full_phone_number = f"+{phone_number}"
    cut_phone_number = phone_number[1:]
    print(f"[+] {full_phone_number}: Решаю капчу на Старте")

    step_error = "true"
    while step_error != "true":
        json_data = {"phone": f"{cut_phone_number}",
                     "full_phone": f"{full_phone_number}",
                     "locale": "RU",
                     "captcha": f"{captcha_key}",
                     "code": null}

        async with session.post("https://api.myataofficial.com/v6/auth/token", json=json_data) as response:
            step_error = await response.json()["error"]
