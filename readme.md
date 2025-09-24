## Tugas 3
```
## mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam proses pengembangan, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya contohnya mengirim data dari backend ke frontend. Data yang dikirimkan bisa bermacam-macam bentuknya. Beberapa contoh format data yang umum digunakan antara lain HTML, XML, dan JSON. 

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut dari yang saya lihat sendiri, JSON memiliki format yang lebih rapi dan ringkas sehingga lebih mudah dibaca manusia. Selain itu berdasarkan hasil pencarian saya JSON lebih ringan dan cepat sehingga untuk web dan aplikasi modern JSON lebih populer


## Fungi method is_valid() pada form django
method is_valid() berfungsi untuk memeriksa apakah semua field yang diminta pada form sudah terisi, lalu mengecek apakah data yang dimasukkan sesuai dengan fieldnya, contoh IntegerField maka is_valid() akan mengecek apakah user memasukkan angka.Selain itu is_valid juga mengecek ketentuan tambahan seperti maksimal panjang character dll. Kita membutuhkan method is_valid karena untuk mencegah adanya error yang ditimbulkan karena ketidaksesuaian tipe data maupun field yang kosong.

## Fungsi CSRF
Kita membutuhkan CSRF karena CSRF memberi token unik pada setiap form POST yang dikirim bersamaan dengan request form. Sehingga kita bisa mengecek apakah request yang didapatkan webserver valid atau tidak berdasarkan token unik pada setiap request. Hal tersebut bisa dimanfaatkan penyerang dengan memaksa user melakukan fake request ke webserver tanpa sepengetahuan user, contoh ketika user masih login pada akun yang dimiliki pada web kita lalu penyerang memberi suatu web berisi form yang jika dibuka akan mengirim request ke server, tanpa CSRF request ini akan dianggap sah dan bisa merugikan user.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
- Membuat masing-masing fungsi pada views.py yang ada pada aplikasi main dimana fungsi JSON dan XML akan mengembalikan data dari semua product yang sudah dibuat baik dalam JSON maupun XML. Dan show_json_by_id maupun show_xml_by_id berfungsi mengembalikan data suatu product berdasarkan id nya dalam bentuk JSON maupun XML
- Import seluruh fungsi yang dibuat pada urls.py yang ada pada main lalu menambahkan path nya sesuai dengan kebutuhan pada urlpatterns
- Membuat function create_product pada views.py lalu melakukn routing dengan menambahkan pada urls.py dan membuat forms.py yang berisi class untuk form create_product serta membuat create_product.html yang berisi form create_product. Mengubah main.html dengan menambahkan tombol add product yang akan menjalankan function create_product sehingga membuka create_product.html dan memastikan isi form valid.
- Membuat product_detail.html lalu membuat function product_detail dan melakukan routing dan memodifikasi main.html dengan menambahkan tombol detail product yang akan menjalankan function product_detail dan akan di redirect ke product_detail.html

## Apakah ada feedback untuk asisten dosen tutorial 2 yang telah kamu kerjakan sebelumnya?
Sudah cukup baik, responsif dan sangat membantu.
```
## Screenshot postman
<table>
  <tr>
    <td>
      <img width="2879" height="1716" alt="Screenshot 2025-09-17 112702" src="https://github.com/user-attachments/assets/f5ca6766-7d9b-4ba2-96e8-e53ad7b50b31" />
      <br>
      <img width="2879" height="1706" alt="Screenshot 2025-09-17 112725" src="https://github.com/user-attachments/assets/45ea3ef2-7191-4cca-ab8a-9312cfd6b3da" />
      <br>
      <img width="2879" height="1714" alt="Screenshot 2025-09-17 112749" src="https://github.com/user-attachments/assets/4874cee7-a6ff-4f7a-a8fb-362eece36593" />
      <br>
      <img width="2879" height="1712" alt="Screenshot 2025-09-17 112804" src="https://github.com/user-attachments/assets/f6bcf593-91cb-418e-ac3e-a038471b3a51" />
    </td>
  </tr>
</table>

