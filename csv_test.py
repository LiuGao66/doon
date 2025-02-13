import re
import csv
from collections import defaultdict

def parse_fortinet_config(config):
    objects = defaultdict(dict)
    current_object = None

    # 정규 표현식을 사용하여 구성 요소를 찾습니다.
    for line in config.splitlines():
        line = line.strip()

        # 오브젝트 항목의 시작을 찾습니다.
        object_match = re.match(r'config firewall address', line)
        if object_match:
            current_object = None  # 새로운 오브젝트 시작
            
        object_name_match = re.match(r'edit (\S+)', line)
        if object_name_match:
            current_object = object_name_match.group(1)  # 오브젝트 이름 저장
            objects[current_object]['type'] = 'address'  # 기본 타입 설정

        # 오브젝트의 속성을 찾습니다.
        if current_object:
            if re.match(r'set subnet', line):
                subnet_match = re.match(r'set subnet (\S+)', line)
                if subnet_match:
                    objects[current_object]['subnet'] = subnet_match.group(1)

            elif re.match(r'set type', line):
                type_match = re.match(r'set type (\S+)', line)
                if type_match:
                    objects[current_object]['type'] = type_match.group(1)

            elif re.match(r'set comment', line):
                comment_match = re.match(r'set comment "(.*)"', line)
                if comment_match:
                    objects[current_object]['comment'] = comment_match.group(1)

        # 오브젝트 종료를 찾습니다.
        if line == 'next':
            current_object = None

    return objects

def save_to_csv(objects, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # CSV 헤더 작성
        writer.writerow(['Object Name', 'Type', 'Subnet', 'Comment'])

        # 각 오브젝트의 정보를 CSV 파일에 작성
        for obj_name, obj_info in objects.items():
            writer.writerow([
                obj_name,
                obj_info.get('type', ''),
                obj_info.get('subnet', ''),
                obj_info.get('comment', '')
            ])

def print_objects(objects):
    for obj_name, obj_info in objects.items():
        print(f"Object: {obj_name}")
        for key, value in obj_info.items():
            print(f"  {key}: {value}")
        print("")

# 예시 Fortinet 구성
fortinet_config = """
config firewall address
    edit "Non_DLP"
        set uuid 5f2233fe-9310-51ed-db10-4a069dd415ef
        set member "10.213.226.17/32" "10.213.8.101-10.213.8.107" "10.213.8.113-10.213.8.117" "10.213.8.150/32" "10.213.8.71-10.213.8.74" "10.213.8.83/32" "10.213.9.51-10.213.9.52" "10.214.132.177-10.214.132.179" "10.214.132.182/32" "10.214.132.184/32" "10.214.132.35/32" "10.214.132.62/32" "10.214.132.71/32" "10.214.218.38/32" "10.214.219.51/32" "10.215.114.131-10.215.114.132" "10.222.111.2/32" "10.225.138.92/32" "10.225.22.140/32" "147.6.133.146/32" "147.6.133.147/32" "147.6.133.218/32" "147.6.133.38/32" "147.6.133.53/32" "147.6.133.68/32" "147.6.133.74/32" "168.248.169.151-168.248.169.152" "172.16.252.83-172.16.252.84" "172.23.36.141/32" "10.214.132.73/32" "147.6.133.175/32" "147.6.133.50/32" "147.6.133.86/32" "147.6.133.98/32" "147.6.133.114/32" "10.200.224.96-10.200.224.97"
    next
end
"""

# 구성 파싱
objects = parse_fortinet_config(fortinet_config)

# 결과 출력
print_objects(objects)

# CSV 파일로 저장
save_to_csv(objects, 'fortinet_objects.csv')
print("오브젝트 정보가 'fortinet_objects.csv' 파일에 저장되었습니다.")
