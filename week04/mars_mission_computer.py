import random
import time

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
            'mars_base_internal_oxygen': None
        }
        self.ds = DummySensor()
        self.accumulated_data = {
            key: [] for key in self.env_values
        }
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
            if self.counter >= 60:
                print('\n[5분 평균값]')
                for key, values in self.accumulated_data.items():
                    avg = round(sum(values) / len(values), 2)
                    print(f"    '{key}': {avg}")
                print()
                self.accumulated_data = {key: [] for key in self.accumulated_data}
                self.counter = 0

            user_input = input(f'[{self.counter * 5}/300초] 종료하려면 q 입력: ')
            if user_input.strip().lower() == 'q':
                print('System stopped….')
                break

            time.sleep(5)

def main():
    ds = DummySensor()
    print('DummySensor instance created:', ds)
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()
     
if __name__ == '__main__':
    main()