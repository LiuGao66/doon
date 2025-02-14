import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entimport csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
ries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entimport csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
import csv

# 입력 파일과 출력 파일 설정
input_file_path = 'fortinet_config.txt'  # 포티넷 설정 파일 경로
output_file_path = 'fortinet_config.csv'  # 출력 CSV 파일 경로

def extract_config(input_path):
    config_entries = []
    current_object = {}

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                # 'edit' 줄을 만나면 새로운 오브젝트 시작
                if line.startswith('edit'):
                    if current_object:  # 이전 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 이전 오브젝트 저장
                    # 이름 추출
                    parts = line.split('"')
                    if len(parts) > 1:
                        current_object = {'object name': parts[1]}  # 오브젝트 이름 저장
                    else:
                        current_object = {'object name': 'Unnamed'}  # 이름이 없을 경우 기본값 설정
                elif line.startswith('set'):
                    # 'set' 줄의 키와 값을 추출
                    parts = line.split()
                    if len(parts) > 2:
                        key = parts[1].lower()  # 키를 소문자로 변환
                        value = ' '.join(parts[2:]).strip().strip('"')
                        current_object[key] = value  # 모든 키-값 쌍 저장
                elif line.startswith('next'):
                    if current_object:  # 현재 오브젝트가 존재하는 경우
                        config_entries.append(current_object)  # 마지막 오브젝트 저장
                    current_object = {}

            # 마지막 오브젝트가 저장되지 않은 경우 추가
            if current_object:
                config_entries.append(current_object)

    except Exception as e:
        print(f"파일 처리 중 오류가 발생했습니다: {e}")

    return config_entries

def save_to_csv(config_entries, output_path):
    if not config_entries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
ries:
        print("저장할 설정이 없습니다.")
        return

    # 저장할 필드명 설정 (이름을 맨 앞으로 이동)
    fieldnames = ['object name'] + list(set(k for entry in config_entries for k in entry.keys() if k != 'object name'))

    # 오브젝트 이름을 기준으로 정렬
    sorted_entries = sorted(config_entries, key=lambda x: x.get('object name', ''))

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in sorted_entries:
                # 지정된 필드명에 맞추어 매핑
                formatted_obj = {field: obj.get(field, '') for field in fieldnames}
                writer.writerow(formatted_obj)

    except Exception as e:
        print(f"CSV 파일 저장 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    config_entries = extract_config(input_file_path)
    save_to_csv(config_entries, output_file_path)

    print('전체 설정이 CSV 파일로 저장되었습니다.')
