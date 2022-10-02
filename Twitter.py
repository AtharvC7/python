def send_to_twitter():
    msg = "This is the text message that will be sent"
    password_manager = urllib.request.HTTPPasswordMgr()
    password_manager.add_password("cC1OoA0GmYNzY0luMVGGEjwN9",
    "http://twitter.com/statuses", "@ChopadeAtharv", "Freefall@123")
    http_handler = urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener = urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params = urllib.parse.urlencode( {'status': msg} )
    resp = urllib.request.urlopen("http://twitter.com/statuses/update.json", params)
    resp.read()