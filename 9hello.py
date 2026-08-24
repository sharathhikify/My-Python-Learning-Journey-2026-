karnataka_food={"shivamogga": "akki rotti",
                "haveri": "jolada rotti",
                "uttara kannada":"dosa"}

print(karnataka_food["shivamogga"]) #accessing dictionary

karnataka_food["banglore"]="bisi bele bath" #updating dictionary
print(karnataka_food)

karnataka_food["banglore"]="idli"#updating item
print(karnataka_food)

karnataka_food.pop("banglore") #removing item
print(karnataka_food)

print(karnataka_food.get("banglore")) #accessing item which is not present in dictionary

print(karnataka_food.keys()) #accessing keys of dictionary

print(karnataka_food.values()) #accessing values of dictionary

new_dishes={"mysore":"mysore pak"}
karnataka_food.update(new_dishes)
print(karnataka_food)