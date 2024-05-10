def flinear(x):
    ylin = 3 * x - 5
    return ylin
def fkuadrat(x):
    ykuad = -2 * x ** 2 + 3 * x + 7
    return ykuad
def fsinus(x):
    ysin = math.sin(x * math.pi/180)
    return ysin
def flogn(x):
    yln = math.log(x + 1)
    return yln

# Fungsi integral numerik

def integral_kotak(namafungsi, batas_kiri, batas_kanan, banyak_kotak):
    lebar_kotak = (batas_kanan - batas_kiri) / banyak_kotak
    luas_tiap_kotak = [0] * banyak_kotak
    for i in range(1, banyak_kotak + 1):
        luas_tiap_kotak[i-1] = namafungsi(batas_kiri + (i - 1) * lebar_kotak) * lebar_kotak
    hasil_integral = sum(luas_tiap_kotak)
    return hasil_integral

def integral_trapesium(namafungsi, batas_kiri, batas_kanan,banyak_trapesium):
    lebar_trapesium = (batas_kanan - batas_kiri) / banyak_trapesium
    y_kiri = namafungsi(batas_kiri)
    y_kanan = namafungsi(batas_kanan)
    if (banyak_trapesium == 1):
        hasil_integral = 0.5 * lebar_trapesium * (y_kiri + y_kanan)
    else: 
       y_antara = [0] * banyak_trapesium
    for k in range(1, banyak_trapesium):
       y_antara[k] = namafungsi(batas_kiri + k * lebar_trapesium)
    hasil_integral = 0.5 * lebar_trapesium * (y_kiri + 2 * sum(y_antara) + y_kanan)
    return(hasil_integral)

# Contoh 

integral_trapesium(flinear, 1, 4, 10)