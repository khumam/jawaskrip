# JawaSkrip
Jawascript  adalah sebuah bahasa esolang berbasis python yang perintahnya menggunakan bahasa jawa. Tujuan dari pembuatan esolang berbahasa jawa ini adalah untuk mengenalkan bahasa jawa dan menjaga bahasa jawa khususnya bahasa jawa krama ingil. Manfaat yang diberikan, selain melestarikan bahasa daerah, juga dapat membuat kita belajar bahasa pemrograman.

# Instalasi
Untuk menginstall silahkan download repositori ini atau clone

```
https://github.com/sahmura/jawaskrip.git
```
Setelah itu masuk ke dalam folder `Jawaskrip`
Buatlah sebuah file dengan ekstensi `.jws`

# Run
Untuk me-run program, di folder jawasckrip, ketikkan di terminal / command prompt

```
python jawaskrip.py nama_program.jws
```
Pastikan sudah menginstall python.

# DOCS

### Variabel
Gunakan `@` dilanjutkan dengan nama variabel.
Contoh

```
@nama = "Tony Stark"
```

### Print
Untuk menampilkan sesuatu, gunakan `serat`
Contoh

```
serat "Mr Tony! Mr Tony! Jangan pergi..."
serat "I love you 3000"
serat 20
serat @nama
```

### Input
Untuk memasukan data ke dalam variabel, gunakan `lebet`
Contoh

```
lebet "Berapa kemungkinan kita mengalahkan thanos? = " @data
```

Ketika kita memasukkan data, maka akan tersimpan di variabel data

### Expresi
Untuk melakukan perhitungan, gunakan perhitungan biasa
Contoh

```
@jumlah = 5 + 3
serat 54 / 23
serat @jumlah
```

### If Statement
Untuk menggunakan if statement, gunakan pola di bawah ini

```
menawi statement mila
    isi
bibarmenawi
```

Contoh

```
menawi 1 == 1 mila
    serat "Captain America"
bibarmenawi
```

if statement yang tersedia

```
'sama dengan' gunakan ==
'kurang dari sama dengan' gunakan <=
'lebih dari sama dengan' gunakan >=
'kurang dari' gunakan 'kirang'
'lebih dari' gunakan 'langkung'
'tidak sama dengan' gunakan !=
```

# Looping
Saat ini looping belum sempurna masih dalam tahap pengembangan

```
kangge 0 ngantos 3
    serat "i love you 3000"
sampung
```

Hasil

```
i love you 3000
i love you 3000
i love you 3000
```

# BUGS

1. Belum bisa menggunakan `<` dan `>` sebagai statement
    - Fix dengan mengganti < dengan kirang dan > langkung
2. Belum bisa melakukan perhitungan dua data dari variabel
Contoh

```
@a = 3
@b = 4
serat @a + @b
```
3. Looping belum sempurna
