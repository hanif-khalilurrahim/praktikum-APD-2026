import os

tambang = [["kutai timur","batu bara", "buka"], ["borneo","nikel", "pemeliharaan"], ["minecraft","lapiece", "tutup"]]

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
            print  ("============INPUT.============")
            input_tambang1 = (input("Masukkan Lokasi Tambang :"))
            input_tambang2 = (input("masukkan Batuan Mineral :"))
            input_tambang3 = (input("masukkan Status :"))
            tambang.append([input_tambang1, input_tambang2, input_tambang3])
            os.system("cls")
            print ("=============DATA=============")
            for i in tambang:
                print (i)
            print ("==============================")
        elif aksi == "2":
            os.system("cls")
            print ("=============READ=============")
            for i in tambang:
                print (i)
            print ("==============================")
        elif aksi == "3":
            os.system("cls")
            print ("=============DATA=============")
            for i in tambang:
                print (i)
            print ("============UPDATE============")
            edit_tambang1 = int(input("masukkan Perubahan List Ke Berapa :"))
            edit_tambang2 = int(input("Masukkan Perubahan Data Ke Berapa :"))
            edit_tambang3 = (input("masukkan Perubahan Yang DI Ingin Kan :"))
            tambang[edit_tambang1][edit_tambang2] = edit_tambang3
            print ("==============================")
            os.system("cls")
        elif aksi == "4":
            os.system("cls")
            print ("=============DATA=============")
            for i in tambang:
                print (i)
            print ("============DELETE============")
            print ("Data Awal = 0")
            del_tambang1 = int(input("Masukkan Data Yang Ingin DI Delete :"))
            del tambang [del_tambang1]
            print ("==============================")
        elif aksi == "5":
            break
        else:
            os.system("cls")
elif user == "user" and passs == "user123":
    for i in tambang:
        print (i)
else:
    print ("ID Tidak Terdaftar")