#nomor 4
def bilangan(angka):
    for i in range(1,angka):
        if i % 2 !=0:
            print(i, end=", ")

bilangan(20)
print()

#nomor 3
def nilai(n = 0):
    if n <= 60:
        print (f"nilai {n} tidak lulus")
    elif n > 60 and n <= 100:
        print(f"nilai {n} lulus")
    else:
        print(f"nilai {n} tidak diketahui")

nilai(80)
nilai()

print()


#nomor 2
def is_genap(n):
    return n % 2 == 0
print(is_genap (2))

#nomor 1
def celsius_ke_fahrenheit(c):
    return (c * 9/5) + 54

print(celsius_ke_fahrenheit(0)) 
print(celsius_ke_fahrenheit(100)) 
