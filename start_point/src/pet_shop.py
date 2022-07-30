def get_pet_shop_name(petshop):
    return petshop["name"]


def get_total_cash(petshop):
    return petshop["admin"]["total_cash"]


def add_or_remove_cash(petshop, cash_amount):
    petshop["admin"]["total_cash"] += cash_amount


def get_pets_sold(petshop):
    return petshop["admin"]["pets_sold"]


def increase_pets_sold(petshop, number_of_pets_sold):
    petshop["admin"]["pets_sold"] += number_of_pets_sold


def get_stock_count(petshop):
    return len(petshop["pets"])


def get_pets_by_breed(petshop, breed_type):
    found_breeds = []
    for pet in petshop["pets"]:
        if pet["breed"] == breed_type:
            found_breeds.append(pet)
    return found_breeds


def find_pet_by_name(petshop, name):
    for pet in petshop["pets"]:
        if name == pet["name"]:
            return pet


def remove_pet_by_name(petshop, pet_name):
    pet_to_remove = []
    for pet in petshop["pets"]:
        if pet["name"] == pet_name:
            pet_to_remove = pet

    petshop["pets"].remove(pet_to_remove)


def add_pet_to_stock(petshop, new_pet):
    petshop["pets"].append(new_pet)
    return len(petshop["pets"])


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(customer, amount):
    customer["cash"] -= amount


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return len(customer["pets"])


def customer_can_afford_pet(customer, new_pet):
    return customer["cash"] >= new_pet["price"]


def is_pet_in_stock(petshop, pet_bought):
    return pet_bought in petshop["pets"]


def sell_pet_to_customer(petshop, pet_bought, customer):
    if is_pet_in_stock(petshop, pet_bought) and customer_can_afford_pet(customer, pet_bought):
        # remove customer cash
        # customer["cash"] -= pet_bought["price"]
        remove_customer_cash(customer, pet_bought["price"])
        # add cash to till
        #petshop["admin"]["total_cash"] += pet_bought["price"]
        add_or_remove_cash(petshop, pet_bought["price"])
        # remove Arthur from petshop stock
        # doesn't work - remove_pet_by_name(petshop, pet_bought)
        # add arthur to customer
        add_pet_to_customer(customer, pet_bought)
        # customer["pets"].append(pet_bought)
        # increase pets sold
        # could you do len here?
        increase_pets_sold(petshop, 1)
        #petshop["admin"]["pets_sold"] += 1


# def remove_pet_by_name(petshop_name, pet_name):
#     for animal in petshop_name["pets"]:
#         if animal["name"] == pet_name:
#             animal.pop(pet_name)
#         return petshop_name["pets"]

# def remove_pet_by_name(petshop, name):
#     new_list = []
#     for pet in petshop["pets"]:
#         if name != pet["name"]:
#             new_list += pet
#     petshop["pets"] = new_list

    # for pet in petshop["pets"]:
    #     pet.pop(name)
