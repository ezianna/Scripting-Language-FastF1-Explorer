🏎️ FastF1 EDA – Exploratory Data Analysis Formula 1

Project ini adalah sebuah aplikasi web sederhana berbasis Flask yang digunakan untuk melakukan Exploratory Data Analysis (EDA) pada data balap Formula 1. Data diambil menggunakan library FastF1, yaitu package Python resmi yang menyediakan akses ke data telemetry, lap times, race information, dan berbagai data teknis yang digunakan dalam analisis performa pembalap.

Aplikasi ini dibuat untuk keperluan mini project/capstone project, dan dapat dijalankan secara lokal maupun dideploy ke platform hosting berbasis Python.

Penjelasan Project

Aplikasi ini bekerja dengan cara mengambil data session Formula 1 dari FastF1, kemudian menampilkannya melalui beberapa halaman analisis. Setiap data yang diambil akan disimpan ke dalam folder cache sehingga akses berikutnya menjadi lebih cepat.

Project terdiri dari beberapa fitur utama:

1. Halaman Home
Menampilkan ringkasan singkat serta navigasi ke halaman-halaman analisis lainnya.

2. Race Overview
Pada halaman ini, pengguna dapat melihat gambaran umum mengenai sebuah sesi (misalnya balapan). Data yang ditampilkan bisa meliputi nama circuit, jumlah pembalap, jumlah lap, dan berbagai informasi dasar lainnya.

3. Lap Time Analysis
Halaman ini menampilkan data lap pembalap, termasuk waktu per lap, fastest lap, dan pola konsistensi pembalap selama race. Data lap biasanya digunakan untuk memahami performa rata-rata pembalap sepanjang race.

4. Telemetry Analysis
Analisis telemetry dapat menunjukkan throttle, brake, gear, speed, dan berbagai data teknis lain dari suatu lap tertentu. Informasi ini relevan untuk menunjukkan bagaimana pembalap mengemudi pada titik-titik tertentu di track.

5. Driver Comparison
Halaman perbandingan pembalap digunakan untuk memvisualisasikan dua pembalap dan membandingkan lap mereka, baik dari sisi telemetry maupun waktu lapnya. Fitur ini sangat berguna untuk memahami perbedaan driving style antar pembalap.

Struktur Folder dan Alur Program

Project ini disusun dengan pola struktur yang umum digunakan pada aplikasi Flask:

app.py
File utama untuk menjalankan aplikasi. Di sini blueprint dari setiap route didaftarkan.

routes/
Berisi file-file Python untuk setiap halaman:

home.py untuk halaman beranda

race.py untuk data balapan

lap.py untuk analisis lap

telemetry.py untuk telemetry

compare.py untuk perbandingan pembalap

services/
Berisi fungsi helper, terutama untuk memuat data FastF1. File fastf1_loader.py menangani semua proses pemanggilan API FastF1, memuat session, laps, dan telemetry.

templates/
Folder tempat semua halaman HTML berada. Menggunakan Jinja2 untuk template engine.

static/
Folder berisi file CSS, JavaScript, dan gambar.

Struktur ini bertujuan agar project mudah di-maintain dan scalable jika ingin dikembangkan lebih jauh.

Dependensi yang Digunakan

Project ini menggunakan beberapa library utama:

Flask: untuk membangun aplikasi web

FastF1: untuk mengambil data Formula 1

Pandas: untuk manipulasi data

Matplotlib: untuk membuat grafik statis

NumPy: mendukung perhitungan numerik

Library tambahan bisa ditambahkan sesuai kebutuhan, misalnya Plotly atau ApexCharts jika ingin membuat visualisasi yang lebih interaktif.

Cara Kerja FastF1 dalam Project

FastF1 mengambil data melalui API F1 Live Timing dan menyediakannya dalam bentuk DataFrame. Ketika pengguna memilih musim dan sesi tertentu, loader akan:

Mengaktifkan cache

Memuat session

Mengambil data lap, telemetry, atau informasi pembalap

Mengirimkan data tersebut ke halaman HTML

Menampilkan hasilnya dalam bentuk tabel atau grafik

Karena FastF1 menyediakan dataset sangat lengkap, project ini bisa dikembangkan lebih jauh untuk analisis performa yang lebih mendalam.

Pengembangan Lanjutan

Jika project ini ingin dikembangkan lagi, beberapa fitur berikut bisa ditambahkan:

Tema UI bergaya F1 (merah–hitam / dark theme)

Grafik interaktif dengan Plotly

Pemilihan Grand Prix & sesi melalui dropdown

Analisis sektor time

Perbandingan multi-driver

Pit stop analysis

Integrasi API untuk data real-time

Penutup

Project ini dibuat sebagai mini project EDA berbasis web untuk menganalisis data Formula 1 secara praktis. Dengan menggunakan FastF1, pengguna bisa mendapatkan insight dari data balapan dan telemetry tanpa harus mengolah data mentah secara manual.

Jika ingin menambahkan fitur, mempercantik tampilan, atau melakukan deployment, project ini sudah cukup fleksibel untuk dikembangkan lebih jauh.