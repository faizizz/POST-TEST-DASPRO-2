#! Nama: Muhammad Fa'iz
#! NIM : 2309116086


def menu():
    print('')
    print("=" * 31)
    print("SELAMAT DATANG DI MAGAZINE ZONE")
    print("=" * 31)
    print('')
    print("PILIHAN MENU : ")
    print('')
    print("1. PRODUK")
    print("2. KERANJANG")
    print("3. LOGIN (ADMIN)")
    print("4. KELUAR")
    print('')
    pilihan_menu()


def pilihan_menu():
    pilihan_menu = int(input("PILIHAN MENU (1/2/3/4) : "))

    if pilihan_menu == 1:
        kategori_magazine()
        pilihan_magazine()
    elif pilihan_menu == 2:
        tampilkan_keranjang()
    elif pilihan_menu == 3:
        loginadmin()
    elif pilihan_menu == 4:
        raise SystemExit

        
def loginadmin():
    print("")
    ID = str(input("USER ID     : "))
    PW = str(input("PASSWORD    : "))
    if ID == "admin" and PW == "admin123":
        menuadmin()
    else:
        print("ID DAN PASSWORD SALAH, SILAHKAN COBA LAGI :")
        loginadmin()
        
def menuadmin():
    print("")
    print("MENU ADMIN :\n")
    print(
            """1. LIST PRODUK
2. TAMBAH PRODUK
3. PERBARUI PRODUK
4. HAPUS PRODUK
5. KEMBALI\n"""
        )
    pilihanadmin1 = str(input("PILIHAN MENU (1/2/3/4/5) : "))
    if pilihanadmin1 == "1":
        viewtabelproduksekarang()
        print("")
        menuadmin()
    elif pilihanadmin1 == "2":
        print('')
        listprodukbaru = []
        produkbaru = input("MASUKKAN NAMA PRODUK : ")
        listprodukbaru.append(produkbaru)
        hargaprodukbaru = input("MASUKKAN HARGA PRODUK (EX. Rp 30,000): ")
        listprodukbaru.append(hargaprodukbaru)
        list_produk.append(listprodukbaru)
        print("")
        print("PRODUK BERHASIL DITAMBAHKAN :D ")
        print('')
        menuadmin()
    elif pilihanadmin1 == "3":
        viewtabelproduksekarang()
        print('')
        updatetable()
    elif pilihanadmin1 == "4":
        viewtabelproduksekarang()
        print("")
        pilihan_menghapus_produk = int(input("PILIH PRODUK YANG INGIN DIHAPUS : ")) - 1
        if 0 <= pilihan_menghapus_produk < len(list_produk):
            print("PRODUK YANG ANDA INGIN HAPUS ADALAH :")
            print(list_produk[pilihan_menghapus_produk])
            print('')
            konfirmasiadmin1 = str(input("APAKAH YAKIN INGIN MENGHAPUS PRODUK INI ? : "))
            if konfirmasiadmin1 == "Iya" :
                del list_produk[pilihan_menghapus_produk]
                menuadmin()
            elif konfirmasiadmin1 == "iya" :
                del list_produk[pilihan_menghapus_produk]
                menuadmin()
            elif konfirmasiadmin1 == "IYA" :
                del list_produk[pilihan_menghapus_produk]
                menuadmin()
            elif konfirmasiadmin1 == "Ya" :
                del list_produk[pilihan_menghapus_produk]
                menuadmin()
            elif konfirmasiadmin1 == "YA" :
                del list_produk[pilihan_menghapus_produk]
                menuadmin()
            elif konfirmasiadmin1 == "ya" :
                del list_produk[pilihan_menghapus_produk]
                menuadmin()
            else:
                print('')
                print("TIDAK VALID, ANDA DIKEMBALIKAN KE MENU")
                menuadmin()
    elif pilihanadmin1 == "5":
        menu()
        pilihan_menu()
    else:
        print("")
        print("TIDAK VALID, ANDA DIKEMBALIKAN KE MENU")
        menuadmin()

            
    
