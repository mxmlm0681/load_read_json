# импортируем json
import json
# Открываем файл
with open("newsafr.json", encoding="utf-8") as f:
    json_data = json.load(f)

# Добавляем в список title
json_list = json_data["rss"]["channel"]["items"]
row_list = []
for row in json_list:
    row_list.append(row["title"])

# делаем список по элементам
lan_list = []
for nam in row_list:
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








