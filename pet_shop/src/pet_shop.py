# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
     return pet_shop['name']

def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

def add_or_remove_cash(pet_shop, amount):
    pet_shop['admin']['total_cash'] += amount

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop, new_pets_sold):
    pet_shop['admin']['pets_sold'] += new_pets_sold

def get_stock_count(pet_shop):
    pets_stock = 0
    for pet in pet_shop['pets']: 
        pets_stock += 1
    return pets_stock

def get_pets_by_breed(pet_shop, breed_type):
    pet_list = pet_shop['pets'][:]
    breed_list = []
    for pet in pet_list:
        if pet['breed'] == breed_type:
            breed_list.append(pet['name'])
    return breed_list

def find_pet_by_name(pet_shop, pet_name):
    pet_list = pet_shop['pets'][:]
    for pet in pet_list:
        if pet['name'] == pet_name:
            return(pet)

# Last Git Commit 

# Test Not Passing - Have added else and it is printing not found but tese showing Pet... is Not None
def remove_pet_by_name(pet_shop, pet_name):
    pet_list = pet_shop['pets'][:]
    for pet in pet_list:
        if pet['name'] == pet_name:
            remove_index = (pet_list.index(pet))
            del pet_list[remove_index]
            pet_list = pet_shop['pets'][:]
            for pet in pet_list:
                if pet['name'] == pet_name:
                    print('found pet: ', pet)
                else:
                    print('Not Found') 
                return pet             

# Test Not Passing - Stock being returned as 7 but test says 7 != 6
def add_pet_to_stock(pet_shop, new_pet):
    pet_list = pet_shop['pets'][:]
    pet_list.append(new_pet)
    print(pet_list)
    stock = 0
    for pet in pet_list:
        stock = stock + 1
        print(pet, stock)
    print(stock)
    return stock

def get_customer_cash(customers):
    cash = customers['cash']
    return cash

def remove_customer_cash(customers, amount):
    customers['cash'] = customers['cash'] - amount 

def get_customer_pet_count(customers):
    customer_pets = customers['pets'][:]
    count = 0
    for pet in customer_pets:
        count = count + 1
    return count

# Test Not Passing - but suspect that this is for the same reason as the simlar one I was having trouble with above.
def add_pet_to_customer(customers, new_pet):
    customer_pets = customers['pets'][:].append(new_pet)
    return customer_pets


# Optional

def customer_can_afford_pet(customers, new_pet):
    new_pet_price = new_pet['price']
    cash = customers['cash']
    if cash >= new_pet_price:
        return True
    else:
        return False