def tabelproduksekarang():
    from prettytable import PrettyTable
    tablelistproduk = PrettyTable()
    tablelistproduk.field_names = ("No.", "NAMA PRODUK", "HARGA PRODUK")
    for i, row in enumerate(list_produk, start=1):
        tablelistproduk.add_row([i] + row)

def viewtabelproduksekarang():
    from prettytable import PrettyTable
    tablelistproduk = PrettyTable()
    tablelistproduk.field_names = ("No.", "NAMA PRODUK", "HARGA PRODUK")
    for i, row in enumerate(list_produk, start=1):
        tablelistproduk.add_row([i] + row)
    print(tablelistproduk)

def updatetable():
    from prettytable import PrettyTable
    tablelistproduk = PrettyTable()
    noproduk = int(input("PILIH PRODUK YANG INGIN DIGANTI/DIPERBARUI : " )) - 1
    if 0 <= noproduk < len(list_produk):
        tabelproduksekarang()
        produkbaru = input("MASUKKAN NAMA PRODUK : ")
        hargaprodukbaru = str(input("MASUKKAN HARGA PRODUK (EX. Rp. 30.000): "))
        produkupdate = [produkbaru, hargaprodukbaru]
        tablelistproduk.clear_rows()
        list_produk[noproduk - 1] = produkupdate
        tablelistproduk.add_rows(list_produk)
        print('')
        print("LIST PRODUK TERBARU : ")
        viewtabelproduksekarang()
        menuadmin()
    else:
        print("Indeks produk tidak valid.")


def produkditambahkan():
    print('')
    print("PRODUK DITAMBAHKAN KE KERANJANG ANDA") 
    menu()


def tampilkan_keranjang():
    
    if len(keranjang_pembeli) == 0:
        print('')
        print("BELUM ADA PRODUK YANG DITAMBAHKAN KE KERANJANG")
        menu()
        pilihan_menu()
    elif len(keranjang_pembeli) != 0:
        from prettytable import PrettyTable
        table = PrettyTable()
        table.field_names = ("No.", "NAMA PRODUK", "HARGA PRODUK")
        for i, row in enumerate(keranjang_pembeli, start=1):
            table.add_row([i] + row)
        print(table)
        print("")
        print(
            """1. Lanjut Pembayaran
2. Kembali\n"""
)
        pilihanlanjutan()
        

def pilihanlanjutan():
    userinput222 = int(input("PILIHAN ANDA : "))
    if userinput222 == 1:
            print("TERIMA KASIH SUDAH BERBELANJA DI TOKO KAMI")
    elif userinput222 == 2:
            menu()
            pilihan_menu()
    else:
            print('SILAHKAN COBA LAGI')
            pilihanlanjutan()


def kategori_magazine():
    print('')
    print("PILIHAN KATEGORI MAJALAH DI MAGAZINE ZONE : ")
    print('')
    viewtabelproduksekarang()
    print('')
    

def pilihan_magazine():
    pilihan_kategori_magazine = int(input("PILIHAN KATEGORI MAJALAH :"))

    if pilihan_kategori_magazine == 1:
        produk1()
    elif pilihan_kategori_magazine == 2:
        produk2()
    elif pilihan_kategori_magazine == 3:
        produk3()
    elif pilihan_kategori_magazine == 4:
        produk4()
    elif pilihan_kategori_magazine == 5:
        produk5()
    elif pilihan_kategori_magazine == 6:
        produk6()
    elif pilihan_kategori_magazine == 7:
        produk7()


def produk1():
    print('')
    print("Deskripsi Produk :\n")
    print("Majalah ini membawa Anda ke dunia fashion terkini")
    print("memberikan inspirasi gaya hidup")
    print("dan memperkenalkan tren terkini")
    print("Dari wawasan designer hingga tips fashion sehari-hari") 
    print("selalu siap mempercantik penampilan Anda.") 
    print('')
    print("Produk   : MAGAZINE LIFESTYLE")
    print(str("Harga    : Rp 20,000\n"))
    produkpilihan = ["MAGAZINE LIFESTYLE", "Rp 20,000"]
    masukan_keranjang = str(input("Apakah anda ingin menambahkan majalah ini ke keranjang? (Ya/Tidak) : "))
    if masukan_keranjang == "Ya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "ya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "iya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "Iya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "Tidak":
        menu()
    elif masukan_keranjang == "tidak":
        menu()
    else:
        tidak_valid_keranjang1()

