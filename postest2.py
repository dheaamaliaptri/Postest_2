from prettytable import PrettyTable

print("""
+==========================================+
|                                          |
|       WELCOME TO DY'S CHOCOLATERIE       |
|                                          |
+==========================================+
""")

# Daftar Menu Dy's Chocolaterie
daftar_menu = PrettyTable()
daftar_menu.field_names = ["No", "Menu", "Harga", "Stok"]

menu_data = [
    [1, "Passion Fruit White Chocolate Truffles", 99000, 12],
    [2, "Sea Salt Dark Chocolate Signature", 99000, 32],
    [3, "Salted Caramels & Hazelnut Chocolates", 82000, 12],
    [4, "Peanuts in Milk Caramel Chocolate", 82000, 14],
    [5, "Matcha White Chocolate Bar", 65000, 15],
    [6, "Hot Chocolate Classic in Cup", 35000, 12]
]

for item in menu_data:
    daftar_menu.add_row(item)

# Fungsi untuk menampilkan daftar menu
def read_daftarmenu():
    print(daftar_menu)

# Fungsi untuk menambahkan menu baru
def create_menu():
    nama = input("Masukkan nama produk: ")
    harga = int(input("Masukkan harga produk: "))
    stok = int(input("Masukkan stok produk: "))
    new_no = len(daftar_menu._rows) + 1
    daftar_menu.add_row([new_no, nama, harga, stok])
    read_daftarmenu()
    print("Produk baru berhasil ditambahkan!")

# Fungsi untuk memperbarui data menu
def update_menu():
    nomor = int(input("Masukkan nomor produk yang akan diupdate: "))
    for row in daftar_menu._rows:
        if int(row[0]) == nomor:
            harga = int(input("Masukkan harga produk baru: "))
            stok = int(input("Masukkan stok produk baru: "))
            row[2] = harga
            row[3] = stok
            print("Data produk berhasil diupdate!")
            break
    else:
        print("Produk tidak ditemukan.")

# Fungsi untuk menghapus menu
def delete_menu():
    nomor = int(input("Masukkan nomor produk yang akan dihapus: "))
    for menu, row in enumerate(daftar_menu._rows):
        if int(row[0]) == nomor:
            daftar_menu._rows.pop(menu)
            print("Produk berhasil dihapus!")
            read_daftarmenu()
            break
    else:
        print("Produk tidak ditemukan.")

# Fungsi transaksi pembelian
def checkout():
    read_daftarmenu()
    nomor = int(input("Masukkan nomor produk yang akan dibeli: "))
    for row in daftar_menu._rows:
        if int(row[0]) == nomor:
            jumlah = int(input("Masukkan jumlah produk yang akan dibeli: "))
            if jumlah <= int(row[3]):
                total_harga = jumlah * int(row[2])
                print(f"Total harga: Rp. {total_harga}")
                print("Pembelian berhasil!")
                row[3] -= jumlah
                break
            else:
                print("Maaf, Stok produk tidak mencukupi.")
            break
    else:
        print("Produk tidak ditemukan.")

# Main Program
while True:
    print("|--------------------------------|")
    print("|        Dy's Chocolaterie       |")
    print("|--------------------------------|")
    print("| 1. ADMIN                       |")
    print("| 2. CUSTOMER                    |")
    print("| 3. LEAVE                       |") 
    print("|--------------------------------|")

    pilihan = int(input("Masukkan pilihan : "))

    if pilihan == 1:
        pw = 'admin'
        input_pw = input("Masukkan Password Admin: ")

        if input_pw == pw:
            print("Welcome Admin! Have a Great Day :)")
            read_daftarmenu()
            print("""
+===================================+
|              Pilihan              |
+===================================+    
|    1. Create Menu                 |
|    2. Read Menu                   |
|    3. Update Menu                 |
|    4. Delete Menu                 |
|    5. Checkout                    |
|    6. Leave                       |
+===================================+
""")
            sub_pilihan = int(input("Masukkan pilihan : "))
            if sub_pilihan == 1:
                create_menu()
            elif sub_pilihan == 2:
                read_daftarmenu()
            elif sub_pilihan == 3:
                read_daftarmenu()
                update_menu()
            elif sub_pilihan == 4:
                delete_menu()
            elif sub_pilihan == 5:
                checkout()
            elif sub_pilihan == 6:
                print("""
+===================================+
|                                    |
|       YOU'VE BEEN LOGGED OUT       |                     
|                                    |
+===================================+
""")
                break
        else:
            print("Password yang Anda Masukkan Salah")
    elif pilihan == 2:
        print("Silahkan pilih produk yang Anda inginkan!")
        checkout()
    elif pilihan == 3:
        print("""
+====================================+
|                                    |
|       THANK YOU FOR VISITING       |
|           OUR SHOP !! :D           |
|                                    |
+====================================+
""")
        exit()
