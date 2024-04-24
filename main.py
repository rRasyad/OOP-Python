from model import Dosen


class Main:
    # Atribut yang ada pada class Main
    # model_dosen
    # def __init__(self):
    #     self.model_dosen = Dosen("aisyah@example.com", "password")
    #     self.model_dosen.proses_login()


    def login(self):
        print("\n-- LOGIN --")
        email = input("Masukkan email: ")
        password = input("Masukkan password: ")

        model_dosen = Dosen(email, password)
        self.model_dosen = model_dosen

        login_status = model_dosen.proses_login()
        # print(login_status)  # Debug

        match login_status:
            case None:
                print(
                    "\nAkun Tidak Ditemukan, "
                    "Mengalihkan ke halaman register untuk membuat akun!"
                )
                return self.register()

            case False:
                print("\nPassword Salah!")
                return self.login()

            case True:
                return self.daftar_siswa()


    def register(self):
        print("\n-- REGISTER --")
        nama_dosen = input("Masukkan nama anda: ")

        self.model_dosen.membuat_akun(nama_dosen)
        print("\nAkun anda berhasil dibuat!")
        return self.login()


    def daftar_siswa(self):
        print("\n-- DAFTAR SISWA --\n")

        data_siswa = self.model_dosen.ambil_data_siswa()
        for i, per_data in enumerate(data_siswa):
            print("{:2}. {}".format((i + 1), per_data["nama_siswa"]))

        print(
            "",
            "[1] untuk menambah data",
            "[2] untuk mengubah data",
            "[3] untuk menghapus data",
            "[4] untuk keluar",
            sep="\n",
        )
        pilihan = int(input("> "))
        match pilihan:
            case 1:
                return self.tambah()
            case 2:
                return self.seleksi(data_siswa, True)
            case 3:
                return self.seleksi(data_siswa, False)
            case 3:
                return
            case _:
                print("\nPilihan tidak ada!")
                return self.daftar_siswa()


    def tambah(self):
        print("\n-- MENAMBAHKAN DATA SISWA --")
        nama_siswa = input("Masukkan nama siswa: ")
        self.model_dosen.tambah_data_siswa(nama_siswa)
        return self.daftar_siswa()


    def seleksi(self, data_siswa, mode_udate):

        nomer_urut = int(input("Masukkan nomer urut: "))
        # Cek nomer yang dimasukkan lebih dari data yang ada
        if nomer_urut > len(data_siswa):
            print("\nPilihan tidak ada")
            return self.seleksi(data_siswa, mode_udate)

        # mengambil id dari data yang dipilih
        id_terpilih = data_siswa[(nomer_urut - 1)]["id_siswa"]

        # Membuat keputusan apakah untuk update atau delete
        if mode_udate is True:
            nama_siswa = input("Masukkan nama baru: ")
            self.model_dosen.ubah_data_siswa(id_terpilih, nama_siswa)
            print("data berhasil diubah!")
            
        else:
            self.model_dosen.hapus_data_siswa(id_terpilih)
            print("data berhasil dihapus!")

        return self.daftar_siswa()


try:
    Main().login()
except KeyboardInterrupt:
    print("Goodbye!")
