var2 = {"Kitchen":{"Freezer": {"Floor1":"Ice", "Floor2":"Ice Cream"}, "Fridge": {"Floor1":"Berries", "Floor2":"Milk", "Floor3":"Tomatoes and curd", "Floor4":"Vegetables"}}}
print("You are in kitchen, choose b/w Fridge or Freezer")
input = input()
room , device, floor = input.split()
print(var2[room][device][floor])
