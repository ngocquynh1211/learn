# Nhập số nguyên từ người dùng
num_check = int(input("Nhập vào một số nguyên: "))

# Sử dụng toán tử ba ngôi để kiểm tra và in ra kết quả
msg = "Even" if num_check % 2 == 0 else "Odd"
print(msg)
