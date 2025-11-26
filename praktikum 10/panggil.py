import bangunruang as br
import bangundatar as bd

print("======= BANGUN RUANG =======")
print(f"volum kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"volum balok adalah {br.balok(4, 5, 2)}")
print(f"volum prisma segitiga adalah {br.prisma(5, 4, 5)}")
print(f"volum tabung adalah {br.tabung(7, 17)}")
print(f"volum kerucut adalah {br.kerucut(7, 18)}")

print("======= BANGUN DATAR =======")
print(f"Luas Persegi adalah {bd.persegi(7)}")
print(f"Luas Persegi Panjang adalah {bd. persegi_panjang(9,6)}")
print(f"Luas Segitiga adalah {bd.segitiga(21,5)}")
print(f"Luas Lingkaran adalah {bd.lingkaran(8)}")
print(f"Luas JajarGanjar adalah {bd.jajarGanjar(4,7)}") 

