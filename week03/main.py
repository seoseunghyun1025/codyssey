class DummySensor:

    def __init__(self, name="DefaultSensor"):
        self.name = name
        print(f"{self.name}가 생성되었습니다.")

        self.env_values = {
            "mars_base_internal_temperature": None,
            "mars_base_external_temperature": None,
            "mars_base_internal_humidity": None,
            "mars_base_external_illuminance": None,
            "mars_base_internal_co2": None,
            "mars_base_internal_oxygen": None,
        }
