from typing import Text
import urllib.request

page=urllib.request.urlopen("http://priyadarshanigroupofschools.com/IndrayaniNagar/contact-us/")
Text=page.read().decode("utf8")

Where=Text.find("@gmail.com")

start_of_email=Where-9
end_of_email=start_of_email+20

price=Text[start_of_email:end_of_email]

print(price)