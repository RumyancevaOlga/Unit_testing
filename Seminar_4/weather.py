from random import randint


class WeatherService:

    def get_current_temperature(self) -> int:
        return randint(0, 30)


class WeatherReporter:

    def __init__(self, weather_service: WeatherService):
        self._weather_service = weather_service

    @property
    def weather_service(self):
        return self._weather_service

    def generate_report(self):
        self._weather_service.get_current_temperature()
