# latihan.py
daftar_belanja=[]

def tambahan_item(item):
    daftar_belanja.append(item)
    print (f'"{item}"telah ditambahkan ke daftar belanja.')
def tampilkan_daftar():
    if daftar_belanja:
        print("\nDaftar Belanja.")
        for i, item in enumerate(daftar_belanja,1):
            print(f"{i}. {item}")
    else:
        print("\nDaftar Belanja kosong.")
def hapus_item(index):
    if 0 <= index < len(daftar_belanja):
        item = daftar_belanja.pop(index)
        print(f'"{item}" telah dihapus dari dafftar belanja.')
    else:
        print("Indeks tidak valid.")

while True:
    print("\nMenu: ")
    print("1. Tambah Item: ")
    print("2. Lihat Daftar Belanja: ")
    print("3. Hapus Item: ")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        item = input("Masukkan nama item: ")
        tambahan_item(item)
    elif pilihan == "2":
        tampilkan_daftar()
    elif pilihan == "3":
        tampilkan_daftar()
        index = int(input("Masukkan nomor item yang ingin di hapus: "))
        hapus_item(index)
    elif pilihan == "4":
        print("Terimakasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid, silahkan coba lagi.")