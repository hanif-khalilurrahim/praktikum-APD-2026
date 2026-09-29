print("==========================LOGIN===========================")
nama = str(input("masukkan nama "))
password = int(input("masukkan nim "))
print("==========================================================")

if password >= 1 :
    print("Login Berhasil")
    print("==========================================================")
    id = int(input("masukkan ID "))
    print("==========================================================")
    print("Tersedia Genshin Impact/Minecraft/Mobile Legends")
    nama_game = str(input("masukkan nama game "))
    print("==========================================================")
    print("Metode Pembayaran Tersedia Pulsa/E-Wallet")
    metodepay = str(input("masukkan metode pembayaran "))
    print("==========================================================")
    print("Kategori Top Up Tersedia Kecil/Menengah/Besar")
    kategori_topup = (input("masukkan kategori top up "))
    print("==========================================================")
    # ================================================================
    if kategori_topup == "kecil":
        harga = 15000
        # ================================================================
        biaya_admin = 2500 if metodepay == "pulsa" else 500
        total_bayar = biaya_admin + harga
        # ================================================================
        print("==========================================================")
        print("Player ID ", (id))
        print("Game Yang Dipilih ", (nama_game))
        print("Kategori Top Up ", (kategori_topup))
        print("Metode Pembayaran ", (metodepay))
        print("Biaya Admin ", (biaya_admin))
        print("Total Pembayaran ", (total_bayar))
        print("==========================================================")
    elif kategori_topup == "menengah":
        harga = 50000
        # ================================================================
        biaya_admin = 2500 if metodepay == "pulsa" else 500
        total_bayar = biaya_admin + harga
        # ================================================================
        print("==========================================================")
        print("Player ID ", (id))
        print("Game Yang Dipilih ", (nama_game))
        print("Kategori Top Up ", (kategori_topup))
        print("Metode Pembayaran ", (metodepay))
        print("Biaya Admin ", (biaya_admin))
        print("Total Pembayaran ", (total_bayar))
        print("==========================================================")
    elif kategori_topup == "besar":
        harga = 150000
        # ================================================================
        biaya_admin = 2500 if metodepay == "pulsa" else 500
        total_bayar = biaya_admin + harga
        # ================================================================
        print("==========================================================")
        print("Player ID ", (id))
        print("Game Yang Dipilih ", (nama_game))
        print("Kategori Top Up ", (kategori_topup))
        print("Metode Pembayaran ", (metodepay))
        print("Biaya Admin ", (biaya_admin))
        print("Total Pembayaran ", (total_bayar))
        print("==========================================================")
    else :
        print("Kategori Tidak Terdaftar")
else:
    print("Login Gagal")

    

