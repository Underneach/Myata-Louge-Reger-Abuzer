import asyncio

from modules.autorerger.autoreger import Registration
from modules.banner import Banner
from modules.autorerger.sms_activate import Check_balance


async def main():
    await Banner()
    account_count, captcha_key, sms_activate_key, promocode_list = await User_Input()
    print("\n[*] Начинаю работу...\n")

    await Check_balance(sms_activate_key, account_count)

    Registration_tasks = []
    for i in range(int(account_count)):
        Registration_tasks.append(Registration(sms_activate_key, captcha_key, promocode_list))

    results = await asyncio.gather(*Registration_tasks)

if __name__ == "__main__":
    asyncio.run(main())
