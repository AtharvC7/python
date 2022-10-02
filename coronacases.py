import urllib.request

page= urllib.request.urlopen("https://www.nytimes.com/interactive/2021/us/covid-cases.html")

text= page.read().decode("utf8")

start_point= text.find("New reported cases")

end_point= text.find("New reported cases")+10

print(text[start_point:end_point])

