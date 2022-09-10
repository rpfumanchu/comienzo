def num_primitiva():

    import random
    print("Tus números son: ")
    for i in range(6):
        print(f"**\t{random.randrange(1, 49, 1)}") 
    for j in range(1):
        print("Y el complementario es:")
        print(f"**\t{random.randrange(0, 9, 1)}")
num_primitiva()