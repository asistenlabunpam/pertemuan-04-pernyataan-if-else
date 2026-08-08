# Program Pernyataan IF Bersarang (Nested IF)

def cek_jenis_huruf(huruf):
    print(f"\nMemeriksa karakter: '{huruf}'")
    if huruf >= 'A':
        if huruf <= 'Z':
            print("Ini adalah Huruf Besar (Kapital)")
        elif huruf >= 'a':
            if huruf <= 'z':
                print("Ini adalah Huruf Kecil")
            else:
                print("Karakter > 'z'")
        else:
            print("Karakter di antara Z dan a")
    else:
        print("Karakter < 'A'")

def cari_terbesar(a, b, c):
    print(f"\nMencari nilai terbesar dari a={a}, b={b}, c={c}")
    if a > b:
        if a > c:
            besar = a
        else:
            besar = c
    elif b > c:
        besar = b
    else:
        besar = c
    print(f"Bilangan yang terbesar adalah = {besar}")

if __name__ == "__main__":
    cek_jenis_huruf('G')
    cek_jenis_huruf('m')
    cek_jenis_huruf('3')

    cari_terbesar(12, 8, 15)
