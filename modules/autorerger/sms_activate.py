import aiohttp


async def Check_balance(sms_activate_key, account_count):
    async with aiohttp.ClientSession() as session_sms_activate:
        async with session_sms_activate.get(
                f"https://api.sms-activate.org/stubs/handler_api.php?api_key={sms_activate_key}&action=getBalance"
        ) as response:
            try:
                response_balance = await response.text()
                balance_raw = response_balance.split(":")
                balance_str = balance_raw[1].split(".")  # Говнокод моя любовь
                balance = balance_str[0]
            except (IndexError, ValueError):
                print("[-] Ошибка при получении баланса SMS Activate!")
                return False

            print(f"[*] Баланс SMS Activate: {balance} р")

            required_balance = (10 * int(account_count)) - int(balance)

            if int(balance) < 10 * int(required_balance):
                exit(
                    f"[-] Недостаточно средств на балансе SMS Activate! Необходимо пополнить баланс на {required_balance:.2f} рублей."
                )


async def Get_Number(sms_activate_key):
    async with aiohttp.ClientSession() as session_sms_activate:
        async with session_sms_activate.get(
                f"https://sms-activate.org/stubs/handler_api.php?api_key={sms_activate_key}&action=getNumber&service=ot&country=$country=0"
        ) as response:
            response_raw = await response.text()
            actication_id = response_raw.split(":")[1]
            phone_number = response_raw.split(":")[2]
            print(f"[+] Получен номер: +{phone_number}")
            return phone_number, actication_id


async def Set_Status_Active(sms_activate_key, activation_id, phone_number):
    async with aiohttp.ClientSession() as session_sms_activate:
        async with session_sms_activate.get(
                f"https://api.sms-activate.org/stubs/handler_api.php?api_key={sms_activate_key}&action=setStatus&status=1&id={activation_id}"
        ) as response:
            print(f"[+] +{phone_number}: Ожидаю SMS...")


async def Get_Sms(sms_activate_key, activation_id):
    async with aiohttp.ClientSession() as session_sms_activate:
        sms_code = "STATUS_WAIT_CODE"
        while sms_code == "STATUS_WAIT_CODE":
            async with session_sms_activate.get(
                    f"https://api.sms-activate.org/stubs/handler_api.php?api_key={sms_activate_key}&action=getStatus&id={activation_id}"
            ) as response:
                response_raw = await response.text()
                if response_raw == "STATUS_WAIT_CODE":
                    sms_code = "STATUS_WAIT_CODE"
                else:
                    sms_code = response_raw.split(":")[1]

        print(f"[+] Получен код: {sms_code}")
        return sms_code
