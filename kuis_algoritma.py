# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa (Andi/Budi/Citra): ").capitalize()

# Menentukan target nilai
if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    target = 0
    print("Nama mahasiswa tidak ditemukan!")

if target != 0:
    print("Nama Mahasiswa\t\t:", nama)
    print("Target Nilai\t\t:", target)

    percobaan = 1
    lulus = False

    # Perulangan maksimal 3 kali
    while percobaan <= 3:
        nilai = int(input(f"\nMasukkan nilai ujian ke-{percobaan}: "))

        if nilai >= target:
            lulus = True
            break
        else:
            print("Nilai belum mencapai target.")
            percobaan += 1

    # Menampilkan hasil akhir
    print("\n=== HASIL AKHIR ===")

    if lulus:
        print(nama, "berhasil lulus!")
        print("Pada percobaan ke-", percobaan)
    else:
        print(nama, "tidak lulus setelah 3 kali percobaan.")