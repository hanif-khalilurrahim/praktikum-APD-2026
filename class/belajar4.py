formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
formula1.insert(2, "DUIT_EMAK")
formula1[0:2] = [6767, 12, 32]
del formula1[6]
print(formula1)
sisa = formula1.pop(0)
print(sisa)
print(formula1)

