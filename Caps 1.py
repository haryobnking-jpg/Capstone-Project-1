import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate 

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="020806",
    database="SMA2"
)
cursor = db.cursor()

def tampilkan_data():
    cursor.execute("SELECT * FROM nilai_siswa")
    rows = cursor.fetchall()
    headers = ["ID", "Nama", "Kelas", "Mata Pelajaran", "Nilai", "Umur", "Gender"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def tambah_siswa():
    Nama = input("Masukkan Nama: ")
    Kelas = input("Masukkan Kelas: ")
    Mapel = input("Masukkan Mata Pelajaran: ")

    while True:
        try:
            Nilai = int(input("Masukkan Nilai: "))
            break
        except ValueError:
            print("Nilai Harus Berupa Angka!!")

    while True:
        try:
            Umur = int(input("Masukkan Umur: "))
            break
        except ValueError:
            print("Umur Harus Berupa Angka!!")

    while True:
            Gender = input("Masukkan Gender(Male/Female): ")
            if Gender in ["Male", "Female"]:
                break
            else:
                print("Gender hanya boleh Male atau Female.")            

    query = """
    INSERT INTO nilai_siswa (Nama, Kelas, Mata_Pelajaran, Nilai, Umur, Gender)
    VALUES (%s,%s,%s,%s,%s,%s)
    """ 
    value = (Nama, Kelas, Mapel, Nilai, Umur, Gender)
    cursor.execute(query, value)
    db.commit()

    print("Data siswa berhasil ditambahkan!")

    lihat = input("Mau lihat data terbaru? (y/n): ").lower()
    if lihat == "y":
        tampilkan_data()


def hitung_statistik():
    while True:
        print("\n ====  Menu Statistik  ====")
        print("1. Statistik Nilai Siswa")
        print("2. Statistik Umur Siswa")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Masukkan pilihan Anda (1-3): ")

        if pilihan == "1":

            while True:
                print("\n====  Statistik Nilai Siswa  ====")
                print("1. Rata-rata Nilai ")
                print("2. Nilai Tertinggi ")
                print("3. Nilai Terendah ")
                print("4. Kembali ke Menu Statistik")

                sub_pilihan = input("Masukkan Pilihan Anda (1-4): ")

                if sub_pilihan == "1":
                    cursor.execute("SELECT AVG(Nilai) FROM nilai_siswa")
                    print(f"Rata-rata Nilai: {cursor.fetchone()[0]:.2f}")
                elif sub_pilihan == "2":
                    cursor.execute("SELECT MAX(Nilai) FROM nilai_siswa")
                    print(f"Nilai Tertinggi: {cursor.fetchone()[0]}")
                elif sub_pilihan == "3":
                    cursor.execute("SELECT MIN(Nilai) FROM nilai_siswa")
                    print(f"Nilai terendah: {cursor.fetchone()[0]}")
                elif sub_pilihan == "4":
                    break       
                else:
                    print("Pilihan Tidak Valid, Coba Lagi!")

        elif pilihan == "2":

            while True:
                print("\n====  Statistik Umur Siswa  ====")
                print("1. Rata-rata Umur")
                print("2. Umur Tertua")
                print("3. Umur Termuda")
                print("4. Kembali ke Menu Statistik")

                sub_pilihan = input("Masukkan pilihan Anda (1-4): ")

                if sub_pilihan == "1":
                    cursor.execute("SELECT AVG(Umur) FROM nilai_siswa")
                    print(f"Rata-rata Umur: {cursor.fetchone()[0]:.2f}")
                elif sub_pilihan == "2":
                    cursor.execute("SELECT MAX(Umur) FROM nilai_siswa")
                    print(f"Umur Tertua: {cursor.fetchone()[0]}")
                elif sub_pilihan == "3":
                    cursor.execute("SELECT MIN(Umur) FROM nilai_siswa")
                    print(f"Umur Termuda: {cursor.fetchone()[0]}")
                elif sub_pilihan == "4":
                    break
                else:
                    print("Pilihan Tidak Valid, Coba Lagi!")

        elif pilihan == "3":
            break
        else:
            print("Pilihan Tidak Valid, Coba Lagi!")

def visualisasi_data():
    print("\n====  MENU VISUALISASI DATA  ====")
    print("1. Gender")
    print("2. Kelas")
    print("3. Mapel")
    print("4. Rata-rata Nilai per Mapel")
    print("5. Nilai")
    print("6. Umur")
    print("7. Top 10 Siswa")
    print("8. Kembali ke Menu Utama")

    while True:
        pilihan = input("Pilih opsi (1-8):  ")

        if pilihan == "1":
            cursor.execute("SELECT Gender, COUNT(*) FROM nilai_siswa GROUP BY Gender")
            data = cursor.fetchall()
            Gender = [row[0] for row in data]
            Jumlah = [row[1] for row in data]
            plt.pie(Jumlah, labels=Gender, autopct='%1.1f%%')
            plt.title("Proporsi Gender")
            plt.show()

        elif pilihan == "2":
            cursor.execute("SELECT Kelas, COUNT(*) FROM nilai_siswa GROUP BY Kelas")
            data = cursor.fetchall()
            Kelas = [row[0] for row in data]
            Jumlah = [row[1] for row in data]
            plt.bar(Kelas, Jumlah)
            plt.title("Jumlah Siswa per Kelas")
            plt.xlabel("Kelas")
            plt.ylabel("Jumlah Siswa")
            plt.show()

        elif pilihan == "3":
            cursor.execute("SELECT Mata_Pelajaran, COUNT(*) FROM nilai_siswa GROUP BY Mata_Pelajaran")
            data = cursor.fetchall()
            Mapel = [row[0] for row in data]
            Jumlah = [row[1] for row in data]
            plt.bar(Mapel, Jumlah)
            plt.title("Jumlah Siswa per Mata Pelajaran")
            plt.show()

        elif pilihan == "4":
            cursor.execute("SELECT Mata_Pelajaran, AVG(Nilai) FROM nilai_siswa GROUP BY Mata_Pelajaran")
            data = cursor.fetchall()
            Mapel = [row[0] for row in data]
            rata = [row[1] for row in data]
            plt.bar(Mapel, rata, color="orange")
            plt.title("Rata-rata Nilai per Mata Pelajaran")
            plt.xlabel("Mata Pelajaran")
            plt.ylabel("Rata-rata Nilai")
            plt.show()

        elif pilihan == "5":
            cursor.execute("SELECT Nilai FROM nilai_siswa")
            data = cursor.fetchall()
            Nilai = [row[0] for row in data]
            plt.hist(Nilai, bins=5,color="green",edgecolor="black")
            plt.title("Distribusi Nilai Siswa")
            plt.xlabel("Nilai")
            plt.ylabel("Frekuensi")
            plt.show()

        elif pilihan == "6":
            cursor.execute("SELECT Umur FROM nilai_siswa")
            data = cursor.fetchall()
            Umur = [row[0] for row in data]
            plt.hist(Umur,bins=5,color="blue",edgecolor="black")
            plt.title("Distribusi Umur Siswa")
            plt.xlabel("Umur")
            plt.ylabel("Frekuensi")
            plt.show()

        elif pilihan == "7":
            cursor.execute("SELECT Nama,Nilai FROM nilai_siswa")
            data = cursor.fetchall()
            Nama = [row[0] for row in data]
            Nilai = [row[1] for row in data]
            plt.bar(Nama,Nilai,color="purple")
            plt.title("Top 10 Siswa berdasarkan Nilai")
            plt.xlabel("Nama Siswa")
            plt.ylabel("Nilai Siswa")
            plt.xticks(rotation=45) 
            plt.show()

        elif pilihan == "8":
            break
        
        else:
            print("Pilihan Tidak Valid, Coba Lagi!")

def menu_utama():
    while True:
        print("\n=====  Menu Utama  =====")
        print("1. Tampilkan data siswa")
        print("2. Tambahkan siswa baru")
        print("3. Statistik data")
        print("4. Visualisasi data")
        print("5. Keluar dari program")

        pilihan = input("Masukkan pilihan anda (1-5): ")

        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            tambah_siswa()
        elif pilihan == "3":
            hitung_statistik()
        elif pilihan == "4":
            visualisasi_data()
        elif pilihan == "5":
            print("Program Selesai. Terima kasih :) ")
            break
        else:
            print("Pilihan tidak valid, coba lagi!!")    

if __name__ == "__main__":
    menu_utama()               