## Tugas 4
```
## apa itu django authetication form, jelaskan kelebihan dan kekurangannya
Django AuthenticationForm adalah sebuah form class bawaan dari modul django yang dirancang untuk proses autentikasi (login) pengguna. Form ini memiliki dua field utama: username dan password. AuthenticationForm bertugas mengecek apakah username yang dimasukkan ada, jika ada mengecek apakah passwordnya benar, dan mengecek apakah akun tersebut aktif. Kelebihannya adalah cepat digunakan, validasi otomatis, dan integrasi penuh dengan login dan logout. Sedangkan kekurangannya kustomisasinya terbatas


## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi (Authentication): Siapa Anda?
Ini adalah proses untuk memverifikasi identitas seseorang, sistem akan memverifikasi apakah anda adalah benar-benar orang sesuai dengan yang anda masukkan
Implementasi di Django: Django mengelola ini melalui django.contrib.auth. Prosesnya melibatkan pengecekan username dan password menggunakan AuthenticationForm dan fungsi authenticate(). Jika berhasil, fungsi login() akan membuat sesi untuk pengguna tersebut, yang menandai mereka sebagai "terautentikasi" untuk request-request selanjutnya.

Otorisasi (Authorization): Apa yang Boleh Anda Lakukan?
Ini adalah proses untuk menentukan hak akses atau izin yang dimiliki oleh pengguna yang sudah terautentikasi.
Implementasi di Django: Django memiliki sistem perizinan (permissions) yang sangat kuat.
Setiap model secara otomatis mendapatkan izin add, change, delete, dan view. Izin kustom juga bisa dibuat. Selain itu Django menyediakan alat seperti decorator @login_required dan @permission_required atau mixin LoginRequiredMixin untuk membatasi akses ke view tertentu


## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Cookies adalah data kecil yang dikirim dari server ke browser pengguna dan disimpan di sisi klien (di komputer pengguna). Browser akan mengirimkan kembali cookie tersebut pada setiap permintaan berikutnya ke server yang sama.
Kelebihannya adalah Sederhana sehingga Mudah untuk diimplementasikan untuk data yang tidak sensitif.
Kekurangan:
Tidak Aman Karena disimpan di klien, data di dalamnya dapat dilihat dan dimanipulasi oleh pengguna. Sangat tidak disarankan untuk menyimpan data sensitif (seperti ID pengguna atau peran) langsung di cookie, Ukuran cookie sangat terbatas (sekitar 4KB), Pengguna dapat memblokir cookies di browser mereka, yang dapat merusak fungsionalitas aplikasi.

Sessions menyimpan data di sisi server. Server akan membuat ID sesi unik, mengirimkannya ke browser dalam bentuk cookie, dan browser akan mengirim kembali ID tersebut pada setiap permintaan. Server kemudian menggunakan ID ini untuk mengambil data sesi yang relevan.
Kelebihannya Aman karena Data sensitif disimpan di server, bukan di klien. Klien hanya menyimpan ID sesi yang acak dan tidak berarti, Ukuran Lebih Besar: Tidak ada batasan ukuran praktis seperti pada cookies karena data disimpan di server, Server memiliki kontrol penuh atas masa aktif dan data sesi.
Kekurangannya Beban Server akan bertambah, karena Setiap sesi aktif akan memakan memori atau ruang penyimpanan di server.


## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Tidak, penggunaan cookies tidak aman secara default. Cookie standar pada dasarnya adalah file teks biasa yang rentan terhadap beberapa risiko keamanan. Namun django mengatasi ini salah satunya adalah bisa dengan manmbahkan CSRF protection


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
- Membuat masing-masing fungsi pada views.py yang ada pada aplikasi main dimana fungsi JSON dan XML akan mengembalikan data dari semua product yang sudah dibuat baik dalam JSON maupun XML. Dan show_json_by_id maupun show_xml_by_id berfungsi mengembalikan data suatu product berdasarkan id nya dalam bentuk JSON maupun XML
- Import seluruh fungsi yang dibuat pada urls.py yang ada pada main lalu menambahkan path nya sesuai dengan kebutuhan pada urlpatterns
- Membuat function create_product pada views.py lalu melakukn routing dengan menambahkan pada urls.py dan membuat forms.py yang berisi class untuk form create_product serta membuat create_product.html yang berisi form create_product. Mengubah main.html dengan menambahkan tombol add product yang akan menjalankan function create_product sehingga membuka create_product.html dan memastikan isi form valid.
- Membuat product_detail.html lalu membuat function product_detail dan melakukan routing dan memodifikasi main.html dengan menambahkan tombol detail product yang akan menjalankan function product_detail dan akan di redirect ke product_detail.html

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- import authenticate, login, logout dari django.contrib.auth
- menambahkan fuction login, logout, dan register pada views.py
- Buat templates html untuk login, register, dan menambahkan button logout pada main.html
- tambahkan path untuk setiap fuction yang dibuat pada urls.py
- pada models, tambahkan variabel user, lalu setiap user login tambahkan setcookies pada functionnya untuk mendapatkan last session user tersebut
- modifikasi product_detail.html dengan menambahkan username dari product yang membuat product tersbut
```
