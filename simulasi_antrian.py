#ujian akhir semester
#pemrograman kelas: D
#NAMA :Richard Hizkiel Kolondam
#NIM : 24210079

import time
from collections import deque
print("----simulasi antrian----")

class SistemAntrian:
    def __init__(self):
        self.antrian = deque()
        self.mulai = {}
        self.selesai = []
        
    def tambah_nasabah(self, nama, kategori):
        
        self.antrian.append({"nama":nama, "kategori": kategori})
        print(f"nasabah {nama} (kategori: {kategori}) ditambahkan ke antrian.")
        
    def proses_nasabah(self):
        if not self.antrian:
            print("tidak ada nasabah")
            return
        
        nasabah = self.antrian.popleft()
        nama = nasabah["nama"]
        kategori = nasabah["kategori"]
        print(F"melayani nasabah {nama}(kategori :{kategori})...")
        waktu_pelayanan = 2
        self.mulai[nama] = time.time()
        time.sleep(waktu_pelayanan)
        selesai = time.time()
        
        self.selesai.append(selesai - self.mulai[nama])
        print(f"nasabah {nama} selesai di layani dalam {selesai - self.mulai[nama]:.2f} menit.")
        
    def tampilkan_statistik(self):
        if not self.selesai:
            print("belum ada data pelayanan")
            return
        
        rata_rata_waktu = sum(self.selesai) / len(self.selesai)
        print(f"\n-----statistik pelayanan-----")
        print(f"jumlah nasabah yang di layani: {len(self.selesai)}")
        print(f"rata-rata waktu pelayanan: {rata_rata_waktu:.2f} menit")
        
if __name__== "__main__":
    sistem = SistemAntrian()
    
    while True:
        print("\nMenu:")
        print("1. tambah nasabah")
        print("2. proses nasabah")
        print("3. tampilkan statistik")
        print("4. keluar")
        
        pilihan = input("pilih menu (1-4): ")
        
        if pilihan == "1":
            nama = input("masukan nama nasabah: ")
            kategori = input("masukan kategori (reguler/prioritas): ")
            sistem.tambah_nasabah(nama, kategori)
        elif pilihan == "2":
            sistem.proses_nasabah()
        elif pilihan == "3":
            sistem.tampilkan_statistik()
        elif pilihan == "4":
            print("keluar dari program.")
            break
        else:
            print("pilihan tidak valid. pilihlah sesuai nomor yang ada.")        