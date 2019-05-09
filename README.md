# JawaSkrip
Tugas Akhir dari mata kuliah Teknik Kompilasi

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
'kurang dari' gunakan 'kirang saking'
'lebih dari' gunakan 'langkung saking'
'tidak sama dengan' gunakan !=
```

# BUGS

1. Belum bisa menggunakan `<` dan `>` sebagai statement
2. Belum bisa melakukan perhitungan dua data dari variabel
Contoh

```
@a = 3
@b = 4
serat @a + @b
```

3. Belum bisa menggabungkan beberapa variabel ke dalam satu variabel