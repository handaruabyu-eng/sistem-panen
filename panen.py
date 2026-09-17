def hitung_total(jumlah, harga):
    return jumlah * harga


def hitung_diskon(total, persentase):
    return total * persentase / 100


jumlah = 100
harga = 5000

total = hitung_total(jumlah, harga)
diskon = hitung_diskon(total, 10)
total_setelah_diskon = total - diskon

print("Jumlah hasil panen:", jumlah, "kg")
print("Harga per kg: Rp", harga)
print("Total hasil panen: Rp", total)
print("Diskon: Rp", diskon)
print("Total setelah diskon: Rp", total_setelah_diskon)
