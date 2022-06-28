import re
def getChatset(page):
    return re.search(r'charset="(?P<charset>.*?)"',page).group("charset")


