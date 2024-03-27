import random
def gen(clave):
    cont = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    contra = "".join(random.choice(cont) for i in range(clave))
    print("La clave generada es:", contra)
    return contra
clavea= int(input("Longitud clave: "))
claveb= gen(clavea)
