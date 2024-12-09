from data.mahasiswa import Mahasiswa
from view.input_form import InputForm

class MahasiswaView:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self):
        nim, nama, jurusan = InputForm.input_mahasiswa()
        mahasiswa = Mahasiswa(nim, nama, jurusan)
        self.daftar_mahasiswa.append(mahasiswa)
        print("Data mahasiswa berhasil ditambahkan!")

    def tampilkan_mahasiswa(self):
        if not self.daftar_mahasiswa:
            print("Belum ada data mahasiswa.")
            return
        print("Daftar Mahasiswa:")
        for i, mahasiswa in enumerate(self.daftar_mahasiswa, start=1):
            print(f"{i}. {mahasiswa}")

    def cari_mahasiswa(self, nim):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None

    def hapus_mahasiswa(self):
        nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
        mahasiswa = self.cari_mahasiswa(nim)
        if mahasiswa:
            self.daftar_mahasiswa.remove(mahasiswa)
            print("Data mahasiswa berhasil dihapus!")
        else:
            print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

    def ubah_mahasiswa(self):
        nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
        mahasiswa = self.cari_mahasiswa(nim)
        if mahasiswa:
            print("Data lama:", mahasiswa)
            nim_baru, nama_baru, jurusan_baru = InputForm.input_mahasiswa()
            mahasiswa.nim = nim_baru
            mahasiswa.nama = nama_baru
            mahasiswa.jurusan = jurusan_baru
            print("Data mahasiswa berhasil diubah!")
        else:
            print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
