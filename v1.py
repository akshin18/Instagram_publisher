from PIL import Image , ImageDraw, ImageFont
import textwrap
import os

def create_content(photo='images/none.png',text = 'СМИ: TikTok начала борьбу с платной рекламой криптовалют' ):
    sablon = Image.open('images/пост3 (1).png')
    new_img = Image.new('RGBA', (1080, 1080), 'blue')
    sab = Image.open(photo)
    res = sab.resize((1080,845))
    res.save('images/res.png',format='png')
    res = Image.open('images/res.png').convert('RGBA')
    new_img.paste(res,(0,0),res)
    new_img.save('images/last.png',format='png')
    twosaq = Image.open('images/last.png')
    twosaq.paste(sablon,(0,0),sablon)
    twosaq.save('images/finish.png',format='png')
    finish = Image.open('images/finish.png')

    font = ImageFont.truetype("images/PTSans-Bold.ttf", 50, encoding='UTF-8')
    pencil = ImageDraw.Draw(finish)

    container = textwrap.wrap(text, width=30)
    step = 0
    for i in range(1,len(container)+1):
        vord = container[i-1].strip()

        pencil.text((245,870+step),vord,  font=font, fill='white')
        step += 50
    finish.save('images/konec.png',format='png')

def story_reshape():
    sablon = Image.new('RGBA', (1080, 1980), 'black')
    konec= Image.open('images/konec.png')
    sablon.paste(konec,(0,450),konec)
    sablon.save('images/cartez.png', format='png')
