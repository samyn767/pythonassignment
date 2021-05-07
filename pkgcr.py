import json
 
pkg = {
   "name":"POSTPAID 1700",
   "data":"50 GB",
   "freemin":"Free calls to all Dhiraagu Numbers, 300 minutes to loacl networks",
   "sms":"Free SMS",
   "intd":"50% off IDD to 3 Countries",
   "freeSocial":"WhatsApp, Viber, Instagram, Facebook, Snapchat",
   "freeapps":"Dhiraagu, BML, Salat, QeueBee",
   "price":"MVR 1700 / Month",
}

with open('PKG-POST1700.json', 'w') as out:
    json.dump(pkg, out)

data = []
with open('PKG-POST1700.json') as f:
    for line in f:
        data.append(json.loads(line))

print(data)
print(data[0]['name'])