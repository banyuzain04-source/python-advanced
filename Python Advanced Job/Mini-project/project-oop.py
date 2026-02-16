import os


class User:
    def __init__(self, nama: str, nis: str):
        self.nama = nama
        self.nis = nis

    def info_user(self) -> str:
        return f"Santri: {self.nama} | NIS: {self.nis}"


class Nasabah(User):
    def __init__(self, nama: str, nis: str, saldo_awal: int = 0):
        super().__init__(nama, nis)
        
        self.__saldo = saldo_awal 
        print(f"[System] Rekening berhasil dibuat untuk {self.nama}!")

    @property
    def saldo_saat_ini(self) -> int:
        return self.__saldo

    def setor(self, nominal: int):
        if nominal > 0:
            self.__saldo += nominal
            print(f"\n[Sukses] Berhasil setor tunai: Rp{nominal:,}")
            print(f"Saldo baru Anda: Rp{self.__saldo:,}")
        else:
            print("\n[Gagal] Nominal setor harus lebih dari 0.")

    def tarik(self, nominal: int):
        if nominal <= 0:
             print("\n[Gagal] Nominal tarik harus lebih dari 0.")
             return

        if nominal > self.__saldo:
            print(f"\n[Gagal] Saldo tidak cukup!")
            print(f"Permintaan: Rp{nominal:,} | Saldo Tersedia: Rp{self.__saldo:,}")
        else:
            self.__saldo -= nominal
            print(f"\n[Sukses] Berhasil tarik tunai: Rp{nominal:,}")
            print(f"Sisa saldo Anda: Rp{self.__saldo:,}")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_angka(pesan: str) -> int:
    while True:
        try:
            angka = int(input(pesan))
            return angka
        except ValueError:
            print("[Error] Input salah! Mohon masukkan hanya angka.")


if __name__ == "__main__":
    clear_screen()
    print("=== APLIKASI TABUNGAN DIGITAL PONDOK ===")
    print("Silakan buat rekening baru terlebih dahulu.\n")

    nama_input = input("Masukkan Nama Santri : ")
    nis_input = input("Masukkan NIS         : ")
    saldo_input = input_angka("Masukkan Saldo Awal  : Rp")

    akun_santri = Nasabah(nama_input, nis_input, saldo_input)

    while True:
        print("\n" + "="*40)
        print(f"MENU UTAMA - User: {akun_santri.nama}")
        print("="*40)
        print("1. Cek Info Akun & Saldo")
        print("2. Setor Tunai (Menabung)")
        print("3. Tarik Tunai (Mengambil)")
        print("4. Keluar Aplikasi")
        print("="*40)
        
        pilihan = input("Pilih menu (ketik angka 1-4): ")

        if pilihan == '1':
            clear_screen()
            print("\n--- INFORMASI AKUN ---")
            print(akun_santri.info_user())
            print(f"Saldo Saat Ini: Rp{akun_santri.saldo_saat_ini:,}")

        elif pilihan == '2':
            print("\n--- SETOR TUNAI ---")
            nominal = input_angka("Masukkan nominal yang akan disetor: Rp")
            akun_santri.setor(nominal)

        elif pilihan == '3':
            print("\n--- TARIK TUNAI ---")
            print(f"Saldo tersedia: Rp{akun_santri.saldo_saat_ini:,}")
            nominal = input_angka("Masukkan nominal yang akan ditarik: Rp")
            akun_santri.tarik(nominal)

        elif pilihan == '4':
            print("\nTerimakasih telah menggunakan aplikasi ini.")
            print("Jazakumullah Khairan.")
            break

        else:
            print("\n[Warning] Pilihan tidak valid. Silakan pilih angka 1 sampai 4.")