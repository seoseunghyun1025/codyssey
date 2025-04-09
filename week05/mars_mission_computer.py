import random
import time
import platform
import psutil
import os
import json


class DummySensor:

    def __init__(self, name='DefaultSensor'):
        self.name = name
        print(f'{self.name}가 생성되었습니다.')

        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None,
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = round(
            random.uniform(18.0, 30.0), 2
        )
        self.env_values['mars_base_external_temperature'] = round(
            random.uniform(0.0, 21.0), 2
        )
        self.env_values['mars_base_internal_humidity'] = round(
            random.uniform(50.0, 60.0), 2
        )
        self.env_values['mars_base_external_illuminance'] = round(
            random.uniform(500.0, 715.0), 2
        )
        self.env_values['mars_base_internal_co2'] = round(
            random.uniform(0.02, 0.1), 4
        )
        self.env_values['mars_base_internal_oxygen'] = round(
            random.uniform(4.0, 7.0), 2
        )

    def get_env(self):
        year = 2025
        month = str(random.randint(1, 12)).zfill(2)
        day = str(random.randint(1, 28)).zfill(2)

        hour = str(random.randint(0, 23)).zfill(2)
        minute = str(random.randint(0, 59)).zfill(2)
        second = str(random.randint(0, 59)).zfill(2)
        fake_timestamp = f'{year}-{month}-{day} {hour}:{minute}:{second}'

        log_line = (
            f'[{fake_timestamp}] '
            f'내부온도: {self.env_values["mars_base_internal_temperature"]}°C | '
            f'외부온도: {self.env_values["mars_base_external_temperature"]}°C | '
            f'내부습도: {self.env_values["mars_base_internal_humidity"]}% | '
            f'외부광량: {self.env_values["mars_base_external_illuminance"]}W/m² | '
            f'CO2: {self.env_values["mars_base_internal_co2"]}% | '
            f'산소: {self.env_values["mars_base_internal_oxygen"]}%\n'
        )

        with open('week03/sensor_log.txt', 'a', encoding='utf-8') as file:
            file.write(log_line)

        return self.env_values


class MissionComputer:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None,
        }
        self.ds = DummySensor()
        self.accumulated_data = {key: [] for key in self.env_values}
        self.counter = 0

    def get_sensor_data(self):
        print('센서 데이터를 출력합니다. 중단하려면 q 를 입력하세요.')
        while True:
            self.ds.set_env()
            env = self.ds.get_env()
            self.env_values.update(env)

            for key, value in env.items():
                self.accumulated_data[key].append(value)

            print('{')
            for key, value in self.env_values.items():
                print(f"    '{key}': {repr(value)},")
            print('}')

            self.counter += 1
            if self.counter >= 3:
                print('\n[5분 평균값]')
                for key, values in self.accumulated_data.items():
                    avg = round(sum(values) / len(values), 2)
                    print(f"    '{key}': {avg}")
                print()
                self.accumulated_data = {
                    key: [] for key in self.accumulated_data
                }
                self.counter = 0

            user_input = input(
                f'[{self.counter * 5}/300초] 종료하려면 q 입력: '
            )
            if user_input.strip().lower() == 'q':
                print('System stopped….')
                break

            time.sleep(5)

    def get_mission_computer_info(self):
        try:
            system_info = {
                '운영체계': platform.system(),
                '운영체계 버전': platform.version(),
                'CPU 타입': platform.processor(),
                'CPU 코어 수': os.cpu_count(),
                '메모리 크기(GB)': round(
                    psutil.virtual_memory().total / (1024**3), 2
                ),
            }

            try:
                with open('week05/setting.txt', 'r', encoding='utf-8') as f:
                    selected_keys = [line.strip() for line in f.readlines()]
            except FileNotFoundError:
                print('[경고] setting.txt 파일이 없어 모든 항목을 출력합니다.')
                selected_keys = list(system_info.keys())

            print('[시스템 정보]')
            for key in selected_keys:
                if key in system_info:
                    print(f'  {key}: {system_info[key]}')
                else:
                    print(f'  {key}: (알 수 없는 항목)')

            return {
                key: system_info.get(key)
                for key in selected_keys
                if key in system_info
            }

        except Exception as e:
            print('시스템 정보를 가져오는 도중 오류가 발생했습니다:', e)
            return {}

    def get_mission_computer_load(self):
        try:
            load_info = {
                'CPU 실시간 사용량(%)': psutil.cpu_percent(interval=1),
                '메모리 실시간 사용량(%)': psutil.virtual_memory().percent,
            }

            print('[시스템 부하 정보]')
            for key, value in load_info.items():
                print(f'  {key}: {value}')
            return load_info
        except Exception as e:
            print('시스템 부하 정보를 가져오는 도중 오류가 발생했습니다:', e)
            return {}


def main():
    ds = DummySensor()
    RunComputer = MissionComputer()

    RunComputer.get_mission_computer_info()
    RunComputer.get_mission_computer_load()

    # RunComputer.get_sensor_data()


if __name__ == '__main__':
    main()
