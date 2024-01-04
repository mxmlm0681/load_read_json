import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")

tree = ET.parse("newsafr.xml", parser)
print(tree)

root = tree.getroot()
title_list =[]
titles_list = root.findall("channel/item/title")
for title in titles_list:
    print(title.text)
    title_list.append(title.text)

# делаем список по элементам
lan_list = []
for nam in title_list:
    word = nam.split()
    lan_list.extend(word)

# Создадим список из слов в котором более 6 букв
six_word = []
count = 6
for lan in lan_list:
    if len(lan) > count:
        #print(lan)
        six_word.append(lan)

# Создадим уникальные слова
uniq_word = set()
for uniq in six_word:
    uniq_word |= set(six_word)

# Узнаем популярные слова
popular_word = []
for word in uniq_word:
    popular_word.append([word, six_word.count(word)])
# Отсортируем
popular_word.sort(key=lambda x:x[1], reverse=True)

# Определяем топ-10
top_10 = [(f"{popular_word[0]}: {popular_word[1]}") for popular_word in popular_word]
print(",".join(top_10[0:10]))