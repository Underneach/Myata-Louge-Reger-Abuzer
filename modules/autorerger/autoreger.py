import aiohttp

from modules.autorerger.apply_codes import Apply_Codes
from modules.autorerger.birthday import Birthday
from modules.autorerger.promocode import Promocode
from modules.autorerger.send_code import Send_Code
from modules.autorerger.sms_activate import Get_Number, Get_Sms
from modules.autorerger.start import Start


async def Registration(sms_activate_key, captcha_key, promocode_list):
    async with aiohttp.ClientSession() as session:
        session.headers.update(
            {'Content-Type': 'application/json',
             'Accept': 'application/json, text/plain, */*',
             'Apploading': 'true',
             'Accept-Encoding': 'gzip, deflate',
             'User-Agent': 'okhttp/4.9.2', }
        )

        phone_number, activation_id = await Get_Number(sms_activate_key)
        # await Set_Status_Active(sms_activate_key, activation_id, phone_number)
        await Start(phone_number, captcha_key)
        await Birthday(phone_number, captcha_key)
        await Promocode(phone_number, captcha_key)
        sms_code = await Get_Sms(sms_activate_key, activation_id)
        auth_token = await Send_Code(phone_number, captcha_key, sms_code)
        await Apply_Codes(promocode_list, auth_token, phone_number)
