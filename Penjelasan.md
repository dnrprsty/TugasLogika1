# Program Penghitungan Biaya Pengiriman

Program ini digunakan untuk menghitung total biaya pengiriman dengan mempertimbangkan beberapa faktor, seperti berat paket, jarak pengiriman, jenis pengiriman, dan status keanggotaan pelanggan. Di bawah ini adalah penjelasan tentang cara kerja program secara rinci.

---

## 1. **Fungsi `hitung_biaya_pengiriman`**

Fungsi utama dalam program ini adalah `hitung_biaya_pengiriman`. Fungsi ini menghitung total biaya pengiriman berdasarkan parameter yang diberikan oleh pengguna. Berikut adalah penjelasan dari setiap parameter dan langkah-langkah penghitungan biaya.

### Parameter Fungsi:
- **`berat`**: Berat paket dalam satuan kilogram (kg).
- **`jarak`**: Jarak pengiriman dalam satuan kilometer (km).
- **`jenis_pengiriman`**: Jenis pengiriman yang dipilih, bisa berupa `biasa` atau `express`.
- **`status_member`**: Status keanggotaan pelanggan, yaitu apakah `member` atau `non-member`.

### Langkah-langkah Perhitungan:
1. **Biaya Dasar**: Setiap pengiriman dikenakan biaya dasar sebesar **Rp 10.000**.
2. **Tambahan Biaya**:
   - Jika berat paket melebihi **5 kg**, dikenakan biaya tambahan sebesar **Rp 5.000**.
   - Jika jarak pengiriman lebih dari **10 km**, dikenakan biaya tambahan sebesar **Rp 8.000**.
   - Jika jenis pengiriman adalah **express**, dikenakan biaya tambahan sebesar **Rp 20.000**.
3. **Diskon Member**: 
   - Jika pelanggan adalah **member**, maka akan diberikan **diskon 10%** dari total biaya sebelum diskon.

### Kode Fungsi:
```python
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
