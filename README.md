# Pertemuan 11 — Dictionary dan Key-Value dalam Python

## Identitas Mahasiswa

- **Nama:** Mutiara Sari
- **NIM:** 2225250071
- **Kelas:** 3A
- **Program Studi:** Pendidikan Matematika

## Deskripsi

Proyek ini dibuat untuk memenuhi tugas mata kuliah Algoritma dan Pemrograman pada Pertemuan 11 mengenai dictionary, pasangan key-value, dan penerapannya dalam bahasa pemrograman Python.

Program utama menerapkan dictionary untuk menyimpan dan mengelola data mahasiswa berdasarkan NIM. Data yang disimpan meliputi nama, kelas, dan nilai mahasiswa.

## Tujuan Pembelajaran

1. Memahami struktur data dictionary dalam Python.
2. Mengakses data menggunakan key.
3. Menambahkan, memperbarui, dan menghapus data dictionary.
4. Melakukan iterasi terhadap pasangan key-value menggunakan `items()`.
5. Menggunakan nested dictionary untuk menyimpan data mahasiswa.
6. Membuat fungsi untuk mencari mahasiswa dan menghitung rata-rata nilai.

## Struktur Proyek

```text
pertemuan-11-dictionary-2225250071/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_dictionary.py
│   ├── 02_akses_get.py
│   ├── 03_manipulasi_dictionary.py
│   ├── 04_iterasi_dictionary.py
│   ├── 05_dictionary_bersarang.py
│   └── 06_fungsi_dictionary.py
└── praktik/
    └── data_mahasiswa.py
```

## Struktur Data

Program menggunakan dictionary bersarang (*nested dictionary*). NIM mahasiswa berfungsi sebagai key utama, sedangkan nilai untuk setiap key berupa dictionary yang memuat nama, kelas, dan nilai mahasiswa.

Contoh:

```python
mahasiswa = {
    "A001": {
        "nama": "Ayu",
        "kelas": "A",
        "nilai": 85
    }
}
```

## Fitur Program

1. **Pencarian mahasiswa:** mencari data berdasarkan NIM menggunakan fungsi `cari_mahasiswa()`.
2. **Penanganan data yang tidak ditemukan:** menampilkan pesan ketika NIM tidak tersedia.
3. **Penambahan data:** menambahkan mahasiswa baru dengan NIM A006.
4. **Perubahan data:** memperbarui nilai mahasiswa A002 dari 78 menjadi 82.
5. **Penampilan data:** menampilkan seluruh data mahasiswa menggunakan iterasi `items()`.
6. **Perhitungan rata-rata:** menghitung rata-rata nilai seluruh mahasiswa menggunakan fungsi `rata_rata_nilai()`.

## Cara Menjalankan Program

Pastikan Python sudah terpasang dan terminal berada di direktori utama proyek.

Jalankan program utama dengan perintah:

```powershell
& C:\Users\USER\.local\bin\python3.14.exe .\praktik\data_mahasiswa.py
```

Untuk menjalankan salah satu latihan, gunakan perintah berikut sebagai contoh:

```powershell
& C:\Users\USER\.local\bin\python3.14.exe .\latihan\01_dasar_dictionary.py
```

Nama file dapat diganti sesuai latihan yang ingin dijalankan.

## Pengujian Program

| No. | Pengujian | Hasil yang Diharapkan | Status |
|---|---|---|---|
| 1 | Mencari NIM A003 | Data Citra ditemukan | Berhasil |
| 2 | Mencari NIM A999 | Pesan data tidak ditemukan | Berhasil |
| 3 | Menambahkan mahasiswa A006 | Data Fajar berhasil ditambahkan | Berhasil |
| 4 | Memperbarui nilai A002 | Nilai berubah menjadi 82 | Berhasil |
| 5 | Menampilkan seluruh data | Enam data mahasiswa ditampilkan | Berhasil |
| 6 | Menghitung rata-rata nilai | Rata-rata sebesar 83,50 | Berhasil |

## Refleksi

Melalui pengerjaan proyek ini, saya memahami penggunaan dictionary sebagai struktur data yang menyimpan pasangan key-value. Saya juga mempelajari cara mengakses data menggunakan key, memanfaatkan metode `get()` untuk menangani pencarian data, serta melakukan penambahan dan perubahan nilai pada dictionary.

Selain itu, penggunaan nested dictionary membantu saya mengorganisasi data mahasiswa secara terstruktur. Penerapan fungsi dan iterasi `items()` juga memudahkan proses pencarian, penampilan data, dan perhitungan rata-rata nilai secara sistematis.

## Kesimpulan

Dictionary dapat digunakan untuk mengelola data mahasiswa secara terstruktur berdasarkan NIM. Dengan memanfaatkan nested dictionary, fungsi, dan iterasi, program dapat melakukan pencarian, penambahan, perubahan, penampilan data, serta perhitungan rata-rata nilai mahasiswa.