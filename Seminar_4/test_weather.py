import unittest
from unittest.mock import patch
from weather import WeatherReporter


class TestWeather(unittest.TestCase):

    def setUp(self) -> None:
        with patch('weather.WeatherService') as mock_weather_service:
            self.weather_report = WeatherReporter(mock_weather_service)

    def test_weather(self):
        self.weather_report.generate_report()
        self.weather_report.weather_service.get_current_temperature.assert_called()
