# def sapa(nama = 'andi'):
#     print(f"hallo {nama}")

# sapa('budi')

# def luas(sisi):
#     luas = sisi ** 2
#     return luas

# print(luas(2))

# nama = 'india'
# def negara():
#     nama = 'indonesia'
#     print(nama)
# print(nama)
# negara()

# def faktorial(n):
# #Base Case: Kondisi fungsi berhenti
#     if n == 0 or n == 1:
#         return 1
# #Rekursive Case: Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# #Memanggil fungsi
# hasil_faktorial = faktorial(4)
# print(f"Hasil dari 4! {hasil_faktorial}")

# def tampilkan_menu():
#     print("\n")
#     print("========= MENU =========")
#     print("[1] Lihat Data Buku")
#     print("[2] Tambahkan Data Buku")
#     print("[3] Edit Data Buku")
#     print("[4] Hapus Data Buku")
#     print("[5] Keluar")
# menu = input("PILIH MENU > ")
# print("\n")
# if menu == "1":
#     lihat_buku()
# elif menu == "2":
#     tambah_buku()
# elif menu == "3":
#     edit_buku()
# elif menu == "4":
#     hapus_buku()
# elif menu == "5":
#     exit()
# else:
#     print("Pilihan tidak valid!")

# modul baru <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# syntax error

# umur = int(input('Masukkan Angka : '))
# print(umur)

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else:
#     print(f'Angka yang kamu input : {angka}')
# finally:
#     print('Blok Try Selesai')

# try:
#     usn = input('Username yang diinginkan : ')
#     if len(usn) < 5:
#         raise ValueError('Nama Minimal Memiliki 5 karakter')
# except ValueError as e:
#     print(e)