import database

database.delete_database()

dishtypes = ["appetizer","meat","fish","dessert"]
fish_names = ["Slashed Sea Bass with Red Onions and Mushrooms","Slashed tuna with Green Onions and potatoes","Grilled fish with mashed potatoes","Slashed swordfish with Red and Green Onions"]
dessert_names = ["Lemon Cupcakes","Coconut-Lime Cheesecake","Five-Star Chocolate Cheesecakes","Tiramisu"]
meat_names = ["Beef Tenderloin","Pork Tenderloin with Green onion","Beef steak with potatoes","Lasagna"]
apetizzer_names = ["Octopus to the party","Spanish Omelette","Calamary to the Roman","Corageous Potatoes"]

dishes_first_letter = ["a","m","f","d"]
dishes_array =[apetizzer_names,meat_names,fish_names,dessert_names]



for j in range (0,4):
    for i in range(0,4):
        name = dishes_array[j][i]
        price = 15
        url = "/images/food/dishes/" + dishes_first_letter[j] + str(i) +".jpg"
        description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent leo tellus, aliquet quis blandit eget, ultricies quis purus. Aliquam eu fermentum metus. Maecenas accumsan, felis vel rhoncus tempus, erat ligula dignissim sem, id hendrerit urna turpis et nunc. "
        type = dishtypes[j]


        database.new_dish(name,price,url,description,type)

name = "Menu: I'm not fat"
price = 32
description = "Why are you looking at me?, I'm not fat."
dishes = []
dishes.append(database.get_dish_by_name(apetizzer_names[0]))
dishes.append(database.get_dish_by_name(meat_names[0]))
dishes.append(database.get_dish_by_name(dessert_names[0]))

database.new_menu(name,price,dishes,description)

name = "Menu Nom Nom Nom"
price = 32
description = "Mmmmmm... Tasty."
dishes = []
dishes.append(database.get_dish_by_name(apetizzer_names[1]))
dishes.append(database.get_dish_by_name(fish_names[2]))
dishes.append(database.get_dish_by_name(dessert_names[3]))

database.new_menu(name,price,dishes,description)

database.new_user("daniel","jesucristo")

