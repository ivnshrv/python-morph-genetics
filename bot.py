import json

import requests

from getter import getImgs
from time import sleep

list = {'7 Dollar Ghost': '2947', 'Het 7 Dollar Ghost': '2947h', 'Acid': '4067', 'Agent Orange': '2913', 'Albino': '1',
        'Het Albino': '1h', 'Albino - Faded': '29', 'Het Albino - Faded': '29h', 'Albino - High contrast': '3',
        'Het Albino - High contrast': '3h', 'Alloy': '3853', 'Alpha': '2580', 'Alpine': '3726', 'Het Alpine': '3726h',
        'Amur': '5795', 'Het Amur': '5795h', 'Apricot': '3576', 'Araza': '2817', 'Arctic': '3724', 'Arid': '5121',
        'ARP': '3883', 'Arroyo': '1969', 'Ashen': '2963', 'Asphalt': '2585', 'Atomic': '2395', 'Het Atomic': '2395h',
        'Aurora': '4729', 'Autunm Gloss': '725', 'Het Autunm Gloss': '725h', 'Axanthic': '30', 'Het Axanthic': '30h',
        'Axanthic - Jolliff': '396', 'Het Axanthic - Jolliff': '396h', 'Axanthic - Markus Jayne Line': '508',
        'Het Axanthic - Markus Jayne Line': '508h', 'Axanthic - Snake Keeper Line': '511',
        'Het Axanthic - Snake Keeper Line': '511h', 'Axanthic - VPI Line': '100', 'Het Axanthic - VPI Line': '100h',
        'Bald Gene': '1812', 'Bamboo': '2413', 'Banana Ball': '45', 'Banded': '1115', 'Het Banded': '1115h',
        'Banded - Corey Woods Line': '4221', 'Het Banded - Corey Woods Line': '4221h', 'Banshee111': '6525',
        'Bantah': '5911', 'Bengal': '1068', 'Het Bengal': '1068h', 'BiancaBall': '2988', 'Bingo': '4222',
        'Black Adder': '3010', 'Black Axanthic': '46', 'Het Black Axanthic': '46h', 'Black Belly': '2690',
        'Black Granite': '6551', 'Black Head': '47', 'Black Knight': '1258', 'Black Lace': '4141',
        'Het Black Lace': '4141h', 'Black Opal': '557', 'Black Pastel': '33', 'Black Pastel (Barnhart Line)': '1887',
        'Black Pastel - Liesen Line': '3735', 'Black Pastel VPI Satin-Line': '764', 'Blade': '2118', 'Blaze': '6148',
        'Bling Yellow Belly': '2066', 'Blitz': '1771', 'Blonde Pastel': '48', 'Bongo': '2414',
        'Bourgogne Albino': '2070', 'Het Bourgogne Albino': '2070h', 'Brite Ball': '2375', 'Brown Back': '2426',
        'Bullseye': '5096', 'Bumble Bee Highway': '5619', 'Burgundy Albino': '49', 'Het Burgundy Albino': '49h',
        'Butter': '34', 'Butterscotch Ghost': '398', 'Het Butterscotch Ghost': '398h', 'Café': '3342', 'Cajun': '335',
        'Calico': '35', "Calico - Flora & Fauna's line": '505', 'Calico - NERD Line': '625',
        'Calico - Regiusco Line': '5856', 'Callisto': '2391', 'Candy': '561', 'Het Candy': '561h', 'Cantaloupe': '3574',
        'Caramel Albino': '37', 'Het Caramel Albino': '37h', 'Caramel Albino (Bell Line)': '379',
        'Het Caramel Albino (Bell Line)': '379h', 'Caramel Albino (Crider Line)': '982',
        'Het Caramel Albino (Crider Line)': '982h', 'Caramel Albino (Ralph Davis line)': '1855',
        'Het Caramel Albino (Ralph Davis line)': '1855h', 'Caramel Albino (Upscale Line)': '773',
        'Het Caramel Albino (Upscale Line)': '773h', 'Carnivore': '7957', 'Champagne': '39', 'Charcoal': '3332',
        'Chocolate': '51', 'Chocolate (Bell line)': '1632', 'Chocolate (BHB Line)': '1631', 'Cinder': '4858',
        'Cinnamon': '40', 'Circinus': '4713', 'Citrus Hypo': '2595', 'Het Citrus Hypo': '2595h', 'Citrus Pastel': '470',
        'Clown': '42', 'Het Clown': '42h', 'Cocoa': '7428', 'Coffee': '1825', 'Confusion': '4072', 'Congo': '52',
        'Coral Glow': '53', 'Cos Mojave': '5485', 'Cosmic': '4712', 'Creed': '3978', 'Creme Ball': '3439',
        'Cupid': '2087', 'Cypress': '5113', 'D-Stripe': '5038', 'Het D-Stripe': '5038h', 'Daisy': '1334',
        'Dark Wonder': '3378', 'Het Dark Wonder': '3378h', 'Darkling': '6389', 'Deme Ball': '2249', 'Desert Ball': '55',
        'Desert Ghost': '56', 'Het Desert Ghost': '56h', 'Disco': '1149', 'DnA': '4863', 'Dot': '826', 'Ember': '763',
        'Enchi': '57', 'Enhancer Ball': '1379', 'Het Enhancer Ball': '1379h', 'Enigma': '1961', 'Epic': '457',
        'Exo-LBB': '2856', 'Fader': '693', 'Fire': '58', 'Fire - Lone Star Reptiles Line': '6270',
        'Fire - NERD Line': '549', 'Flame': '1610', 'Flame (Noah Line Calico)': '2466', 'Flare': '1935',
        'Freak': '1210', 'Frenzy': '7571', 'Fuego': '2620', 'Fusion': '5108', 'G1 Hypo': '1519', 'Het G1 Hypo': '1519h',
        'Galaxy': '1554', 'Garcia Chocolate': '1629', 'Genesis': '2993', 'Genetic Banded': '188',
        'Genetic Banded - Pacific Coast Reptiles Line': '2289', 'Genetic Banded - Vesper Line': '2295',
        'Genetic Black Back': '1069', 'Genetic Stripe': '59', 'Het Genetic Stripe': '59h',
        'Genetic Tiger - M&S Line': '2968', 'GeneX': '4786', 'Ghi Ball': '60', 'Ghost': '28', 'Het Ghost': '28h',
        'Glossy': '2865', 'Gobi Ball': '7627', 'Goblin': '61', 'Goldblush': '3939', 'Goldfinger': '329',
        'Gorgon': '7522', 'Granite (Co-Dom)': '62', 'Granite (Dom)': '1636', 'Granite - Snakeguy Line': '1879',
        'Gravel': '1012', 'Green Ghost': '63', 'Het Green Ghost': '63h', 'Grim': '5283', 'Grim Reaper': '5374',
        'Harlequin': '604', 'Harlequin - Amir Line': '1979', 'Hayabusa': '2666', 'Hazel': '4019', 'Het Daddy': '1281',
        'Het Red Axanthic': '65', 'Het Saturn': '1235', 'Het Scimitar': '6925', 'Hidden Gene Woma': '971',
        'High Yellow': '2399', 'Highblush': '4851', 'Honey': '1535', 'HPK': '4216', 'Huffman': '1345',
        'Hurricane': '1893', 'Hydra': '2495', 'Hyper Striper': '66', 'IceFyre': '4505', 'Ivory': '212', 'Java': '1316',
        'Jaxon': '5229', 'Jedi': '1342', 'Jolt': '6550', 'Joppa': '2488', 'Josie Ball': '710', 'Jumanji Ball': '3264',
        'Jungle Woma': '1139', 'Kalabash Reduction Gene': '3744', 'Killer Zebra': '1392', 'Kosmos': '1759',
        'KS Hypo': '6344', 'Het KS Hypo': '6344h', 'Ktulu': '2460', 'Lace': '615', 'Lace Black Back': '64',
        'Latte': '1238', 'Lattice': '4898', 'Lavender Albino': '68', 'Het Lavender Albino': '68h',
        'LC Black Magic': '2440', 'LC Black Magic Super': '2441', 'Lemon Pastel': '69', 'Lemonback': '531',
        'Leopard Ball': '382', 'Lesser': '70', 'Lightning Ball': '4114', 'Lilly': '71', 'Lori': '72', 'Lucifer': '1455',
        'Luminoso': '2889', 'Magenta': '6397', 'Mahogany': '416', 'Majestic': '3570', 'Maker': '4359', 'Mako': '2578',
        'Malum': '5854', 'Mandarin': '2403', 'Mandarin Pastel': '233', 'Mango Ball': '4145', 'Mario': '3407',
        'Mathew': '3786', 'Mckenzie': '7965', 'Microscale': '7948', 'Milk Chocolate': '1692', 'Mocha': '1237',
        'Mojave': '73', 'Monarch': '2126', 'Het Monarch': '2126h', 'Monsoon': '5694', 'Het Monsoon': '5694h',
        'Mota': '1818', 'Mystic': '512', 'Nanny Ball': '2744', 'Napalm': '74', 'Nazca': '1643', 'Nebula': '4289',
        'Nemo': '3350', 'Nova': '797', 'NR Mandarin': '5118', 'Nyala': '3315', 'Ofy': '2898', 'Omega': '7054',
        'Orange Belly': '1127', 'Orange Crush': '595', 'Het Orange Crush': '595h', 'Orange Dream': '76',
        'Orange Ghost': '77', 'Het Orange Ghost': '77h', 'Orange Glow': '509', 'Orbit': '1723', 'Paint Ball': '1102',
        'Panther TII': '2290', 'Paragon': '342', 'Het Paragon': '342h', 'Pastel': '32', 'Pastel - Bell Line': '78',
        'Pastel - Graziani': '79', 'Pastel - Morton Wright Line': '80', 'Patternless': '81', 'Het Patternless': '81h',
        'Pearl': '973', 'PG': '4130', 'Phantom': '82', 'Phantom #2': '2103', 'Piebald': '83', 'Het Piebald': '83h',
        'Pinstripe': '84', 'Power Ball': '1101', 'Puzzle Back': '1140', 'Puzzle Ball': '434', 'Het Puzzle Ball': '434h',
        'Quake': '2308', 'Radioactive': '2769', 'Rainbow': '4600', 'Het Rainbow': '4600h', 'Raven': '2770',
        'Reaper': '485', 'Red Axanthic': '107', 'Red Gene': '4260', 'Red Stripe': '499', 'Redhead': '3324',
        'Rio': '1970', 'Ruppel Pastel': '86', 'Russo Het Leucistic': '1205', 'Russo Leucistic': '1206', 'Sable': '88',
        'Safari': '1320', 'Sahara': '2419', 'Het Sahara': '2419h', 'Sandblast': '4413', 'Sapphire': '4444',
        'Satin': '2142', 'Saturn': '1236', 'Sauce': '3962', 'Scaleless': '2909', 'Scaleless Head': '2906',
        'Scimitar': '6938', 'Sentinel': '2650', 'Het Sentinel': '2650h', 'Shatter': '89', 'Shinobi': '4271',
        'Shiraz': '7659', 'Shrapnel': '3919', 'Shredder': '3312', 'Sienna': '2973', 'Sierra': '2994', 'Sirius': '4496',
        'Solar Ball': '1026', 'Solar Flare': '1936', 'Spark': '680', 'Sparkler': '4511', 'Special': '388',
        'Speckled': '612', 'Specter': '90', 'Spider': '91', 'Splash': '2423', 'Splatter': '1931', 'Spotnose': '1100',
        'Static': '1677', 'Storm': '7955', 'Stranger': '3399', 'Stretcher SNA': '3833', 'Sugar': '93',
        'Sugar - BHB Line': '2010', 'Sulfur': '94', 'Suma': '474', 'Sunkist': '2903', 'Sunrise': '6712',
        'Sunset Ball': '296', 'Het Sunset Ball': '296h', 'Super Alloy': '3854', 'Super Alpha': '2581',
        'Super Arctic': '3725', 'Super Asphalt': '7266', 'Super Banana': '1114', 'Super Black Head': '207',
        'Super Black Opal': '558', 'Super Black Pastel': '111', 'Super Blade': '2119',
        'Super Bling Yellow Belly': '2067', 'Super Blonde Pastel': '1538', 'Super Bongo': '2415',
        'Super Brown Back': '2427', 'Super Butter': '231', 'Super Cajun': '50', 'Super Callisto': '2392',
        'Super Champagne': '1669', 'Super Charcoal': '3333', 'Super Chocolate': '152',
        'Super Chocolate (Bell line)': '1634', 'Super Chocolate (BHB Line)': '1633', 'Super Cinnamon': '41',
        'Super Citrus Pastel': '991', 'Super Coral Glow': '1960', 'Super Cypress': '5116', 'Super Darkling': '6390',
        'Super Disco': '1150', 'Super Dot': '3349', 'Super Ember': '1529', 'Super Enchi': '298',
        'Super Exo-LBB': '3251', 'Super Fader': '3102', 'Super Fire': '128', 'Super Flame': '1611',
        'Super Frenzy': '7572', 'Super Fusion': '5109', 'Super Garcia Chocolate': '1630',
        'Super Genetic Banded': '4981', 'Super Genetic Tiger - M&S Line': '2969', 'Super Ghi Ball': '545',
        'Super Glossy': '2866', 'Super Goblin': '1574', 'Super Granite': '643', 'Super Gravel': '2205',
        'Super Green Pastel': '1129', 'Super Honey': '1536', 'Super Huffman': '1346', 'Super Hydra': '2496',
        'Super Java': '2534', 'Super Jedi': '3272', 'Super Lemon Pastel': '300', 'Super Lemonback': '532',
        'Super Lesser': '230', 'Super Lori': '1406', 'Super Luminoso': '4333', 'Super Mario': '5666',
        'Super Mathew': '3788', 'Super Mckenzie': '7966', 'Super Mojave': '229', 'Super Mota': '3931',
        'Super Mystic': '513', 'Super Nazca': '1644', 'Super Orange Belly': '2281', 'Super Orange Dream': '1383',
        'Super Orbit': '4846', 'Super Paint Ball': '1103', 'Super Panther TII': '2292', 'Super Pastel': '112',
        'Super Phantom': '307', 'Super Quake': '2313', 'Super Red Stripe': '722', 'Super Reduced Pattern': '608',
        'Super Ruppel Pastel': '3654', 'Super Sable': '309', 'Super Satin': '2143', 'Super Sauce': '3964',
        'Super Shredder': '3313', 'Super Spark': '1543', 'Super Special': '389', 'Super Speckled': '613',
        'Super Specter': '1648', 'Super Splatter': '1932', 'Super Storm': '7958', 'Super Sulfur': '1143',
        'Super Taronja': '2932', 'Super Vanilla': '312', 'Super Vanilla - Freek Nuyt Line': '3782',
        'Super X-treme Gene': '1483', 'Super Z': '3792', 'Tango': '7713', 'Taronja': '2931', 'Terra': '3566',
        'The 401 Ball': '2586', 'The Matriarch': '4976', 'Het The Matriarch': '4976h', 'Thunder Ball': '4113',
        'TimeBomb': '6399', 'Toffee': '806', 'Het Toffee': '806h', 'Toxique': '3815', 'Tri-Stripe': '97',
        'Het Tri-Stripe': '97h', 'Tri-Stripe (Bloodlines lineage)': '1846',
        'Het Tri-Stripe (Bloodlines lineage)': '1846h', 'Tri-Stripe (Maddox Line)': '2565',
        'Het Tri-Stripe (Maddox Line)': '2565h', 'Trick': '1359', 'Trident': '4115', 'Turbo': '4982', 'Twister': '1881',
        'Ultramelanistic': '98', 'Het Ultramelanistic': '98h', 'Vanilla': '99', 'Vanilla - Freek Nuyt Line': '3526',
        'Vega': '4035', 'Vortex': '3414', 'Web': '2515', 'Whirlwind': '5596', 'White Lace': '616', 'Whiteout': '1396',
        'Whitewash': '6676', 'Het Whitewash': '6676h', 'WHS line Scaleless Head': '3461', 'Wilbanks Granite': '2511',
        'Woma': '970', 'Wookie': '5392', 'X-treme Gene': '1480', 'Yellow Belly': '20', 'Yellow Ghost': '15',
        'Het Yellow Ghost': '15h', 'Yoda Ball': '3274', 'Z': '3790', 'Zebra Pastel': '323', 'Het Zebra Pastel': '323h'}

