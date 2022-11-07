
with open("recipe_book", "r", encoding="utf-8") as file:
    cook_book = {}
    cook_book_keys = ["ingredient_name", "quantity", "measure"]
    for line in file:
        dish_name = line.strip()
        counter = int(file.readline())
        dish_ing_list = []
        for _ in range(counter):
            ingr = file.readline().strip().split("|")
            ing_dict = dict(zip(cook_book_keys, ingr))
            dish_ing_list.append(ing_dict)
        file.readline()
        cook_book[dish_name] = dish_ing_list


def get_shop_list_by_dishes(dishes, person_count):
    ingred_list = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            ing_name = ing["ingredient_name"]
            if ing_name not in ingred_list:
                ingred_list[ing_name] = {"quantity": int(ing["quantity"]) * person_count, "measure": ing["measure"]}
            else:
                ingred_list[ing_name]["quantity"] += int(ing["quantity"]) * person_count
    return ingred_list

print("============= Задание № 1 =============")
print(cook_book)
print("============= Задание № 2 =============")
print(get_shop_list_by_dishes(["Омлет", "Фахитос"], 3))