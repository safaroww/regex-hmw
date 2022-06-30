import re


#1
# names = ['Aygun Kazimova', 'fermer Həsən', 'Namiq Qaracuxurlu', 'Rehim Rehimli', 'roya Ayxan', 'Eynulla']

# for name in names:
#     match = re.match('[A-Z]', name)
#     match2 = re.search(' [A-Z]', name)
#     if not match and match2:
#         names.remove(name)





#2 ?
# ['14, 6, 2', 'f1, 12, 255', 'a, 54, 1']

# user_num = input("nomreleri girin: ")

# for num in user_num:
#     match = re.findall()



#3
# site = """Dünyada bir çox saytlar mövcuddur. Bunların bir çoxu fərqli məqsədlərə xidmət edirlər. Müsal üçün http://www.google.com saytı axtarış üçün istifadə olunur. Digər yandan https://facebook.com və http://www.instagram.com saytları sosial şəbəkə kimi fəaliyyət göstərirlər"""

# default = 'https?://(www.)?[a-z]+\.[a-z]+'

# sites = re.findall(default, site)


#4
# username ='^[a-z]+(\.?|_)[a-z]+'
# email = '[A-Za-z1-9]+\.[A-Za-z1-9]+@[a-z]+\.[a-z]+'
# password = '\S+'



#5
# phone_num_list = """051-235-642-12, 055-236-642-23, 077-623-234-26, 51-125-646-32, 50-125-542-12, 70-253-644-12, 050-135-346-64"""

# azercell_default = '^0?50|51-\d{3}-\d{3}-\d{2}'
# print(re.findall(azercell_default, phone_num_list))