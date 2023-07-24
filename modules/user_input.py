async def User_Input():
    account_count = None
    captcha_key = None
    sms_activate_key = None
    promocode_list = None

    while account_count is None or not account_count.isdigit():
        account_count = input("Введите количество аккаунтов (целое число): ")

    while captcha_key is None or captcha_key.strip() == "":
        captcha_key = input("Введите API ключ Captcha Guru: ")

    while sms_activate_key is None or sms_activate_key.strip() == "":
        sms_activate_key = input("Введите API ключ SMS Activate: ")

    while promocode_list is None or promocode_list.strip() == "":
        promocode_list = input("Введите список промокодов через запятую: ")

    return int(account_count), captcha_key, sms_activate_key
