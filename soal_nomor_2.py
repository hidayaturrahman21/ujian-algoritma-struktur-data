def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print("Pilih fungsi yang ingin dijalankan:")
print("1. Faktorial")
print("2. Fibonacci")

pilihan = int(input("Masukkan pilihan (1/2): "))
n = int(input("Masukkan angka untuk dihitung: "))

if pilihan == 1:
    hasil = faktorial(n)
    print(f"Faktorial dari {n} adalah {hasil}")
    
elif pilihan == 2:
    hasil = fibonacci(n)
    print(f"Bilangan Fibonacci ke-{n} adalah {hasil}")
else:
    print("Peringatan: Hanya boleh memilih 1 atau 2!")
