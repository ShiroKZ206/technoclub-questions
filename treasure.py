"""
Mengungkap Pesan Tersembunyi

Di akhir petualangan, kamu menemukan kotak harta karun. 
Namun, untuk membukanya, kamu harus menemukan pesan tersembunyi di antara serangkaian kata. 
Penduduk Pulau Python memberimu sebuah daftar kata, dan kamu harus mencari kata yang paling sering muncul.

Contoh Input:
["harta", "karun", "petualangan", "harta", "kunci", "harta", "petualangan"]

Contoh Output:
Kata yang paling sering muncul adalah "harta"
"""
arr = ["harta", "karun", "petualangan", "harta", "kunci", "harta", "petualangan", "harta"]
# lanjutkan code dibawah ini

from collections import Counter

arr = ["harta", "karun", "petualangan", "harta", "kunci", "harta", "petualangan", "harta"]

# Menggunakan Counter untuk menghitung frekuensi setiap kata
frekuensi_kata = Counter(arr)

# Mencari kata dengan kemunculan paling sering
kata_tersering = frekuensi_kata.most_common(1)[0][0]

print(f'Kata yang paling sering muncul adalah "{kata_tersering}"')