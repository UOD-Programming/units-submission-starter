import copy

def update_list_item_one(items, x):
  pass

def new_list_item_one(items, x):
  pass

if __name__ == "__main__":
    list_one = [1,2,3,4]
    update_list_item_one(list_one, 0)
    print(list_one) # should print out [0,2,3,4]
    
    list_one = [1,2,3,4]
    new_list_item_one(list_one, 0)
    print(list_one) # should print out [1,2,3,4]
    
    list_one = [1,2,3,4]
    list_one = new_list_item_one(list_one, 0) # bind the new object to l
    print(list_one) # should print out [0,2,3,4]