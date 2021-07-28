import time

import requests
from bs4 import BeautifulSoup as bs
import sqlite3

from instabot import Bot


from v1 import create_content
from selen.selen import instapublisher



def parse(a):
    r = requests.get(a)
    soup = bs(r.content,'lxml')
    texts = '\n'.join([i.text for i in soup.find('div',class_='post_content').find_all('p')[:-1]])
    return texts


def Compare_links(con,cur,name,pub):
    r = requests.get(name)

    soup = bs(r.content,'lxml')

    a = soup.find('div',class_='category_page_grid').find('div').find('a')
    img = a.find('div')['style'].split('(')[1][:-1]
    title = a.find('p').text


    if cur.execute(f'''select link from links where name = '{name}' ''').fetchall()[0][0] != a['href']:
        print(img, title)
        parss = parse(a['href'])
        if img != '':
            with open('images/photo.'+img.split('.')[-1],'wb')as f:
                f.write(requests.get(img).content)
            create_content(photo='images/photo.'+img.split('.')[-1],text=title)
        else:
            create_content(photo='images/none.png',text=title)

        pub.publish(texto=parss)

        cur.execute(f'''update links set link='{a['href']}' where name='{name}' ''')
        con.commit()
        print('vso')
    else:
        print('uje net')
        return






def create_db():
    con = sqlite3.connect('link.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS links (
        name text,
        link text
        ); ''')
    con.commit()
    return con,cur
def main():

    con,cur = create_db()
    pub = instapublisher()
    while True:
        for name in cur.execute('select name from links').fetchall()[0]:

                Compare_links(con,cur,name,pub)
                time.sleep(300)

if __name__ == '__main__':
    main()