
rak_buku = {
    "Rak 1 (max 4)": [],
    "Rak 2 (max 4)": []
}

def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    while True:
        try:
            tahun = int(input("Masukkan tahun terbit: "))
            break
        except ValueError:
            print("Tahun terbit harus berupa angka.")
    buku = {"judul": judul, "penulis": penulis, "tahun": tahun}

    rak_tersedia = [rak for rak in rak_buku if len(rak_buku[rak]) < 4]
    if rak_tersedia:
        for i, rak in enumerate(rak_tersedia, 1):
            print(f"{i}. {rak}")
        while True:
            try:
                pilihan_rak = int(input("Pilih rak untuk menambahkan buku (masukkan nomor rak): ")) - 1
                if pilihan_rak < 0 or pilihan_rak >= len(rak_tersedia):
                    print("Pilihan rak tidak valid. Silakan masukkan nomor rak yang benar.")
                else:
                    rak_buku[rak_tersedia[pilihan_rak]].append(buku)
                    print(f"Buku '{judul}' berhasil ditambahkan ke {rak_tersedia[pilihan_rak]}")
                    break
            except ValueError:
                print("Masukkan harus berupa angka.")
    else:
        print("Semua rak penuh! Tidak bisa menambahkan buku.")

def cari_buku(kata_kunci, kriteria):
    hasil = [buku for rak in rak_buku.values() for buku in rak if kata_kunci.lower() in buku[kriteria].lower()]
    return sorted(hasil, key=lambda x: (x['tahun'], x['judul'].lower(), x['penulis'].lower()))

def tampilkan_buku(buku_buku):
    if not buku_buku:
        print("Tidak ada buku yang ditemukan.")
    else:
        for buku in buku_buku:
            print(f"Judul: {buku['judul']}, Penulis: {buku['penulis']}, Tahun: {buku['tahun']}")

def tampilkan_semua_buku():
    semua_buku = [buku for rak in rak_buku.values() for buku in rak]
    tampilkan_buku(sorted(semua_buku, key=lambda x: (x['tahun'], x['judul'].lower(), x['penulis'].lower())))

def hapus_buku():
    judul = input("Masukkan judul buku yang ingin dihapus: ")
    for rak in rak_buku.values():
        for buku in rak:
            if judul.lower() == buku["judul"].lower():
                rak.remove(buku)
                print(f"Buku '{judul}' berhasil dihapus.")
                return
    print(f"Buku '{judul}' tidak ditemukan.")

def main():
    while True:
        print("\nMenu Perpustakaan:")
        for i, menu in enumerate(["Tambah Buku", "Cari Buku", "Hapus Buku", "Tampilkan Semua Buku", "Keluar"], 1):
            print(f"{i}. {menu}")
        while True:
            try:
                pilihan = int(input("Pilih menu (1/2/3/4/5): "))
                if pilihan < 1 or pilihan > 5:
                    raise ValueError
                break
            except ValueError:
                print("Pilihan tidak valid. Silakan masukkan nomor menu yang benar.")

        if pilihan == 1:
            tambah_buku()
        elif pilihan == 2:
            print("Cari berdasarkan:")
            for i, kriteria in enumerate(["Judul", "Penulis", "Tahun"], 1):
                print(f"{i}. {kriteria}")
            while True:
                try:
                    pilihan_kriteria = int(input("Pilih kriteria (1/2/3): "))
                    if pilihan_kriteria == 1:
                        kriteria = "judul"
                    elif pilihan_kriteria == 2:
                        kriteria = "penulis"
                    elif pilihan_kriteria == 3:
                        kriteria = "tahun"
                    else:
                        raise ValueError
                    break
                except ValueError:
                    print("Pilihan kriteria tidak valid. Silakan masukkan nomor kriteria yang benar.")
            kata_kunci = input(f"Masukkan kata kunci {kriteria}: ")
            tampilkan_buku(cari_buku(kata_kunci, kriteria))
        elif pilihan == 3:
            hapus_buku()
        elif pilihan == 4:
            tampilkan_semua_buku()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan perpustakaan!")
            break

if __name__ == "__main__":
    main()