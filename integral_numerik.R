flinear = function(x) 3*x-5
fkuadrat = function(x) -2 * x ** 2 + 3 * x + 7
fsinus = function(x) sin(x * pi/180)
flogn = function(x) log(x + 1)

integral_kotak = function(namafungsi, batas_kiri, batas_kanan, banyak_kotak) {
  lebar_kotak = (batas_kanan - batas_kiri) / banyak_kotak
  luas_tiap_kotak = rep(0, banyak_kotak)
  for (i in 1:banyak_kotak) {
    luas_tiap_kotak[i] = namafungsi(batas_kiri + (i - 1) * lebar_kotak) * lebar_kotak
  }
  hasil_integral = sum(luas_tiap_kotak)
  return(hasil_integral)
}

integral_trapesium = function(namafungsi, batas_kiri, batas_kanan, banyak_trapesium) {
  lebar = (batas_kanan - batas_kiri) / banyak_trapesium
  y_kiri = namafungsi(batas_kiri)
  y_kanan = namafungsi(batas_kanan)
  if (banyak_trapesium == 1) {
    hasil_integral = (1 / 2) * lebar * (y_kiri + y_kanan)
  } else {
    y_antara = rep(0, banyak_trapesium)
    k = 1:(banyak_trapesium - 1)
    y_antara[k] = namafungsi(batas_kiri + k * lebar)
    hasil_integral =
      (1 / 2) * lebar * (y_kiri + 2 * sum(y_antara) + y_kanan)
  }
  return(hasil_integral)
}

