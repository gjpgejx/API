import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

latit = input()
longit = input()

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latit,
    "longitude": longit,
    "hourly": "temperature_2m",
    "timezone": "Europe/Moscow"
}
responses = openmeteo.weather_api(url, params=params)

response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
    start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
    end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
    freq=pd.Timedelta(seconds=hourly.Interval()),
    inclusive="left"
)}
hourly_data["temperature_2m"] = hourly_temperature_2m

hourly_dataframe = pd.DataFrame(data=hourly_data)
print(hourly_dataframe)

# Создание requirements.txt
with open('requirements.txt', 'w') as file:
    file.write('openmeteo_requests\n')
    file.write('requests_cache\n')
    file.write('pandas\n')
    file.write('retry_requests\n')

# Создание .gitignore
with open('.gitignore', 'w') as file:
    file.write('.cache\n')
    file.write('.vscode\n')
    file.write('__pycache__\n')
    file.write('*.pyc\n')
    file.write('*.log\n')