def produk2():
    print('')
    print("Deskripsi Produk :\n")
    print("Temukan rahasia kesehatan optimal ")
    print("dan kebugaran fisik melalui majalah ini")
    print("Dari artikel kesehatan terkini hingga resep makanan sehat")
    print("Kami dapat menginspirasi Anda untuk hidup sehat dan aktif")
    print('')
    print("Produk   : MAGAZINE KESEHATAN DAN KEBUGARAN")
    print(str("Harga    : Rp 20,000\n"))
    produkpilihan = ["MAGAZINE KESEHATAN DAN KEBUGARAN", "Rp 20,000"]
    masukan_keranjang = str(input("Apakah anda ingin menambahkan majalah ini ke keranjang? (Ya/Tidak) : "))
    if masukan_keranjang == "Ya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "ya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "iya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "Iya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "Tidak":
        menu()
    elif masukan_keranjang == "tidak":
        menu()
    else:
        tidak_valid_keranjang2()

def produk3():
    print('')
    print("Deskripsi Produk :\n")
    print("Menjadi yang pertama mengetahui tentang perkembangan teknologi ")
    print("terbaru dan temukan keindahan dunia ilmu pengetahuan")
    print("Majalah ini membawa Anda pada perjalanan")
    print("eksplorasi teknologi, inovasi, dan temuan ilmiah terbaru")
    print('')
    print("Produk   : MAGAZINE TEKNOLOGI DAN SAINS")
    print(str("Harga    : Rp 20,000\n"))
    produkpilihan = ["MAGAZINE TEKNOLOGI DAN SAINS", "Rp 20,000"]
    masukan_keranjang = str(input("Apakah anda ingin menambahkan majalah ini ke keranjang? (Ya/Tidak) : "))
    if masukan_keranjang == "Ya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "ya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "iya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "Iya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "Tidak":
        menu()
    elif masukan_keranjang == "tidak":
        menu()
    else:
        tidak_valid_keranjang3()

def produk4():
    print('')
    print("Deskripsi Produk :\n")
    print("Jelajahi dunia melalui halaman-halaman majalah ini")
    print("Dari destinasi wisata eksotis hingga petualangan tak terlupakan")
    print("kami membawa Anda ke tempat-tempat")
    print("yang menakjubkan dan memberikan tips untuk perjalanan Anda")
    print('')
    print("Produk   : MAGAZINE TRAVEL DAN PETUALANGAN")
    print(str("Harga    : Rp 20,000\n"))
    produkpilihan = ["MAGAZINE TRAVEL DAN PETUALANGAN", "Rp 20,000"]
    masukan_keranjang = str(input("Apakah anda ingin menambahkan majalah ini ke keranjang? (Ya/Tidak) : "))
    if masukan_keranjang == "Ya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "ya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "iya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "Iya":
        keranjang_pembeli.append(produkpilihan)
        produkditambahkan()
    elif masukan_keranjang == "Tidak":
        menu()
    elif masukan_keranjang == "tidak":
        menu()
    else:
        tidak_valid_keranjang4()

def produk5():
        print('')
        print("Deskripsi Produk :\n")
        print("Dapatkan liputan eksklusif tentang dunia olahraga")
        print("Dari berita terkini hingga profil atlet")
        print("majalah ini menyajikan segala hal")
        print("tentang olahraga favorit Anda")
        print('')
        print("Produk   :  MAGAZINE OLAHRAGA")
        print(str("Harga    : Rp 20,000\n"))
        produkpilihan = ["MAGAZINE OLAHRAGA", "Rp 20,000"]
        masukan_keranjang = str(input("Apakah anda ingin menambahkan majalah ini ke keranjang? (Ya/Tidak) : "))
        if masukan_keranjang == "Ya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "ya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "iya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "Iya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "Tidak":
            menu()
        elif masukan_keranjang == "tidak":
            menu()
        else:
            tidak_valid_keranjang5()
