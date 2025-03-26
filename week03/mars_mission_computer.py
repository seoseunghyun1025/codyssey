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
        return self.env_values


if __name__ == '__main__':
    ds = DummySensor('TestSensor')
    ds.set_env()
    env_data = ds.get_env()
    print(env_data)
