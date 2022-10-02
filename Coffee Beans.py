import urllib.request

page = urllib.request.urlopen("https://www.thespruceeats.com/how-much-is-starbucks-coffee-766065")

Amey = urllib.request.urlopen("https://www.usatoday.com/story/money/2019/03/02/coffee-price-cost-regular-cappuccino-around-world/38920143/")

text = page.read().decode("utf8")

Captain = Amey.read().decode("utf8") 

start_point= text.find("$")

end_point= text.find("$")+5

print(text[start_point:end_point])

first= Captain.find("$")

end= Captain.find("$")+5

print(text[first:end]) 