names = [name for name in list]

# print('\n'.join(names))
f = open('names.txt', 'w')
f.write('\n'.join(names))
f.close()


def url(urlpath):
  return 'https://api.telegram.org/bot***/' + urlpath


chats = {}


def setInterval(func, ms=1000):
  func()
  sleep(ms / 1000)
  setInterval(func, ms)


f = open('./data.json', 'r+')

chats = json.load(f)


def getUpdate():
  data = requests.get(url('getUpdates')).json()
  for res in data['result']:
    if not ('message' in res):
      continue
    id = res['message']['chat']['id']
    date = res['message']['date']
    text = res['message']['text']

    if not (id in chats):
      chats[id] = {
        'date': date,
        'text': text,
        'isNew': 1
      }
    else:
      if date > chats[id]['date']:
        chats[id] = {
          'date': date,
          'text': text,
          'isNew': 1
        }
  for chatId in chats:
    if chats[chatId]['isNew']:
      chats[chatId]['isNew'] = 0
      if text == '/help' or text == '/start':
        requests.get(url('sendMessage?chat_id={}&text={}'.format(id,
                                                                 "Добрый день! Для выполнения запроса пришлите данные в формате M Морф1, Морф2 F Морф3, Морф4. M и F обозначают пол. Бот принимает любое количествро морфов. Список наших морфов: https://pastebin.com/mE1tJw1T")))
      else:
        fIndex = chats[chatId]['text'].find(' F ')
        # M mName, mName2 F fName1, fName2
        females = chats[chatId]['text'][fIndex + 3:].split(',')
        males = chats[chatId]['text'][2:fIndex].split(',')
        l = max(len(females), len(males))
        goodF = []
        goodM = []
        for name in females:
          name = name.strip()

          if name in list:
            goodF.append(list[name])
        for name in males:
          name = name.strip()
          print('m', name)
          if name in list:
            goodM.append(list[name])

        images = getImgs(goodM, goodF)
        if len(goodM) + len(goodF) > 0:
          goodLinks = []
          for link in images:
            if link[-1] != '/':
              goodLinks.append(link)
          print('-->', goodM, goodF, 'goodLinks', goodLinks)
          for photo in goodLinks:
            r = requests.get(url('sendPhoto?chat_id={}&photo={}'.format(chatId, photo)))
          else:
            r = requests.get(url('sendMessage?chat_id={}&text={}'.format(chatId,
                                                                         "Это все имеющиеся фотографии. Если ничего не пришло - значит данное фото отсутствует в базе")))
          print(chats[chatId]['text'], chats)
        f = open('./data.json', 'w+')
        json.dump(chats, f, ensure_ascii=False)


def init():
  getUpdate()


setInterval(init)

# print(names)
# print(list['7 Dollar Ghost'])
# # print(getImgs(['2947', '4067'], ['29h', '29']))time
