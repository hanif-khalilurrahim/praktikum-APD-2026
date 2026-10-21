import os

tambang = {
    "kutai timur" : ["batu bara", "buka"],
    "borneo" : ["nikel", "pemeliharaan"],
    "minecraft" : ["lapiece", "tutup"]
    }

print ("==============================")
print ("======Located By Tambang======")
print ("==============================")
user = input("confirm ID ADMIN Or USER :")
passs = input("confirm PASSWORD :")
("==============================")

os.system("cls")
if user == "admin" and passs == "admin123":
    while True:
        print ("============ACTION============")
        print ("1. INPUT DATA")
        print ("2. READ DATA")
        print ("3. UPDATE DATA")
        print ("4. DELETE DATA")
        print ("5. Log Out")
        aksi = input("Masukkan Nomor Untuk Menentukan Aksi Berikutnya :")
        os.system("cls")
        if aksi == "1":
            print ("=============DATA=============")
            for key,value in tambang.items():
                print (key, ":", value)
            print  ("============INPUT.============")
            print("PASTIKAN DATA YANG DIMASUKKAN TIDAK ADA PADA DICTIONARY AGAR TIDAK MENYEBABKAN PERUBAHAN PADA DATA YANG SUDAH ADA !!!")
            input_tambang1 = (input("Masukkan Lokasi Tambang :"))
            input_tambang2 = (input("masukkan Batuan Mineral :"))
            input_tambang3 = (input("masukkan Status :"))
            tambang.update({input_tambang1 : [input_tambang2, input_tambang3]})
            os.system("cls")
            print ("=============DATA=============")
            for key,value in tambang.items():
                print (key, ":", value)
            print ("==============================")
        elif aksi == "2":
            os.system("cls")
            print ("=============READ=============")
            for key,value in tambang.items():
                print (key, ":", value)
            print ("==============================")
        elif aksi == "3":
            os.system("cls")
            print ("=============DATA=============")
            for key,value in tambang.items():
                print (key, ":", value)
            print ("============UPDATE============")
            print("PASTIKAN NAMA DATA YANG DIMASUKKAN SESUAI DENGAN DATA YANG INGIN DI UBAH AGAR TIDAK MENAMBAH DICTIONARY BARU !!!")
            edit_tambang1 = (input("masukkan Data KEY Yang Ingin Di Ubah Datanya :"))
            edit_tambang2 = (input("Masukkan Perubahan Velue Biji Mineral :"))
            edit_tambang3 = (input("masukkan Perubahan Velue Status :"))
            tambang.update({edit_tambang1 : [edit_tambang2, edit_tambang3]})
            print ("==============================")
            os.system("cls")
        elif aksi == "4":
            os.system("cls")
            print ("=============DATA=============")
            for key,value in tambang.items():
                print (key, ":", value)
            print ("============DELETE============")
            del_tambang1 = (input("Masukkan Data Yang Ingin DI Delete :"))
            del tambang [del_tambang1]
            print ("==============================")
            os.system("cls")
        elif aksi == "5":
            break
        else:
            os.system("cls")
elif user == "user" and passs == "user123":
    for key,value in tambang.items():
                print (key, ":", value)
else:
    print ("ID Tidak Terdaftar")