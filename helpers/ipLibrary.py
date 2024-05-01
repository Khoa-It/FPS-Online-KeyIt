import subprocess
import re

def get_ipv4_address():
    try:
        # Gọi lệnh ipconfig từ terminal và lấy đầu ra
        result = subprocess.run(['ipconfig'], capture_output=True, text=True)
        output = result.stdout
        # Sử dụng biểu thức chính quy để tìm địa chỉ IPv4
        ipv4_pattern = r'IPv4 Address[^\d]+(\d+\.\d+\.\d+\.\d+)'
        matches = re.findall(ipv4_pattern, output)
        if matches:
            # Trả về địa chỉ IPv4 cuối cùng
            return matches[-1]
        else:
            return None
    except Exception as e:
        print("Can not recieve your ip.", e)
        return None

# Lấy và in địa chỉ IPv4 cuối cùng
ipv4_address = get_ipv4_address()
if ipv4_address:
    print("your ip v4 is: ", ipv4_address)
else:
    print("Can not recieve your ip.")
