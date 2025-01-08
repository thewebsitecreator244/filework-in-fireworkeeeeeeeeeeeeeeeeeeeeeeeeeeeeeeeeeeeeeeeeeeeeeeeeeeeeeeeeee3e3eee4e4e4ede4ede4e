def receipt():
    lol = "receipt.txt"
    sus = open(lol, encoding="utf-8")
    ded = sus.read()
    sus.close()
    delete = ded.split()
    leep = delete[1::2]
    sumofsus = 0
    for lolsusded in leep:
        dedsuslolint = int(lolsusded)
        sumofsus += dedsuslolint
    print(f"Итого: {sumofsus}")



receipt()
