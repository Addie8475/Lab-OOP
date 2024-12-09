# File: main.py

from view.mahasiswa import MahasiswaView

def main():
    mahasiswa_view = MahasiswaView()

    while True:
        print("\nMenu Utama:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Hapus Mahasiswa")
        print("4. Ubah Mahasiswa")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            mahasiswa_view.tambah_mahasiswa()
        elif pilihan == "2":
            mahasiswa_view.tampilkan_mahasiswa()
        elif pilihan == "3":
            mahasiswa_view.hapus_mahasiswa()
        elif pilihan == "4":
            mahasiswa_view.ubah_mahasiswa()
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
