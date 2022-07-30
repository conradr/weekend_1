from ssl import PEM_cert_to_DER_cert


customers = [
    {
        "name": "Alice",
                "pets": [],
                "cash": 1000
    },
    {
        "name": "Bob",
                "pets": [],
                "cash": 50
    },
    {
        "name": "Jack",
                "pets": [],
                "cash": 100
    }
]

new_pet = {
    "name": "Bors the Younger",
    "pet_type": "cat",
    "breed": "Cornish Rex",
    "price": 100
}

cc_pet_shop = {
    "pets": [
        {
            "name": "Sir Percy",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "King Bagdemagus",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "Sir Lancelot",
            "pet_type": "dog",
            "breed": "Pomsky",
            "price": 1000,
        },
        {
            "name": "Arthur",
            "pet_type": "dog",
            "breed": "Husky",
            "price": 900,
        },
        {
            "name": "Tristan",
            "pet_type": "cat",
            "breed": "Basset Hound",
            "price": 800,
        },
        {
            "name": "Merlin",
            "pet_type": "cat",
            "breed": "Egyptian Mau",
            "price": 1500,
        }
    ],
    "admin": {
        "total_cash": 1000,
        "pets_sold": 0,
    },
    "name": "Camelot of Pets"
}


# def remove_pet_by_name(petshop, name):
#    petshop["pets"].pop(name)


#remove_pet_by_name(cc_pet_shop, "Arthur")
# print(cc_pet_shop)
cc_pet_shop["pets"].pop(1)
print(cc_pet_shop)
