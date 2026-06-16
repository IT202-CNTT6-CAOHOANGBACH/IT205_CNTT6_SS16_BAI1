""" 
Phân tích lỗi
    - Hai dòng lệnh raw_diagnosis.strip() và raw_diagnosis.title() trong hàm không hề làm thay đổi giá trị của biến raw_diagnosis vì
    trong Python, String là immutable (bất biến). Điều này nghĩa là mọi thao tác như strip(), title(), upper()… sẽ trả về một chuỗi mới
    chứ không sửa trực tiếp chuỗi ban đầu. 
    -> Để các hàm xử lý chuỗi ở trên thực sự phát huy tác dụng và chuỗi mới được lưu lại, ta cần sửa lại cú pháp gán biến :
    raw_diagnosis = raw_diagnosis.strip()
    raw_diagnosis = raw_diagnosis.title()
    
    - Phương thức extend() của List coi chuỗi là một iterable (tập hợp các ký tự). Do đó, nó sẽ thêm từng ký tự riêng lẻ vào list.
    -> Để thêm nguyên vẹn một chuỗi vào list, ta dùng append(). 
"""

# Sửa lỗi
# Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
patient_diagnoses = ["Sốt Xuất Huyết"]

# Hàm chuẩn hóa tên bệnh và thêm vào hồ sơ
def add_diagnosis(raw_diagnosis, current_list):
    # Chuẩn hóa tên bệnh: xóa khoảng trắng thừa và viết hoa chữ cái đầu mỗi từ
    raw_diagnosis = raw_diagnosis.strip()
    raw_diagnosis = raw_diagnosis.title()
    
    # Thêm chẩn đoán vào danh sách bệnh án
    current_list.append(raw_diagnosis)
    return current_list

# Bác sĩ nhập thêm một chẩn đoán mới bị lỗi định dạng
new_diagnosis = "  viEm phE QUan  "

# Gọi hàm để xử lý và cập nhật hồ sơ
updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)
print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)