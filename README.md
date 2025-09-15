# FeetBalls
FeetBalls

### Author
- Name: Muhammad Nadhif Ibrahim
- NPM: 2406398324
- Class: PBP C

### Deployment
You can access the web here: [FeetBalls](https://muhammad-nadhif41-footballshop.pbp.cs.ui.ac.id/)

---

## Tugas Individu 2 - PBP Ganjil 2025/2026

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. **Membuat sebuah proyek Django baru.**
   - Buat direktori baru yaitu football-shop. Pastikan Python sudah terinstall (bisa cek dengan mengetik `python --version` di terminal). Lalu, install django dengan mengetik `pip install django` di terminal atau `pip install -r requirements.txt` di mana requirements.txt berisi django dan lain-lain. Terakhir, jalankan `django-admin startproject football-shop`

2. **Membuat aplikasi dengan nama main pada proyek tersebut.**
   - Ketik `python manage.py startapp main` di terminal dan aplikasi main akan terbuat.

3. **Melakukan *routing* pada proyek agar dapat menjalankan aplikasi main.**
   - Buka `settings.py`, tambahkan main di `INSTALLED_APPS`.

4. **Membuat model pada aplikasi main dengan nama Product.**
   - Buka models.py, tambahkan `class Product(models.Model):`, lalu isi dengan atribut wajib `name`, `price`, `description`, `thumbnail`, `category`, dan `is_featured`.

5. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.**
   - Import `from django.shortcuts import render`, buat fungsi yang menerima `request`, mengisi `context` yang berguna seperti "kamus" untuk aplikasi, dan me-return `render(request, file HTML, context)`.

6. **Membuat sebuah *routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
   - Buka `football-shop/urls.py`, tambahkan `from django.urls import path, include`, lalu di `urlspattern`; tambahkan `path('', include('main.urls'))`.

7. **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
   - Buat project baru di PWS. Set enviroment variables. Tambahkan URL deployment PWS di `ALLOWED_HOSTS` pada `settings.py`. Lalu push ke PWS dan gunakan credentials yang telah diterima.

8. **Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.**
   - Buat file `README.md` yang berisi tautan menuju aplikasi PWS dan menjawab beberapa pertanyaan.

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   ![Bagan Django](assets/bagan_django.jpg)

### Jelaskan peran settings.py dalam proyek Django!
 - `settings.py` bagaikan otak dari project tersebut. Ia mengatur identitas project (bahasa, zona waktu, dll), daftar aplikasi aktif (di `INSTALLED_APPS`), konfigurasi database, mengatur lokasi file statis dan file upload dari user, keamanan, dan lain-lain.

### Bagaimana cara kerja migrasi database di Django?
 - Migrasi adalah cara Django menerjemahkan perubahan pada `models.py` ke database. Alur kerjanya adalah mendefinisikan model di `models.py`. Lalu, jalankan `python manage.py makemigrations` di terminal, ini akan membuat file migrasi di folder migrations. Terakhir, jalankan `python manage.py migrate` di terminal sehingga tabel dari model akan terbentuk di database.

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
 - Pertama, Django menggunakan bahasa pemrograman Python, di mana Python merupakan bahasa pemrograman yang mudah dipelajari oleh pemula karena bahasanya yang mendekati bahasa manusia. Kedua, dokumentasi dan komunitas yang bagus, di mana dokumentasi Django sangat lengkap dan banyak forum yang membahas Django. Ketiga, relevansi dunia nyata, di mana banyak industri besar yang menggunakan Django sebagai framework.

### Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
 - Tidak ada.

## Tugas Individu 3 - PBP Ganjil 2025/2026

### Menjawab beberapa pertanyaan berikut pada README.md pada root folder.

1. **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
 - Data delivery diperlukan dalam pengimplementasian sebuah platform agar semua modul dapat komunikasi dan bekerja sama. Data harus bisa dikirim dari satu bagian ke bagian lain. Misal, user isi form di web, data dikirim ke server, server proses, lalu kirim hasil ke user. Selain itu, data delivery yang aman dapat meningkatkan keamanan dan privasi, data delivery yang aman mencakup HTTPS, enkripsi, dan autentikasi. Data delivery yang baik juga dapat meningkatkan efisiensi dan perform, misalnya caching, compression, atau streaming.

2. **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
 - Menurut saya, JSON lebih baik dari XML. Alasannya adalah lebih readable, cocok dengan struktur data di banyak bahasa pemrograman, dan ringan (tidak banyak tag). JSON lebih populer dibandingkan XML karena beberapa alasan yang saya tulis tadi. Selain itu, JSON lebih populer karena ekosistem API modern sudah seragam memakai JSON. Semenjak mobile app & web API berkembang pesat, JSON menjadi standar di industri.

3. **Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
 - 

4. **Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
 - 

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

6. **Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**

### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.