import requests
from bs4 import BeautifulSoup


def getImgs(male=[], female=[]):
    req = []
    for m in male:
        req.append('male[]={}'.format(m))
    for m in female:
        req.append('female[]={}'.format(m))
    req = "&".join(req)

    a = requests.get(
        'https://wizard.worldofballpythons.com/wizard/calculate?' + req)

    soup = BeautifulSoup(a._content, 'html.parser')
    imgs = []
    for img in soup.find_all(class_='card-img-top'):
        src = img.attrs['src']
        if src.find('no-morph-image.jpg') < 0:
            imgs.append(img.attrs['src'])

    return imgs


print(getImgs([2534], [2534]))

# print(print(soup.prettify()))
