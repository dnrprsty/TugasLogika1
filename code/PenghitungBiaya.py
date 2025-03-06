def hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, status_member):
    # Biaya dasar pengiriman
    biaya = 10000
    
    # Tambahan biaya jika berat lebih dari 5 kg
    if berat > 5:
        biaya += 5000
    
    # Tambahan biaya jika jarak lebih dari 10 km
    if jarak > 10:
        biaya += 8000
    
    # Tambahan biaya jika memilih pengiriman express
    if jenis_pengiriman == 'express':
        biaya += 20000
    
    # Diskon 10% jika pelanggan adalah member
    if status_member == 'member':
        biaya -= biaya * 0.10
    
    return biaya

# Mengambil input dari pengguna
berat = float(input("Masukkan berat paket (kg): "))
jarak = float(input("Masukkan jarak pengiriman (km): "))
jenis_pengiriman = input("Masukkan jenis pengiriman (biasa/express): ").lower()
status_member = input("Masukkan status keanggotaan (member/non-member): ").lower()

# Menghitung total biaya pengiriman
total_biaya = hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, status_member)

# Menampilkan total biaya pengiriman
print(f"Total biaya pengiriman: Rp {total_biaya}")
