# main.py

def print_hello_mars():
    print('Hello Mars')

def read_log_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"에러: '{file_path}' 파일을 찾을 수 없습니다.")
        return []
    except Exception as e:
        print(f"알 수 없는 오류 발생: {e}")
        return []

def display_logs(logs):
    print('\n전체 로그 출력:')
    for log in logs:
        print(log.strip())

def write_markdown_report(logs, report_path):
    try:
        with open(report_path, 'w', encoding='utf-8') as file:
            file.write('# 전체 로그 내역\n')
            for log in logs:
                file.write(f'- {log.strip()}\n')
            file.write('\n')
    except Exception as e:
        print(f"보고서 작성 중 오류 발생: {e}")

def sort_logs_descending(logs):
    sorted_logs = sorted(logs, key=lambda x: x.split(',')[0], reverse=True)
    print('\n시간 역순 정렬된 로그')
    for log in sorted_logs:
        print(log.strip())
    return sorted_logs

def extract_issue_logs(logs):
    issue_logs = []
    for log in logs:
        if 'unstable' in log.lower() or 'explosion' in log.lower():
            issue_logs.append(log.strip())
    return issue_logs

def save_to_file(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in data:
                file.write(line + '\n')
    except Exception as e:
        print(f"파일 저장 중 오류 발생: {e}")

# 메인 실행
if __name__ == '__main__':
    print_hello_mars()

    log_file = 'mission_computer_main.log'
    report_file = 'log_analysis.md'
    issue_file = 'issue_logs.txt'

    logs = read_log_file(log_file)

    if logs:
        display_logs(logs)             
        sorted_logs = sort_logs_descending(logs) 
        issue_logs = extract_issue_logs(logs)   

        # 결과 저장
        save_to_file(issue_logs, issue_file) 
        write_markdown_report(logs, report_file) 
