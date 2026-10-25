class KarakterSurfer:
    def __init__(self, nama):
        # TODO 1: Inisialisasi properties
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        # TODO 2: Buat behavior agar karakter mulai berlari
        self.is_running = True
        print(f"{self.nama} mulai berlari kencang menghindari kejaran inspektur!")

    def ambil_koin(self, jumlah):
        # TODO 3: Tambahkan jumlah koin ke properties koin dan berikan output informasi
        self.koin += jumlah
        self.skor += jumlah * 10 
        print(f"{self.nama} berhasil mengambil {jumlah} koin! Total koin sekarang: {self.koin}")

    def tabrak_rintangan(self):
        # TODO 4: Jika menabrak rintangan, ubah is_running menjadi False dan cetak pesan game over
        self.is_running = False
        print(f" Keprok atuh! {self.nama} menabrak rintangan kereta! Game Over!")

    def info_player(self):
        # TODO 5: Cetak status terkini (nama, skor, jumlah koin, dan status berlari)
        print("STATUS PEMAIN SUBWAY SURFERS")
        print(f"Nama Karakter : {self.nama}")
        print(f"Skor Total    : {self.skor}")
        print(f"Jumlah Koin   : {self.koin}")
        print(f"Status Berlari: {self.is_running}")
        

# --- PENGUJIAN OBJEK ---

player1 = KarakterSurfer("Jake")

player1.berlari()
player1.ambil_koin(5)
player1.ambil_koin(3)
player1.info_player()

player1.tabrak_rintangan()
player1.info_player()