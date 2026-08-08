# Program Menentukan Bilangan Genap atau Ganjil

def cek_genap_ganjil(bilangan):
    if bilangan % 2 == 0:
        print(f"Bilangan {bilangan} adalah GENAP")
    else:
        print(f"Bilangan {bilangan} adalah GANJIL")

if __name__ == "__main__":
    algoritma = 'Struktur Data'
    if algoritma == 'Struktur Data':
        print("Belajar Algoritma dan Struktur Data!")
    else:
        print("Belum belajar")

    # Pengujian fungsi
    cek_genap_ganjil(10)
    cek_genap_ganjil(7)
