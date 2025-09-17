## mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
```
Dalam proses pengembangan, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya contohnya mengirim data dari backend ke frontend. Data yang dikirimkan bisa bermacam-macam bentuknya. Beberapa contoh format data yang umum digunakan antara lain HTML, XML, dan JSON. Implementasi data delivery dalam bentuk HTML sudah kamu pelajari pada tutorial sebelumnya. Pada tutorial ini akan diajarkan terkait XML dan JSON.

```

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
```
Menurut dari yang saya lihat sendiri, JSON memiliki format yang lebih rapi dan ringkas sehingga lebih mudah dibaca manusia. Selain itu berdasarkan hasil pencarian saya JSON lebih ringan dan cepat sehingga untuk web dan aplikasi modern JSON lebih populer
```


## Fungi method is_valid() pada form django
```
method is_valid() berfungsi untuk memeriksa apakah semua field yang diminta pada form sudah terisi, lalu mengecek apakah data yang dimasukkan sesuai dengan fieldnya, contoh IntegerField maka is_valid() akan mengecek apakah user memasukkan angka.Selain itu is_valid juga mengecek ketentuan tambahan seperti maksimal panjang character dll. Kita membutuhkan method is_valid karena untuk mencegah adanya error yang ditimbulkan karena ketidaksesuaian tipe data maupun field yang kosong.
```

## Fungsi CSRF
```
Kita membutuhkan CSRF karena CSRF memberi token unik pada setiap form POST yang dikirim bersamaan dengan request form. Sehingga kita bisa mengecek apakah request yang didapatkan webserver valid atau tidak berdasarkan token unik pada setiap request. Hal tersebut bisa dimanfaatkan penyerang dengan memaksa user melakukan fake request ke webserver tanpa sepengetahuan user, contoh ketika user masih login pada akun yang dimiliki pada web kita lalu penyerang memberi suatu web berisi form yang jika dibuka akan mengirim request ke server, tanpa CSRF request ini akan dianggap sah dan bisa merugikan user.
```

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
```
- Membuat masing-masing fungsi pada views.py yang ada pada aplikasi main dimana fungsi JSON dan XML akan mengembalikan data dari semua product yang sudah dibuat baik dalam JSON maupun XML. Dan show_json_by_id maupun show_xml_by_id berfungsi mengembalikan data suatu product berdasarkan id nya dalam bentuk JSON maupun XML
- Import seluruh fungsi yang dibuat pada urls.py yang ada pada main lalu menambahkan path nya sesuai dengan kebutuhan pada urlpatterns
- Membuat function create_product pada views.py lalu melakukn routing dengan menambahkan pada urls.py dan membuat forms.py yang berisi class untuk form create_product serta membuat create_product.html yang berisi form create_product. Mengubah main.html dengan menambahkan tombol add product yang akan menjalankan function create_product sehingga membuka create_product.html dan memastikan isi form valid.
- Membuat product_detail.html lalu membuat function product_detail dan melakukan routing dan memodifikasi main.html dengan menambahkan tombol detail product yang akan menjalankan function product_detail dan akan di redirect ke product_detail.html
```

## Apakah ada feedback untuk asisten dosen tutorial 2 yang telah kamu kerjakan sebelumnya?
```
Sudah cukup baik, responsif dan sangat membantu.
```

## Screenshot postman
```
<img width="2879" height="1716" alt="Screenshot 2025-09-17 112702" src="https://github.com/user-attachments/assets/f5ca6766-7d9b-4ba2-96e8-e53ad7b50b31" />
<img width="2879" height="1706" alt="Screenshot 2025-09-17 112725" src="https://github.com/user-attachments/assets/45ea3ef2-7191-4cca-ab8a-9312cfd6b3da" />
<img width="2879" height="1714" alt="Screenshot 2025-09-17 112749" src="https://github.com/user-attachments/assets/4874cee7-a6ff-4f7a-a8fb-362eece36593" />
<img width="2879" height="1712" alt="Screenshot 2025-09-17 112804" src="https://github.com/user-attachments/assets/f6bcf593-91cb-418e-ac3e-a038471b3a51" />

```

=======
