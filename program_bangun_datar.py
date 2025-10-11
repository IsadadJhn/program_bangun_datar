import os
import math

def menu_utama():
        print( 50*"=")
        print( "Program Hitung Luas dan Keliling Bangun Datar".center(50))
        print( 50*"=")
        print("Pilih Bangun Datar :\n1.Persegi\n2.Persegi Panjang\n3.Segitiga\n4.Jajar Genjang\n5.Belah Ketupat\n6.Layang-Layang\n7.Trapesium\n8.Lingkaran")
    
def persegi():
        print(10*"=","Luas Persegi",10*"=")
        sisi = float(input("Masukkan sisi (cm) = "))
        print("Rumus luas = sisi x sisi")
        rumus_luas = sisi**2
        print(f"Luas Persegi  = {rumus_luas}")
        print(10*"=","Keliling  Persegi",10*"=")
        print("Rumus Keliling = 4 x sisi")
        rumus_keliling = 4 * sisi 
        print(f"Keliling Persegi  = {rumus_keliling}")
        return sisi,rumus_luas,rumus_keliling
        
def persegi_panjang():
        print(10*"=","Luas Persegi Panjang",10*"=")
        panjang = float(input("Masukkan panjang (cm) = "))
        lebar = float(input("Masukkan lebar (cm) = "))
        print("Rumus Luas = panjang x lebar")
        rumus_luas = panjang * lebar
        print(f"Luas Persegi Panjang = {rumus_luas}")
        print(10*"=","Keliling Persegi Panjang",10*"=")
        print("Rumus Keliling = 2 x (panjang + lebar)")
        rumus_keliling = 2 * (panjang + lebar)
        print(f"Keliling Persegi Panjang = {rumus_keliling}")
        return panjang,lebar,rumus_luas,rumus_keliling

def segitiga():
        print(10*"=","Luas Segitiga",10*"=")
        alas = float(input("Masukkan alas (cm) = "))
        tinggi = float(input("Masukkan tinggi (cm) ="))
        print("Rumus Luas = 1/2 (alas * tinggi)")
        rumus_luas = (alas * tinggi)/2
        print(f"Luas Segitiga = {rumus_luas}")
        print(10*"=","Keliling Segitiga",10*"=")
        sisi_a = float(input("Masukkan sisi a (cm) = "))
        sisi_b = float(input("Masukkan sisi b (cm) ="))
        sisi_c = float(input("Masukkan sisi c (cm) ="))
        print("Rumus Keliling = sisi a + sisi b + sisi c")
        rumus_keliling = sisi_a + sisi_b + sisi_c
        print(f"Keliling Segitiga = {rumus_keliling}")
        return rumus_luas,rumus_keliling
    
def jajar_genjang():
        print(10*"=","Luas Jajar Genjang",10*"=")
        alas = float(input("Masukkan alas (cm) = "))
        tinggi = float(input("Masukkan tinggi (cm) ="))
        print("Rumus Luas = alas x tinggi")
        rumus_luas = (alas * tinggi)
        print(f"Luas Jajar Genjang = {rumus_luas}")
        print(10*"=","Keliling Jajar Genjang",10*"=")
        sisi_miring = float(input("Masukkan sisi miring (cm) ="))
        print("Rumus Keliling = 2 x (alas + sisi miring)")
        rumus_keliling = 2 * (alas + sisi_miring)
        print(f"Keliling Jajar Genjang = {rumus_keliling}")
        return alas,rumus_luas,rumus_keliling
        
def belah_ketupat():
        print(10*"=","Luas Belah Ketupat",10*"=")
        diagonal1 = float(input("Masukkan diagonal1 (cm) = "))
        diagonal2 = float(input("Masukkan diagonal2 (cm) ="))
        print("Rumus Luas = 1/2 x (diagonal1 x diagonal2)")
        rumus_luas = (diagonal1 * diagonal2)/2
        print(f"Luas Belah Ketupat = {rumus_luas}")
        print(10*"=","Keliling Belah Ketupat",10*"=")
        sisi = float(input("Masukkan panjang sisi (cm) = "))
        print("Rumus Keliling = 4 x sisi")
        rumus_keliling = 4 * sisi
        print(f"Keliling Belah Ketupat = {rumus_keliling}")
        return rumus_luas,rumus_keliling
