import mysql.connector as mysql


# Class DB adalah parent class/model yang berperan sebagai koneksi ke database
class DB:
    # Atribut yang ada di dalam class DB
    # connection, cursor

    def __init__(self):
        try:
            db_connection = mysql.connect(
                host="localhost", user="root", password="911", database="oop_python"
            )

            # print(db_connection)
            # Kalau connect outputnya akan seperti ini
            # <mysql.connector.connection_cext.CMySQLConnection object at 0x0000024F9A6FDE10>

            self.connection = db_connection
            self.cursor = self.connection.cursor()

        except Exception as e:
            print("Error Message:\n", e)


# Class Dosen adalah child class/model yang mewakili tabel Dosen
class Dosen(DB):
    # Atribut yang ada dalam class Dosen
    # data_login, id_dosen, nama_dosen, no_telp, email, __password
    # data_login sebagai atribut sementara

    def __init__(self, email, password):
        # memanggil fungsi constructor yang ada di parent class/model
        super().__init__()

        # menyimpan data_login
        self.data_login = {"email": email, "password": password}


    def proses_login(self):
        # Deklarasi variable lokal
        data_login = self.data_login
        cursor = self.cursor
        query = "SELECT * FROM dosen WHERE email = %s"

        # Memeriksa apakah akun ada atau tidak
        cursor.execute(query, (data_login["email"],))
        hasil = cursor.fetchone()
        # print('Contoh hasil querynya:', hasil) # Debug

        # Jika email tidak ditemukan
        if hasil is None:
            return None

        # Jika password salah
        elif hasil[-1] != data_login["password"]:
            return False

        # Jika semuanya benar data akan disimpan kedalam attribut
        else:
            (
                self.id_dosen,
                self.nama_dosen,
                self.no_telp,
                self.email,
                self.__password,
            ) = hasil

            del self.data_login
            return True


    def membuat_akun(self, nama_dosen):
        # Deklarasi variable lokal
        data_login = self.data_login
        cursor = self.cursor
        connection = self.connection
        query = "INSERT INTO dosen (nama_dosen, email, password) VALUES (%s, %s, %s)"

        cursor.execute(query, (nama_dosen, data_login["email"], data_login["password"]))
        connection.commit()

        del self.data_login
        return None


    def daftar_siswa(self):
        # Deklarasi variable lokal
        cursor = self.cursor
        query = "SELECT * FROM siswa WHERE id_dosen = %s"

        cursor.execute(query, (self.id_dosen,))
        data_raw = cursor.fetchall()
        # print("Contoh data mentahnya:", data_raw) # Debug

        hasil = []
        for per_data in data_raw:
            hasil.append({"id_siswa": per_data[0], "nama_siswa": per_data[2]})
        # print("Setelah di ubah:", hasil) # Debug
        return hasil


    def tambah_data_siswa(self, nama_siswa):
        # Deklarasi variable lokal
        cursor = self.cursor
        connection = self.connection
        query = "INSERT INTO siswa  (id_dosen, nama_siswa) VALUES (%s, %s)"

        cursor.execute(query, (self.id_dosen, nama_siswa))
        connection.commit()
        return
    

    def ubah_data_siswa(self, id_siswa, nama_siswa):
        # Deklarasi variable lokal
        cursor = self.cursor
        connection = self.connection
        query = "UPDATE siswa SET nama_siswa = %s WHERE id_siswa = %s"

        cursor.execute(query, (nama_siswa, id_siswa))
        connection.commit()
        return


    def hapus_data_siswa(self, id_siswa):
        # Deklarasi variable lokal
        cursor = self.cursor
        connection = self.connection
        query = "DELETE FROM siswa WHERE id_siswa = %s"

        cursor.execute(query, (id_siswa,))
        connection.commit()
        return
