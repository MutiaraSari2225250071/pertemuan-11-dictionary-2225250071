# Data mahasiswa menggunakan dictionary bersarang
mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


# Fungsi mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(data, nim):
    return data.get(nim, "Data mahasiswa tidak ditemukan")


# Fungsi menghitung rata-rata nilai mahasiswa
def rata_rata_nilai(data):
    if not data:
        return 0

    total_nilai = sum(
        data_mahasiswa["nilai"]
        for data_mahasiswa in data.values()
    )

    return total_nilai / len(data)


# Menampilkan hasil pencarian mahasiswa
print("=== PENCARIAN MAHASISWA ===")
print("NIM A003:", cari_mahasiswa(mahasiswa, "A003"))
print("NIM A999:", cari_mahasiswa(mahasiswa, "A999"))


# Menambahkan data mahasiswa baru
mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

print("\n=== SETELAH PENAMBAHAN DATA ===")
print("Data mahasiswa A006:", mahasiswa["A006"])


# Memperbarui nilai mahasiswa
mahasiswa["A002"]["nilai"] = 82

print("\n=== SETELAH PERUBAHAN NILAI ===")
print("Data mahasiswa A002:", mahasiswa["A002"])


# Menampilkan seluruh data mahasiswa
print("\n=== SELURUH DATA MAHASISWA ===")
for nim, data_mahasiswa in mahasiswa.items():
    print(
        f"NIM: {nim}, "
        f"Nama: {data_mahasiswa['nama']}, "
        f"Kelas: {data_mahasiswa['kelas']}, "
        f"Nilai: {data_mahasiswa['nilai']}"
    )


# Menghitung rata-rata nilai seluruh mahasiswa
print("\n=== RATA-RATA NILAI ===")
print(f"Rata-rata nilai mahasiswa: {rata_rata_nilai(mahasiswa):.2f}")