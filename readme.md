<!-- # 🚀 MyProject


---

## 📖 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license) -->

## Alur pengerjaan step by step
```bash
- Membuat directory pada local dan repository baru pada github sesuai dengan project yang akan dibuat
- menginstall dan mengaktifkan enviroment agar dependencies tidak konflik dengan dependencies yang ada di local
- Install dependencies yang diperlukan pada directory
- Melakukan integrasi antara local dengan repo pada github
- Menambahkan aplikasi main pada project
- Mengubah models pada main sesuai dengan ketentuan soal dan yang dibutuhkan
- melakukan migration untuk data yang sudah diubah
- Membuat directory templates pada aplikasi main yang berisi html sesuai dengan apa yang ingin ditampilkan pada aplikasi main
- Melakukan perubahan pada file views di aplikasi main dan membuat fungsi untuk mengembalikan dictionary berisi data sesuai dengan yang dibutuhkan pada html dan melakukan render html
- menambahkan urls pada aplikasi main dengan path kosong maka akan menampilkan aplikasi main lalu menambahkannya pada urls project
- Melakukan deployment pada pacil web service
```

## Bagan
<img width="1707" height="957" alt="Screenshot 2025-09-10 110335" src="https://github.com/user-attachments/assets/a7eed1e6-dc4b-483c-a40e-ce4256ac7be9" />


## Penjelasan settings.py
```
settings bertugas sebagai pusat konfigurasi dari web yang dibuat. Mulai dari mengatur allowed hosts (host/domain yang diizinkan), allowed apps untuk mengatur app apa saja yang akan digunakan
```

## Penjelasan fungsi migrate
```
migrate bertujuan untuk mencatat setiap perubahan pada models, contoh menambah/rename atribut, lalu migrate menerjemahkan perubahan tersebut untuk dijalankan di database
```

## Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
```
Django memungkinkan kita untuk membuat real product tanpa perlu mempelajari SQL secara mendalam, jadi pemula bisa lebih fokus pada logika pengembangan perangkat lunak terlebih dahulu tanpa perlu takut untuk mempelajari SQL sebagai database.
```

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
```
Sudah cukup baik, responsif dan sangat membantu.
```

<!-- ## 🛠 Installation
```bash
git clone https://github.com/username/myproject.git
cd myproject
npm install -->
