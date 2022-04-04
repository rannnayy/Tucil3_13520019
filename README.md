# Tucil3_13520019
> Tugas Kecil 3 IF2121 Strategi Algoritma
> Maharani Ayu Putri Irawan - 13520019 - K1

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- <i>N-Puzzle</i> merupakan permainan menyusun angka yang disusun acak dalam 1 dimensi dengan sebuah kotak kosong untuk membentuk konfigurasi tertentu yang terurut.
- Dalam program ini, dibuat solver untuk 15-Puzzle, yakni N-Puzzle yang memiliki 4 baris dan 4 kolom dengan angka 1-15 dan sebuah kotak kosong.
- Permainan ini dilakukan dengan menggeser kotak-kotak dengan angka untuk mengisi tempat kotak kosong, secara tidak langsung, menggeser posisi kotak kosong untuk mengatur kotak-kotak lain.
- Algoritma <i>Branch and Bound</i> merupakan algoritma yang menggabungkan BFS dan <i>least cost search</i>, menjadikannya cocok untuk persoalan optimasi. Algoritma ini menerapkan fungsi pembatas untuk memangkas pembangkitan node yang tidak mengarah ke solusi. Alasan inilah yang menyebabkan algoritma ini cocok digunakan untuk mencari solusi dari <i>N-Puzzle</i>.

Berikut merupakan penjelasan algoritma yang digunakan.
1.	Dibuat node yang menyatakan state awal puzzle. Node ini dimasukkan ke dalam sebuah Priority Queue yang mengurutkan node berdasarkan cost (c(i)) minimum.
2.	Selama masih ada node yang berada dalam Priority Queue, akan dilakukan pemrosesan sebagai berikut untuk setiap node yang ada:
- Diambil node yang memiliki nilai estimasi cost (atau bound) terkecil.
- Dicek apakah node tersebut merupakan node solusi. Pengecekan dilakukan dengan mengecek apakah tidak ada tile yang tidak berada pada state yang seharusnya.
- Bila node tersebut merupakan node solusi, dilakukan output. Pencarian berhenti
- Bila node tersebut bukan node solusi, akan dibangkitkan node child dengan menggeser tile kosong ke seluruh arah yang mungkin di antara atas, kanan, bawah, dan kiri.
- Sebuah child node yang dibangkitkan perlu dicek validitasnya, yakni apakah tile kosong bisa digerakkan ke arah tertentu. Untuk keperluan optimasi, pergerakan tile kosong tidak boleh berlawanan dengan pergerakan sebelumnya, serta state puzzle yang ada bukan merupakan state node yang pernah dibangkitkan sebelumnya.
- Bila node valid dan memenuhi kriteria optimasi, node dimasukkan ke dalam Priority Queue dan state tersebut ditandai agar tidak terdapat pengulangan state yang sama pada pencarian selanjutnya
3.	Apabila pencarian berakhir, dilakukan output.

- Program ini disusun dalam bahasa C.


## Technologies Used
- Text Editor Visual Studio Code
- Python 3.10.0 64-bit


## Features
Fitur yang terdapat dalam program ini antara lain:
- Pengguna dapat memilih metode untuk menghasilkan puzzle yang hendak diselesaikan, yakni melalui fungsi random ataupun masukan melalui file. Catatan: File yang dimasukkan <b>harus</b> terdapat pada folder ```test```
- Keluaran program dalam bentuk state awal puzzle, nilai dari Kurang(i) dalam bentuk tabel, nilai dari Kurang(i) + X yang menentukan apakah puzzle dapat diselesaikan atau tidak, kedalaman solusi, langkah yang dilakukan pada suatu node beserta nomor node yang bersangkutan, setiap state node yang mengarah pada solusi, waktu eksekusi, dan jumlah node yang dihasilkan.


## Screenshots
![SampleOutput](https://drive.google.com/uc?export=view&id=1lrmn1fB6NmKyrC7f4oY0GWBuLyEKEbIp)


## Setup
Program ini dibangun menggunakan bahasa Python sehingga membutuhkan Python3 yang dapat diinstal pada link <a src="https://www.python.org/downloads/">berikut</a>. Download as zip atau clone repository ini. Buka project kode sumber, lalu tekan tombol F5 lalu enter, ataupun dapat menggunakan code runner extension pada Visual Studio Code Text Editor. Masukkan angka 1 untuk menghasilkan puzzle melalui fungsi random, atau 2 untuk membaca state puzzle pada file yang terletak pada folder ```/test```

Lalu program akan mencari solusi N-Puzzle pada file yang dimaksudkan. Hasil pencarian akan ditampilkan untuk setiap node yang mengarah pada solusi yang dicari. Di akhir akan ditampilkan waktu eksekusi yang diperlukan.


## Usage
Saat program dijalankan, user akan diminta untuk memasukkan pilihan menu. Masukkan 1 untuk menghasilkan state puzzle dengan randomizer, masukkan 2 untuk membaca state puzzle melalui file. Jika memilih menu 2, masukkan nama file yang berisi puzzle yang hendak diselesaikan, beserta dengan extension file yang dimaksud. Contoh input yang valid adalah sebagai berikut:

`5step.txt`

Setelahnya, program akan secara otomatis mencari solusi 15-Puzzle menggunakan algoritma ,<i>branch and bound</i>.


## Project Status
Project is: _complete_.


## Room for Improvement
Program ini masih dapat dikembangkan lebih lanjut, antara lain:.
- Penggunaan GUI.
- Optimisasi baik dalam hal memori dan waktu dalam proses.


## Acknowledgements
Ucapan terima kasih hendak saya sampaikan kepada:
- Bapak/Ibu Dosen pengampu mata kuliah IF2121 Strategi Algoritma ITB.
- Kakak-kakak asisten mata kuliah IF2121 Strategi Algoritma.


## Contact
Created by [@rannnayy](https://github.com/rannnayy) - feel free to contact me!

<b>Maharani Ayu Putri Irawan - 13520019 - K1</b>