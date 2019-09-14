def cetak_gambar(n):
    if ((n%2 != 0) & (n>1)):
        sep = '   '
        n_setengah = n//2
        panjang = (n * 4) - 14
        panjang_garis = panjang//2
        
        print (' ', end='')
        if (panjang_garis > 0):
            print ('=' * panjang_garis, end=' ')
        print ('panjang', end=' ')
        if (panjang_garis > 0):
            print ('=' * panjang_garis, end='')
        print()
            
        for _ in range(0,n_setengah):
            print('*', end=sep)
            for _ in range(2,n):
                print ('=', end=sep)
            print('*')
        
        for _ in range(n):
            print('*', end=sep)
        print()        
        
        for _ in range(0,n_setengah):
            print('*', end=sep)
            for _ in range(2,n):
                print ('=', end=sep)
            print('*')
    else:
        print('input salah')

cetak_gambar(5)