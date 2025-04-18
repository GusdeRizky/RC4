# 🔐 Implementasi Algoritma RC4 dalam Bahasa Python

Repositori ini merupakan implementasi dari algoritma kriptografi **RC4 (Rivest Cipher 4)** yang ditulis menggunakan bahasa pemrograman Python. Proyek ini dibuat sebagai bagian dari **tugas proyek mata kuliah Keamanan Jaringan**.

---

## 📌 Alur Kerja Algoritma RC4

Algoritma RC4 bekerja sebagai stream cipher simetris yang menggunakan kunci rahasia untuk menghasilkan _keystream_ pseudorandom. Proses enkripsi dan dekripsi dilakukan dengan operasi XOR antara plaintext dan keystream.

Terdapat tiga tahapan utama dalam proses enkripsi menggunakan RC4:

---

### 🔸 1. **Key Scheduling Algorithm (KSA)**

Tahapan pertama bertujuan untuk menginisialisasi array **S** yang terdiri dari 256 elemen (0 hingga 255). Array ini diacak berdasarkan kunci rahasia yang dimasukkan oleh pengguna.

Langkah-langkah:

- Membuat array S dengan nilai 0 hingga 255
- Menyesuaikan panjang kunci agar sama dengan array S
- Melakukan pertukaran (swap) nilai dalam array berdasarkan kunci

---

### 🔸 2. **Pseudo-Random Generation Algorithm (PRGA)**

Tahapan ini menghasilkan _keystream_ yang akan digunakan dalam proses XOR terhadap plaintext. Keystream yang dihasilkan bersifat pseudorandom dan tergantung dari hasil proses KSA sebelumnya.

Langkah-langkah:

- Melakukan iterasi dan swap pada elemen array S
- Mengambil nilai dari array S untuk dijadikan keystream

---

### 🔸 3. **Proses Enkripsi dan Dekripsi (XOR)**

Setiap karakter dalam plaintext dikonversi ke dalam format ASCII 8-bit, lalu di-_XOR_-kan dengan keystream yang telah dihasilkan. Karena RC4 adalah algoritma simetris, proses dekripsi dilakukan dengan cara yang sama menggunakan keystream yang sama.

---

## 📚 Tujuan Proyek

Tujuan dari proyek ini adalah untuk memahami dan mengimplementasikan algoritma RC4 secara menyeluruh, meliputi proses KSA, PRGA, dan operasi XOR, serta menganalisis keunggulan dan kelemahan RC4 dalam konteks kriptografi modern.

---

Video : https://youtu.be/VTUQX-dRjYQ
