import mysql.connector
from mysql.connector import Error

# Konfigurasi koneksi MySQL
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "abil123",
    "database": "uts_pbo"
}

def get_koneksi():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print("Gagal koneksi ke MySQL:", e)
        return None


def hitung_nilai_huruf(nilai):
    if nilai >= 85:
        return 'A'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 65:
        return 'C'
    elif nilai >= 50:
        return 'D'
    else:
        return 'E'


class RapotModel:
    def __init__(self):
        self.conn = get_koneksi()

    def fetch_all(self):
        if not self.conn:
            return []

        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM rapot_mahasiswa ORDER BY id ASC")
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def create(self, nim, nama, prodi, matkul, nilai_angka):
        if not self.conn:
            return False, "Tidak terkoneksi ke DB"

        nilai_huruf = hitung_nilai_huruf(nilai_angka)

        sql = """
            INSERT INTO rapot_mahasiswa (nim, nama, prodi, matkul, nilai_angka, nilai_huruf)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, (nim, nama, prodi, matkul, nilai_angka, nilai_huruf))
            self.conn.commit()
            return True, cursor.lastrowid
        except Error as e:
            return False, str(e)
        finally:
            cursor.close()

    def update(self, id_, nim, nama, prodi, matkul, nilai_angka):
        if not self.conn:
            return False, "Tidak terkoneksi ke DB"

        nilai_huruf = hitung_nilai_huruf(nilai_angka)

        sql = """
            UPDATE rapot_mahasiswa
            SET nim=%s, nama=%s, prodi=%s, matkul=%s, nilai_angka=%s, nilai_huruf=%s
            WHERE id=%s
        """

        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, (nim, nama, prodi, matkul, nilai_angka, nilai_huruf, id_))
            self.conn.commit()
            return True, None
        except Error as e:
            return False, str(e)
        finally:
            cursor.close()

    def delete(self, id_):
        if not self.conn:
            return False, "Tidak terkoneksi ke DB"

        cursor = self.conn.cursor()
        try:
            cursor.execute("DELETE FROM rapot_mahasiswa WHERE id=%s", (id_,))
            self.conn.commit()
            return True, None
        except Error as e:
            return False, str(e)
        finally:
            cursor.close()
