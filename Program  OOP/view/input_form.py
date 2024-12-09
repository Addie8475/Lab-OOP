# File: view/input_form.py

class InputForm:
    @staticmethod
    def input_mahasiswa():
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")
        return nim, nama, jurusan
