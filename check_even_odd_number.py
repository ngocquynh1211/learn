# check_even_odd_number.py

def main():
    # Nhập số từ người dùng và chuyển sang kiểu float
    a = float(input("Nhập vào một số: "))

    # Kiểm tra tính chẵn lẻ của số nhập vào
    if a % 2 == 0:
        print('Số chẵn')
    elif a % 2 == 1:
        print('Số lẻ')
    else:
        print('Không phải số tự nhiên')

# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
