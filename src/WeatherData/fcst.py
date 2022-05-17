import requests

from WeatherData.util import parse_city_town_to_region_code
from WeatherData.region_code import RegionCodeInfo

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


WD_API_SERVER_HOST = 'http://api.weatherdata.tw/'


def get(lat: float = None, lon: float = None, citytown: str = None):

    if lat:
        if isinstance(lat, float):
            lat = str(lat)
        else:
            raise TypeError(f'illegal argument type for {lat}, argument must be a float latitude')

    if lon:
        if isinstance(lon, float):
            lon = str(lon)
        else:
            raise TypeError(f'illegal argument type for {lon}, argument must be a float longitude')

    if lat is None and lon is None:
        if citytown:
            region_code = parse_city_town_to_region_code(citytown)
            lat, lon = RegionCodeInfo[region_code][0], RegionCodeInfo[region_code][1]
            # ex.lat, lon = 25.068025, 121.507228
        else:
            raise KeyError()

    if lat and lon:
        url = f'{WD_API_SERVER_HOST}api/fcst/angel_wrf/'
        res = requests.get(url, headers=get_wd_api_header(), verify=False, params={
            'lat': lat,
            'lon': lon
        })
        res.raise_for_status()
        # WD的CWB Wrf逐六小時報， 找出使用者的時間點最接近的前後時間點預報值回傳 [{}, {}]
        fcst_data = res.json().get('data', None)
        if fcst_data:
            return fcst_data
        else:
            return []


def get_wd_api_header():
    token = 'caccfc7087e0441591b531ba944f06b6'
    api_token = f'Token {token}'
    return {'Content-Type': 'application/json', 'Authorization': api_token}
