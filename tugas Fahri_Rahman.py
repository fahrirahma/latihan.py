# mensimulasikan printer yang mencetak dokumen
class Queue:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def is_full(self):
        return len(self.items) == self.max_size

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def display(self):
        if not self.is_empty():
            return self.items
        else:
            return "Queue is empty"


def main():
    Q = Queue(5)  # Maksimal 5 dokumen dalam antrian
    while True:
        print("\nMenu")
        print("1. Masukkan dokumen Anda")
        print("2. Cetak dokumen")
        print("3. Tampilkan dokumen dalam antrian")
        print("4. Hapus semua dokumen dalam antrian")
        print("5. Keluar")
        try:
            pilihan = int(input("Masukkan pilihan Anda: "))
            if pilihan == 1:
                item = input("Masukkan nama dokumen Anda: ")
                if not Q.is_full():
                    Q.enqueue(item)
                    print(f"Dokumen '{item}' telah ditambahkan ke antrian.")
                else:
                    print("Antrian penuh! Tidak dapat menambahkan dokumen.")
            elif pilihan == 2:
                if not Q.is_empty():
                    dokumen_dicetak = Q.dequeue()
                    print(f"Dokumen '{dokumen_dicetak}' sedang dicetak...")
                else:
                    print("Antrian kosong! Tidak ada dokumen untuk dicetak.")
            elif pilihan == 3:
                print("Dokumen dalam antrian:", Q.display())
            elif pilihan == 4:
                Q.items.clear()
                print("Semua dokumen dalam antrian telah dihapus.")
            elif pilihan == 5:
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid!")


if __name__ == "__main__":
    main()