def produk6():
        print('')
        print("Deskripsi Produk :\n")
        print("Dengarkan irama musik dan cerita hiburan melalui majalah ini")
        print("Dari wawancara musisi terkenal")
        print("hingga ulasan konser")
        print("kami membawa Anda ke dunia musik dan hiburan")
        print('')
        print("Produk   :  MAGAZINE MUSIK DAN HIBURAN")
        print(str("Harga    : Rp 20,000\n"))
        produkpilihan = ["MAGAZINE MUSIK DAN HIBURAN", "Rp 20,000"]
        masukan_keranjang = str(input("Apakah anda ingin menambahkan majalah ini ke keranjang? (Ya/Tidak) : "))
        if masukan_keranjang == "Ya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "ya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "iya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "Iya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "Tidak":
            menu()
        elif masukan_keranjang == "tidak":
            menu()
        else:
            tidak_valid_keranjang6()
def produk7():
        print('')
        print("Deskripsi Produk :\n")
        print("Jelajahi dunia rasa dan kelezatan melalui majalah ini")
        print("Dengan resep masakan dari berbagai belahan dunia")
        print("hingga ulasan restoran")
        print("kami memenuhi selera kuliner Anda")
        print('')
        print("Produk   :  MAGAZINE KULINER DAN MASAKAN")
        print(str("Harga    : Rp 20,000\n"))
        produkpilihan = ["MAGAZINE KULINER DAN MASAKAN", "Rp 20,000"]
        masukan_keranjang = str(input("Apakah anda ingin menambahkan majalah ini ke keranjang? (Ya/Tidak) : "))
        if masukan_keranjang == "Ya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "ya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "iya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "Iya":
            keranjang_pembeli.append(produkpilihan)
            produkditambahkan()
        elif masukan_keranjang == "Tidak":
            menu()
        elif masukan_keranjang == "tidak":
            menu()
        else:
            tidak_valid_keranjang7()

def tidak_valid_keranjang1():
    print('')
    print("=" * 33)
    print("TIDAK VALID, SILAHKAN COBA LAGI :")
    print("=" * 33)
    produk1()
def tidak_valid_keranjang2():
    print('')
    print("=" * 33)
    print("TIDAK VALID, SILAHKAN COBA LAGI :")
    print("=" * 33)
    produk2()
def tidak_valid_keranjang3():
    print('')
    print("=" * 33)
    print("TIDAK VALID, SILAHKAN COBA LAGI :")
    print("=" * 33)
    produk3()
def tidak_valid_keranjang4():
    print('')
    print("=" * 33)
    print("TIDAK VALID, SILAHKAN COBA LAGI :")
    print("=" * 33)
    produk4()
def tidak_valid_keranjang5():
    print('')
    print("=" * 33)
    print("TIDAK VALID, SILAHKAN COBA LAGI :")
    print("=" * 33)
    produk5()
def tidak_valid_keranjang6():
    print('')
    print("=" * 33)
    print("TIDAK VALID, SILAHKAN COBA LAGI :")
    print("=" * 33)
    produk6()
def tidak_valid_keranjang7():
    print('')
    print("=" * 33)
    print("TIDAK VALID, SILAHKAN COBA LAGI :")
    print("=" * 33)
    produk7()

keranjang_pembeli = []  
list_produk = [
    ["MAGAZINE LIFESTYLE", "Rp. 20.000"],
    ["MAGAZINE KESEHATAN DAN KEBUGARAN", "Rp. 20.000"],
    ["MAGAZINE TEKNOLOGI DAN SAINS", "Rp. 20.000"],
    ["MAGAZINE TRAVEL DAN PETUALANGAN", "Rp. 20.000"],
    ["MAGAZINE OLAHRAGA", "Rp. 20.000"],
    ["MAGAZINE MUSIK DAN HIBURAN", "Rp. 20.000"],
    ["MAGAZINE KULINER DAN MASAKAN", "Rp. 20.000"]
]

menu()

        


