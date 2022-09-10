# Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
# separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

# se puede hacer co .replace o con .join y .split


name = "Jesu"

print(name.split("s"))

print("_".join(name.split("s")))


cesta = input("introduce los productos de la compra separados por cómas:  ")
print(cesta.replace(",", "\n"))


# otro ejemplo con .join y .split

cesta = input("introduce los productos de la compra separados por cómas:  ")
print("\n".join(cesta.split(",")))
