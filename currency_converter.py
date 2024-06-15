# currency_converter.py

def main():
    # Bước 1: Nhập số tiền USD cần đổi
    usd_amount = float(input("Nhập số tiền USD cần đổi: "))

    # Bước 2: Nhập tỉ giá USD/VND
    exchange_rate = float(input("Nhập tỉ giá USD/VND: "))

    # Bước 3: Tính toán số tiền VND theo tỉ giá và số tiền USD nhập vào
    vnd_amount = usd_amount * exchange_rate

    # Bước 4: In ra kết quả
    print(f"{usd_amount} USD tương đương với {vnd_amount} VND")

# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
