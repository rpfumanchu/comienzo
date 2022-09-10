def num_euro():
    import random
    print("Tus números son: ")
    for i in range(5):
        print(f"**\t{random.randrange(1, 50, 1)}")
    
    print("y tus estrellas:")
    for j in range(2):
        print(f"**\t {random.randrange(0, 12, 1)}")
num_euro()