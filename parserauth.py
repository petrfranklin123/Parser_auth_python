from bs4 import BeautifulSoup
import requests

s = requests.Session()

auth_html = s.get('https://smartprogress.do/')
auth_bs = BeautifulSoup(auth_html.content, 'html.parser')
csrf = auth_bs.select('input[name=YII_CSRF_TOKEN]')[0]['value']

print(auth_html.status_code)

payload = {
    'YII_CSRF_TOKEN': csrf,
    'returnUrl': '/',
    'UserLoginForm[email]': 'petr784512@mail.ru',
    'UserLoginForm[password]': 'Gtnh45123',
    'UserLoginForm[rememberMe]': 1
}

asnw = s.post('https://smartprogress.do/user/login/', data = payload)
anw_bs = BeautifulSoup(asnw.content, 'html.parser')



SLOVAR = {
   'Name': anw_bs.find('div', class_='user-menu__name').get_text(strip=True),
   'Lvl': anw_bs.find('div', class_='user-menu__info-text--lvl').get_text(strip=True),
   'XP': anw_bs.find('div', class_='user-menu__info-text--exp').get_text(strip=True)
}
#name = anw_bs.find('div', class_='user-menu__name').get_text(strip=True)
print(f'{SLOVAR["Name"]} {SLOVAR["Lvl"]} {SLOVAR["XP"]}')
#print(name)
#print(' Имя: ' + anw_bs.select('.user-menu__name')[0].text.strip())
#print(' Уровень: ' + anw_bs.select('.user-menu__info-text--lvl')[0].text.strip())
#print(' Опыт: ' + anw_bs.select('.user-menu__info-text--exp')[0].text.strip())