import random


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
        log_line = (
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


def main():
    ds = DummySensor('TestSensor')
    ds.set_env()
    env_data = ds.get_env()
    print(env_data)


if __name__ == '__main__':
    main()
