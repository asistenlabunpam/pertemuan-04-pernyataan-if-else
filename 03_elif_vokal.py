# Program Pengecekan Huruf Vokal Menggunakan Elif

def cek_vokal(huruf):
    huruf = huruf.lower()
    if huruf == 'a':
        print("Ini adalah huruf vokal -a-")
    elif huruf == 'e':
        print("Ini adalah huruf vokal -e-")
    elif huruf == 'i':
        print("Ini adalah huruf vokal -i-")
    elif huruf == 'o':
        print("Ini adalah huruf vokal -o-")
    elif huruf == 'u':
        print("Ini adalah huruf vokal -u-")
    else:
        print(f"Karakter '{huruf}' bukan huruf vokal")

if __name__ == "__main__":
    test_huruf = ['a', 'e', 'i', 'o', 'u', 'x']
    for h in test_huruf:
        cek_vokal(h)
