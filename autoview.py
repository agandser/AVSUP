import time
import requests
from bs4 import BeautifulSoup
delay = int(input("введите задержку между проверками постов"))
chlink = input("введите ссылку на канал")
keyn = input("введите ключ")
views = int(input("введите количество просмотров"))
chlink = f"{chlink[:12]}/s/{chlink[13:]}"
print(chlink)
def new_post(oldnum, num, keyn, views):
    if num > oldnum:
        oldnum = num
        views = requests.post("https://smmprime.com/api/v2", json =  {
        "key":f"{keyn}",
        "action":"add",
        "quantity":f"{views}",
        "service":"705",
        "link":f"https://t.me/hucciflip/{num}"
    })
        print(views.text)
        if "order" in views.text:
            print(f"успешно накрутили на пост {oldnum}")
        else:
            return "pen"
        return oldnum
    else:
        return oldnum
def collect_data(link):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
    }
    response = requests.get(link, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    num = str(soup.find('link', rel='canonical'))[32:-19]
    num = int(num)
    return num-1

def main():
    oldnum = collect_data(chlink)
    while True:
        num = collect_data(chlink)
        oldnum = new_post(oldnum, num, keyn, views)
        time.sleep(delay)
        if oldnum == "pen":
            break


if __name__ == '__main__':
    main()
