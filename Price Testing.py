import urllib.request

page = urllib.request.urlopen("https://ycharts.com/indicators/world_coffee_arabica_price")

text = page.read().decode("utf8")

where = text.find('USD/kg')

start_of_price = where + -10

end_of_price = start_of_price + 100

#price = float(text[start_of_price:end_of_price])

price = (text[start_of_price:end_of_price])

print(price)

print("Buy!")
