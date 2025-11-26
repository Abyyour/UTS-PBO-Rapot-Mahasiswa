Siap Abil! Aku buatin **README.md versi profesional**, rapi, lengkap, dan cocok banget buat dinilai dosen (nilai tambah CLEAN ARCHITECTURE + MVP).
Tinggal copy–paste ke GitHub ➝ klik README.md ➝ edit.

---

# ✅ **README.md — Aplikasi Rapot Mahasiswa (UTS PBO)**

# 📚 Aplikasi Rapot Mahasiswa

Aplikasi GUI desktop untuk mengelola data penilaian mahasiswa dengan fitur **CRUD**, **filtering**, dan **integrasi database MySQL**. Dibuat menggunakan arsitektur **MVP (Model–View–Presenter)** agar kode rapi, mudah dikembangkan, dan terstruktur.

---

## ✨ **Fitur Utama**

* ➕ **Tambah data mahasiswa**
* ✏️ **Update data**
* ❌ **Hapus data**
* 🔍 **Filter berdasarkan:**

  * Angkatan (berdasarkan 2 digit awal NIM)
  * Program Studi (Prodi)
  * Mata Kuliah
* 🔄 Refresh data otomatis setelah CRUD
* 🗂 **Konversi nilai angka → huruf (A–E)**
* 💾 Database **MySQL**
* 🎨 GUI modern menggunakan **CustomTkinter**

---

## 🏗 **Arsitektur Projek**

Menggunakan pola **MVP (Model–View–Presenter)**:

```
rapot_mahasiswa_project/
│
├── app/
│   ├── model.py       → Query ke database MySQL
│   ├── view.py        → GUI CustomTkinter
│   └── controller.py  → Logika aplikasi & penghubung Model–View
│
├── main.py            → Entry point aplikasi
├── requirements.txt   → Library Python
└── schema.sql         → File pembuatan tabel MySQL
```

---

## 🛢 **Struktur Database**

Table: **rapot_mahasiswa**

| Kolom       | Tipe Data          |
| ----------- | ------------------ |
| id          | INT AUTO_INCREMENT |
| nim         | VARCHAR(20)        |
| nama        | VARCHAR(100)       |
| prodi       | VARCHAR(100)       |
| matkul      | VARCHAR(100)       |
| nilai_angka | INT                |
| nilai_huruf | CHAR(1)            |
| created_at  | TIMESTAMP          |

---

## 🚀 **Cara Menjalankan Aplikasi**

### 1️⃣ Install Library

```
pip install -r requirements.txt
```

### 2️⃣ Import Database

Jalankan file `schema.sql` di MySQL Workbench.

### 3️⃣ Jalankan Aplikasi

```
python main.py
```

---

## 🖼 **Tampilan GUI**

* Input data mahasiswa
* Tabel penilaian terstruktur
* Filter angkatan, prodi, dan mata kuliah
* Desain modern CustomTkinter

---

## 👨‍💻 **Teknologi yang Digunakan**

* Python 3
* CustomTkinter
* Tkinter
* MySQL Connector
* MySQL Workbench
* MVP Architecture

---

## 📌 **Tujuan Dibuat**

Tugas **UTS Pemrograman Berbasis Objek (PBO)**
Dosen: **Rudy Rachman**

---

## ✍️ **Developer**

**Muhammad Abil**
NIM: *240105003*

---

## 📁 **Link Repository GitHub**

🔗 [https://github.com/Abyyour/UTS-PBO-Rapot-Mahasiswa](https://github.com/Abyyour/UTS-PBO-Rapot-Mahasiswa)

---

Kalau mau versi README yang ada gambar/screenshots, tinggal bilang:
👉 **"Tambahkan screenshot ke README"**
NTAR aku buatin yang lebih keren lagi 😎🔥
