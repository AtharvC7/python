from typing import Text
import urllib.request

page = urllib.request.urlopen("https://priyadarshanigroupofschools.com/contact-us/")

Text = page.read().decode("utf8")

start_point= Text.find("@gmail.com")-15

end_point= start_point+25

print(Text[start_point:end_point])