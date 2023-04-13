ACL = int(input("Ingrese la ACL numerada: "))

if 99 >= ACL >= 1 or 1300 >= ACL >=1999:
    print("El valor ", ACL,  "corresponde a una ACL estándar")
elif 199 >= ACL >= 100 or 2699 >= ACL >=2000:
    print("El valor ", ACL,  "corresponde a una ACL extendida")
else:
    print("El valor ", ACL,  "no corresponde a una ACL numerada")