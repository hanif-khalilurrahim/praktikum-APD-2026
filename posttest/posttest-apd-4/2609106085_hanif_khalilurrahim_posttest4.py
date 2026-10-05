Username = "karuga"
Password = "085"
saldo = 1000000


for batas in range(1,4):

    print("====================ATM=====================")
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
    print("============================================")

    if (username != Username and password != Password):
        continue
    break
print("Akun Anda Diblokir!!!")
print("============================================")


if(username == Username and password == Password):
    print("[1] Cek Saldo")
    print("[2] Tarik Tunai")
    print("[3] Setor Tunai")
    print("[4] Keluar")
    aksi = int(input("Tentukan Pilihan : "))
    if (aksi == 1):
        print (saldo)
    elif aksi == 2:
        tarik = int(input("Masukkan Nominal Yang Ingin Di Tarik : "))
        hasil_tarik = saldo - tarik
        print ("Total Saldo : ", hasil_tarik)
    elif aksi == 3:
        setor = int(input("Masukkan Nominal Yang Ingin Di Setor"))
        hasil_setor = saldo + setor
        print (hasil_setor)
    else :
        print ("anda keluar")

   