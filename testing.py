import json
 
customer = {
   "phoneNumber":7116854,
   "idNumber":"A111685",
   "name":"Mariyam Ahmed",
   "email":"marrieee@gmail.com",
   "address":"randomge, k.hulhumale",
   "staus":"Active",
   "plan":"POSTPAID 550",
   "unbillCharges":550.12,
   "outstanding":180.23,
   "dataLeft":"1.65 / 10.00 GB",
   "voiceMinLeft":"25/300 MINS",
   "LBPD":"21st April 2021",
   "LBAP":"550",
   "currNetInUse":"4G",
   "currCellNetConnected":"Hulhumale Hospital Radio Tower"
}

with open('testing.txt', 'w') as out:
    json.dump(customer, out)

data = []
with open('7778695.txt') as f:
    for line in f:
        data.append(json.loads(line))

print(data)
print(data[0]['idNumber'])