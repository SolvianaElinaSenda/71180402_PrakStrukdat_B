from math import factorial

masuk=int(input("Masukan Range Data:"))
faktorial=1
# menghitung faktorial dari bilangan yang dimasukan
for i in range(1,masuk+1):
    faktorial*=i

    if i % 2 == 0:
    #ambil bilangan yang genap-nya
        hasil=f'{i} : {faktorial}'
        print(hasil)
    tampil=int(input("Masukan Data yang Ingin Ditampilkan:"))
        # if tampil>i:
        #     input("Data Tidak Ditemukan")