def layang():
        print(10*"=","Luas Layang-Layang",10*"=")
        diagonal1 = float(input("Masukkan diagonal1 (cm) = "))
        diagonal2 = float(input("Masukkan diagonal2 (cm) ="))
        print("Rumus Luas = 1/2 x (diagonal1 x diagonal2)")
        rumus_luas = (diagonal1 * diagonal2)/2
        print(f"Luas Layang-Layang = {rumus_luas}")
        print(10*"=","Keliling Layang-Layang",10*"=")
        sisi_pnjng= float(input("Masukkan sisi panjang (cm) = "))
        sisi_pndk = float(input("Masukkan sisi pendek (cm) ="))
        print("Rumus Keliling = 2 x (sisi panjang + sisi pendek)")
        rumus_keliling = 2 * (sisi_pnjng + sisi_pndk)
        print(f"Keliling Layang-Layang = {rumus_keliling}")
        return rumus_luas,rumus_keliling
def trapesium():
        print(10*"=","Luas Trapesium",10*"=")
        sisi_atas = float(input("Masukkan sisi a (cm) = "))
        sisi_bawah = float(input("Masukkan sisi b (cm) ="))
        tinggi = float(input("Masukkan tinggi (cm) ="))
        print("Rumus Luas = 1/2 x (sisi alas + sisi bawah)")
        rumus_luas = (sisi_atas + sisi_bawah) * tinggi /2
        print(f"Luas Trapesium = {rumus_luas}")
        print(10*"=","Keliling Trapesium",10*"=")
        sisi_c = float(input("Masukkan sisi c(cm) ="))
        sisi_d = float(input("Masukkan sisi d (cm) ="))
        print("Rumus Keliling = sisi a + sisi b + sisi c + sisi d")
        rumus_keliling = sisi_atas + sisi_bawah + sisi_c + sisi_d
        print(f"Keliling Trapesium = {rumus_keliling}")
        return sisi_atas,sisi_bawah,rumus_luas,rumus_keliling
def lingkaran():
        print(10*"=","Luas Lingkaran",10*"=")
        jari2= float(input("Masukkan jari-jari (cm) ="))
        print("Rumus Luas = math.pi x jari^2")
        rumus_luas = math.pi * jari2**2
        print(f"Luas Lingkaran = {rumus_luas:.2f} cm^2")
        print(10*"=","Keliling Lingkaran",10*"=")
        print("Rumus Keliling = 2 x math.pi x jari-jari")
        rumus_keliling = 2 * math.pi * jari2
        print(f"Keliling Lingkaran = {rumus_keliling:.2f} cm^2")
        return jari2,rumus_luas,rumus_keliling

while True:
        os.system("cls" if os.name=="nt" else"clear") #buat bersihin terminal
        menu_utama()
        pilihan = int(input("Pilih bangun ruang [1-8] : "))
        
        if pilihan == 1:
                persegi()
        elif pilihan == 2:
                persegi_panjang()
        elif pilihan == 3:
                segitiga()
        elif pilihan == 4:
                jajar_genjang()
        elif pilihan == 5:
                belah_ketupat()
        elif pilihan == 6:
                layang()
        elif pilihan == 7:
                trapesium()
        elif pilihan == 8:
                lingkaran()
                
        else:
            print("Pilihan tidak valid!coba lagi yaaaa...")
        
        lanjut = input("Mau lanjut?[y/n]: ").lower()
        if lanjut == "n":
            break
print("Program Selesai\nTerima Kasih!")

        

        
    








