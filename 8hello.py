national_festival={"jan 26": "ganaraajyotsava",
                    "aug 15" :"ndipendence day",
                   "jan 1" : "kannada raajyotsava"}

print(national_festival.get("aug 25"))
national_festival["aug 17"]="panhcami"
print(national_festival)
national_festival["jan 1"]="karnataka raajyotsava"
print(national_festival)
national_festival.pop("jan 1")
print(national_festival)