# weekday_converter.py

def main():
    # Nhập số từ người dùng và chuyển sang kiểu int
    num = int(input("Nhập vào một số từ 1 đến 7: "))

    # Kiểm tra số nhập vào và in ra ngày tương ứng
    if num == 1:
        print("Monday")
    elif num == 2:
        print("Tuesday")
    elif num == 3:
        print("Wednesday")
    elif num == 4:
        print("Thursday")
    elif num == 5:
        print("Friday")
    elif num == 6:
        print("Saturday")
    elif num == 7:
        print("Sunday")
    else:
        print("error, out of range")

# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
