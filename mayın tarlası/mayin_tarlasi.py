# Nursena Taskopru
import random

while True:
    r = int(input("Boyut giriniz:"))
    while True:
        if r < 10:  # 10 ya da daha buyuk bir deger girene kadar kontrol ediyor
            print("!10ya da daha buyuk bir sayi giriniz!")
            r = int(input("Yeni sayi giriniz:"))
            continue
        else:
            break
    mayin_sayisi = int(r * r * 0.3)
    matrix = [['?' for _ in range(r)] for _ in range(r)]
    mayinlar = []  # mayinlarin ust uste gelmemesi icin
    yerlesen_mayinlar = 0  # tum mayinlar yerlestirilmis mi kontrol ederken kullaniliyor
    while yerlesen_mayinlar < mayin_sayisi:
        x = random.randint(0, r - 1)
        y = random.randint(0, r - 1)
        if (x, y) not in mayinlar:
            matrix[x][y] = 'x'
            yerlesen_mayinlar += 1
            mayinlar.append((x, y))
    oyun_bitti_mi = False
    while not oyun_bitti_mi:  # oyun bitmedigi surece dongu devam ediyor ve tekrar tekrar satir ve sutun degeri aliniyor
        print("1)Gizli Mod\n2)Acik Mod")
        secim = input("Seciminizi giriniz:")
        if secim == '1':
            hamle = 0
            gizli_matrix = matrix.copy()  # orijinal matrixi kaybetmeden gizli matrixi yazdırmak icin
            gizli_matrix = [['?' if matrix[i][j] == 'x' else '?' for j in range(r)] for i in range(r)]
            while not oyun_bitti_mi:
                for satir in gizli_matrix:  # 2 boyutlu matrix yazdirmak icin
                    print('\t'.join(satir))
                x = int(input("Satir giriniz:"))
                y = int(input("Sutun giriniz:"))
                while True:
                    if x > (r - 1) or y > (r - 1):  # matrix disindan deger secilmemesi icin
                        print("!Boyuttan buyuk bir sayi girmeyiniz!")
                        x = int(input("Yeni satir degeri giriniz:"))
                        y = int(input("Yeni sutun degeri giriniz:"))
                    elif x < 0 or y < 0:
                        print("!0'dan kucuk bir sayi girmeyiniz!")
                        x = int(input("Yeni satir degeri giriniz:"))
                        y = int(input("Yeni sutun degeri giriniz:"))
                    else:
                        break
                if (x, y) in mayinlar:
                    gizli_matrix[x][y] = 'x'
                    for satir in gizli_matrix:
                        print('\t'.join(satir))
                    oyun_bitti_mi = True
                    print("Maalesef kaybettiniz\tPuaniniz:{}".format(hamle))
                    print("1)Yeni Oyun\n2)Cikis")
                    istek = int(input("Seciminizi giriniz:"))
                    if istek == 1:
                        r = 0
                        x = 0
                        y = 0
                        mayin_sayisi = 0
                        hamle = 0
                        gizli_matrix = [[]]
                        matrix = []
                        mayinlar = []
                        yerlesen_mayinlar = 0
                        sayac = 0
                        oyun_bitti_mi = False
                        r = int(input("Boyut giriniz:"))
                        while True:
                            if r < 10:  # 10 ya da daha buyuk bir deger girene kadar kontrol ediyor
                                print("!10ya da daha buyuk bir sayi giriniz!")
                                r = int(input("Yeni sayi giriniz:"))
                                continue
                            else:
                                break
                        mayin_sayisi = int(r * r * 0.3)
                        matrix = [['?' for _ in range(r)] for _ in range(r)]
                        mayinlar = []  # mayinlarin ust uste gelmemesi icin
                        yerlesen_mayinlar = 0  # tum mayinlar yerlestirilmis mi kontrol ederken kullaniliyor
                        while yerlesen_mayinlar < mayin_sayisi:
                            x = random.randint(0, r - 1)
                            y = random.randint(0, r - 1)
                            if (x, y) not in mayinlar:
                                matrix[x][y] = 'x'
                                yerlesen_mayinlar += 1
                                mayinlar.append((x, y))
                        oyun_bitti_mi = False
                        break
                    else:
                        print("Cikis yapiliyor...")
                        exit()
                elif matrix[x][y] == '?':
                    hamle += 1
                    sayac = 0
                    for i in range(max(0, x - 1), min(r, x + 2)):
                        for j in range(max(0, y - 1), min(r, y + 2)):
                            if matrix[i][j] == 'x':
                                # secilen hucrenin etrafindaki mayinlarin sayisini verilen sınırlar içinde var mı bulup mayin sayisini hucreye yazdirmak icin
                                sayac += 1
                    gizli_matrix[x][y] = str(sayac)
                elif gizli_matrix[x][y] != '?' or matrix[x][y] != '?':
                    print("Burasi daha once secildi baska yer seciniz")
                    continue
        elif secim == '2':
            hamle = 0
            while not oyun_bitti_mi:  # gizli moddakiyle ayni sadece gizli modda ek olarak gizli matrix vardi
                for satir in matrix:
                    print('\t'.join(satir))
                x = int(input("Satir giriniz:"))
                y = int(input("Sutun giriniz:"))
                while True:
                    if x > (r - 1) or y > (r - 1):  # matrix disindan deger secilmemesi icin
                        print("!Boyuttan buyuk bir sayi girmeyiniz!")
                        x = int(input("Yeni satir degeri giriniz:"))
                        y = int(input("Yeni sutun degeri giriniz:"))
                    elif x < 0 or y < 0:
                        print("!0'dan kucuk bir sayi girmeyiniz!")
                        x = int(input("Yeni satir degeri giriniz:"))
                        y = int(input("Yeni sutun degeri giriniz:"))
                    else:
                        break
                if (x, y) in mayinlar:
                    matrix[x][y] = 'x'
                    for satir in matrix:
                        print('\t'.join(satir))
                    oyun_bitti_mi = True
                    print("Maalesef kaybettiniz\tPuaniniz{}:".format(hamle))
                    print("1)Yeni Oyun\n2)Cikis")
                    istek = int(input("Seciminizi giriniz:"))
                    if istek == 1:
                        r = 0
                        mayin_sayisi = 0
                        hamle = 0
                        matrix = []
                        mayinlar = []
                        yerlesen_mayinlar = 0
                        sayac = 0
                        oyun_bitti_mi = False
                        # asagıda exit fonksiyonuna kadar olan kısmı 2 modda da oyun kaybedilirse ve kazanılırsa diye 3 yere tekrar ekledim
                        r = int(input("Boyut giriniz:"))
                        while True:
                            if r < 10:  # 10 ya da daha buyuk bir deger girene kadar kontrol ediyor
                                print("!10ya da daha buyuk bir sayi giriniz!")
                                r = int(input("Yeni sayi giriniz:"))
                                continue
                            else:
                                break
                        mayin_sayisi = int(r * r * 0.3)
                        matrix = [['?' for _ in range(r)] for _ in range(r)]
                        mayinlar = []  # mayinlarin ust uste gelmemesi icin
                        yerlesen_mayinlar = 0  # tum mayinlar yerlestirilmis mi kontrol ederken kullaniliyor
                        while yerlesen_mayinlar < mayin_sayisi:
                            x = random.randint(0, r - 1)
                            y = random.randint(0, r - 1)
                            if (x, y) not in mayinlar:
                                matrix[x][y] = 'x'
                                yerlesen_mayinlar += 1
                                mayinlar.append((x, y))
                        oyun_bitti_mi = False
                        break
                    else:
                        print("Cikis yapiliyor...")
                        exit()
                elif matrix[x][y] == '?':
                    hamle += 1
                    sayac = 0
                    for i in range(max(0, x - 1), min(r, x + 2)):
                        for j in range(max(0, y - 1), min(r, y + 2)):
                            if matrix[i][j] == 'x':
                                sayac += 1
                    matrix[x][y] = str(sayac)
                elif matrix[x][y] != '?':
                    print("Burasi daha once secildi baska yer seciniz")
                    continue
        else:
            acilmayanlarin_sayisi = sum(satir.count('?') for satir in matrix)
            # oyunu kazanıp kazanmadigimizi kontrol etmek icin kullaniyoruz
            if acilmayanlarin_sayisi == mayin_sayisi:
                oyun_bitti_mi = True
                print("Oyunu kazandiniz\tPuaniniz:{}".format(hamle))
                print("1)Yeni Oyun\n2)Cikis")
                istek = int(input("Seciminizi giriniz:"))
                if istek == 1:
                    r = 0
                    mayin_sayisi = 0
                    hamle = 0
                    gizli_matrix = []
                    matrix = []
                    mayinlar = []
                    yerlesen_mayinlar = 0
                    sayac = 0
                    oyun_bitti_mi = False
                    r = int(input("Boyut giriniz:"))
                    while True:
                        if r < 10:  # 10 ya da daha buyuk bir deger girene kadar kontrol ediyor
                            print("!10ya da daha buyuk bir sayi giriniz!")
                            r = int(input("Yeni sayi giriniz:"))
                            continue
                        else:
                            break
                    mayin_sayisi = int(r * r * 0.3)
                    matrix = [['?' for _ in range(r)] for _ in range(r)]
                    mayinlar = []  # mayinlarin ust uste gelmemesi icin
                    yerlesen_mayinlar = 0  # tum mayinlar yerlestirilmis mi kontrol ederken kullaniliyor
                    while yerlesen_mayinlar < mayin_sayisi:
                        x = random.randint(0, r - 1)
                        y = random.randint(0, r - 1)
                        if (x, y) not in mayinlar:
                            matrix[x][y] = 'x'
                            yerlesen_mayinlar += 1
                            mayinlar.append((x, y))
                    oyun_bitti_mi = False
                    break
                else:
                    print("Cikis yapiliyor...")
                    exit()
