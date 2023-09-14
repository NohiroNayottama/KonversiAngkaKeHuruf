# Kalkulator Angka ke Huruf

def welcome():
    print('''
Selamat datang di Program Konversi Nilai Angka menjadi Nilai Huruf

          Programmed by Nohiro
''')




def konversi(operasi):
    
    if operasi >= 90:
        return 'A'
    elif operasi >= 70:
        return 'B'
    elif operasi >= 60:
        return 'C'
    elif operasi >= 40:
        return 'D'
    else:
        return 'F'
    
def main():
    welcome()

    while True:
        try:
            operasi = float(input('''
Masukkan Nilai Angka yang ingin anda konversi menjadi Nilai Huruf: 
'''))
            if 0 <= operasi <= 100:
                break

            else:
                print('Angka yang dimasukkan harus diantara 0-100')

        except ValueError:
            print('Masukkan Angka yang valid')


    hasil_operasi = konversi(operasi)
    
    print(f'Hasil dari Nilai Angka {operasi} adalah Nilai Huruf {hasil_operasi}')

    
    konv_lagi = input('''
Gunakan kembali? Mohon Ketik Y untuk YES atau N untuk NO
''')
    
    if konv_lagi.upper() == 'Y':
        main()
    elif konv_lagi.upper() == 'N':
        print('''
Terima kasih sudah menggunakan program ini :)

Programmed by Nohiro
''')
    else:
        print('Input data tidak valid, Program selesai.')

if __name__ == "__main__":
    main()