import requests
from bs4 import BeautifulSoup as b

hitung = 0
for page in range(1,308): #mentok 308
    url = 'https://yellowpages.co.id/cari/bisnis/hotel/jakarta?page='+str(page)+'&sort='
    headers = {'Referer':'https://yellowpages.co.id/cari/bisnis/hotel/jakarta?'}
    r = requests.get(url, headers=headers)
    soup= b(r.text, 'html.parser')
    results = soup.findAll('div', 'home-list-pop list-spac')

    for re in results:
        nama = re.find('h4').text.strip()
        p = re.findAll('p')
        kategori = p[0].text.strip()
        jalan = p[1].text.strip()
        kota = p[2].text.strip()
        kontak = re.find('div','col-md-4 home-list-pop-desc inn-list-pop-desc').findAll('a')
        if len(kontak) > 1:
            email = kontak[0]['href'].replace('mailto:','').strip()
            web = kontak[1]['href'].replace('https://www.','').replace('http://www.','')\
                .replace('https://','').replace('http://','').split('?')[0].strip()
        elif len(kontak) == 1:
            email = kontak[0]['href'].replace('mailto:', '').strip()
            if '@' in email:
                em = email
            web = 'Tidak Ada'
        else:
            continue

        hitung +=1
        print('Nomor    : ', hitung)
        print('Nama     : ', nama)
        print('Kategori : ', kategori)
        print('Alamat   : ', jalan)
        print('Kota     : ', kota)
        print('E-mail   : ', em)
        print('Website  : ', web, '\n')