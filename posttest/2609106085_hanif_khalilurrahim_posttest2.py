# tugas untuk declaire veriable
nim = 85
harga_komponen = (
    komponen_1 := 120000,
    komponen_2 := 135000,
    komponen_3 := 150000,
    komponen_4 := 175000,
    komponen_5 := 200000,
    komponen_6 := 220000
)

# tugas untuk perhitungan
total_biaya = komponen_1 + komponen_2 + komponen_3 + komponen_4 + komponen_5 + komponen_6 + 15000
rata_rata = total_biaya / 6
bolean = nim != rata_rata
mata_uang = total_biaya / 23.860

# tugas untuk print semua veriable
print ("TOTAL BIAYA : ", (total_biaya))
print ("RATA RATA : ", int(rata_rata), "| versi FLOAT : ", (rata_rata))
print ("BOLEAN : ", (bolean))
print ('slice index NEGAtif', (harga_komponen [-6 : -2]))
print ("konversi mata uang dari total biaya ke GBP : ", int(mata_uang), "| versi FLOAT : ", (mata_uang))
