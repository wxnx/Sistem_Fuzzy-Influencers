import csv

# ini fungsi-fungsi/prosedur-prosedur nya
def ambilFile():
    with open('influencers.csv') as file:
        baca = csv.reader(file)
        hasil = []
        for i in baca:
            hasil.append(i)
    return hasil

def ambilValuensi(x):
    y = x[1:100]
    hasil = []
    for i in y:
        data = []
        data.append(float(i[1]))
        data.append(float(i[2]))
        hasil.append(data)
    return hasil

def pengikutTinggi(x):
    if(x > 55000):
        hasilF = 1
    elif(x <= 45000):
        hasilF = 0
    else:
        hasilF = (x-4500)/(55000-45000)
    return hasilF

def pengikutSedang(x):
    if (x > 55000 or x <= 5000):
        hasilF = 0
    elif (25000 < x <= 35000):
        hasilF =1
    elif (5000 < x <= 25000):
        hasilF = (x - 5000) / (25000 - 5000)
    else:
        hasilF = (55000 - x) / (55000-35000)
    return hasilF

def pengikutRendah(x):
    if (x < 5000):
        hasilF = 1
    elif (x >= 15000):
        hasilF = 0
    else:
        hasilF = (15000 - x) / (15000 - 5000)
    return hasilF

def jumlahPengikut(x):
    hasilF = []
    tinggi = pengikutTinggi(x)
    hasilF.append(tinggi)
    sedang = pengikutSedang(x)
    hasilF.append(sedang)
    rendah = pengikutRendah(x)
    hasilF.append(rendah)
    return hasilF

def engBagus(x):
    if (x > 5):
        hasilF = 1
    elif (x <= 4):
        hasilF = 0
    else:
        hasilF = (x - 4) / (5 - 4)
    return hasilF

def engCukup(x):
    if (x <= 0.5 or x > 5):
        hasilF = 0
    elif (2 < x <= 3):
        hasilF = 1
    elif(0.5 < x <= 2):
        hasilF = (x - 0.5) / (2 - 0.5)
    else:
        hasilF = (5 - x) / (5 - 3)
    return hasilF

def engBuruk(x):
    if ( x < 0.5):
        hasilF = 1
    elif (x >= 1.5):
        hasilF = 0
    else:
        hasilF = (1.5 - x) / (1.5 - 0.5)
    return hasilF

def jumEng(x):
    hasilF = []
    bagus = engBagus(x)
    hasilF.append(bagus)
    cukup = engCukup(x)
    hasilF.append(cukup)
    buruk = engBuruk(x)
    hasilF.append(buruk)
    return hasilF

def hasil(x, y):
    hasil = []
    for i in x:
        for j in y:
            if(i > j):
                hasil.append(i)
            else:
                hasil.append(j)
    return hasil

def setuju(x):
    s7 = []
    s7.append(x[0])
    s7.append(x[1])
    s7.append(x[3])
    hasil = max(s7)
    return hasil

def dipertimbang(x):
    dT = []
    dT.append(x[2])
    dT.append(x[4])
    dT.append(x[5])
    dT.append(x[6])
    hasil = max(dT)
    return hasil

def tolak(x):
    tlk = []
    tlk.append(x[7])
    tlk.append(x[8])
    hasil = max(tlk)
    return hasil

def metodeSugeno(x, y, z):
    hasil = ((x * 80) + (y * 60) + (z * 40)) / (x + y + z)
    return hasil

# ini main Programnya

file = ambilFile()
data = ambilValuensi(file)
hasilnya = []
for i in data:
    pengikut = jumlahPengikut(i[0])
    eng = jumEng(i[1])
    h = hasil(pengikut, eng)
    s7 = setuju(h)
    dT = dipertimbang(h)
    tlk = tolak(h)
    hmet = metodeSugeno(s7, dT, tlk)
    hasilnya.append(hmet)

a = sorted(range(len(hasilnya)), key=lambda k: hasilnya[k], reverse=True)
b = a[:20]
maks = []
for i in b:
    maks.append([hasilnya[i], i+1])
maksimum = maks

print("#####################----- 20 Influencer Terbaik -----#####################")

for i in maksimum :
    print("---------------------------------------------------------------------------")
    print(" Nilai Fuzzy : ", i[0])
    print(" Index Data  : ", i[1])
    print("---------------------------------------------------------------------------")

print("***************************************************************************")

with open("result.csv", "+w") as csvNya:
    tulis = csv.writer(csvNya, delimiter=',')
    tulis.writerows(maksimum)
