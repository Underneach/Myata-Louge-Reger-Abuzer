import aiofiles


async def Save_Result(phone_number, auth_token):
    async with aiofiles.open('result.txt', mode='a') as file:
        await file.write(f"{phone_number}:{auth_token}\n")
        await file.close()
