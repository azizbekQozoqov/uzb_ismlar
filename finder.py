import requests
from bs4 import BeautifulSoup
from translate import to_latin

def get_name(name:str):
    name = name.replace("'", "‘")
    data = requests.get(f"https://ismlar.com/uz/name/{name}").text
    soup = BeautifulSoup(data, "html.parser")
    
    try:
        dp = soup.find("div", {'class':"p-4 rounded-2xl mb-4 space-y-4 bg-cyan-100"}) if soup.find("div", {'class':"p-4 rounded-2xl mb-4 space-y-4 bg-cyan-100"}) else soup.find("div", {'class':"p-4 rounded-2xl mb-4 space-y-4 bg-pink-100"})
        meaning = sorted([x.text for x in soup.find("div", {"class": "p-4 rounded-2xl bg-gray-100 my-4 space-y-4"}).div.findChildren("p")], key=len, reverse=True)[0]
    except:
        return {"ok":False,"message":"Ism topilmadi! Yoki qandaydur xatolik yu berdi."}
    name = name.title()

    return {"ok":True, "meaning":to_latin(meaning), "desc":to_latin(dp.find("div", {"class": "space-y-4"}).p.text.strip())} 

def search_name(name):
    name = name.replace("'", "‘")
    all = []
    soup = BeautifulSoup(requests.get(f"https://ismlar.com/uz/search/{name}").text, "html.parser")
    finder = soup.find("ul", {"class": "list-none space-y-2"})
    if not finder:
        return {"ok":False,"message":"Ism topilmadi! Yoki qandaydur xatolik yu berdi."}
    for li in finder.find_all("li"):
        all.append(to_latin((li.find("div", {"class": "space-y-4"}).text.strip()), to_latin(li.h2.text.strip())))

    return all

def get_footer():
    return f"""<i>Yangiliklardan boxabar bo'lish uchun @AzizbekDeveloper sahifasiga obuna bo'ling\n@imloqoida_bot - Imloni tekshiruvchi bot.
    </i>
    """

def get_start_text():
    return f"""<b>Ismlar ma'nosini bilish uchun bot\n\n<i>@AzizbekDeveloper</i>\n\nwww.ismlar.com</b>"""