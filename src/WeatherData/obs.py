from datetime import datetime, timedelta

import pytz
import requests

from WeatherData.util import parse_city_town_to_region_code
from WeatherData.region_code import RegionCodeInfo

import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


WD_API_SERVER_HOST = 'http://api.weatherdata.tw/'


def get(lat: float = None, lon: float = None, dtime: datetime = None, citytown: str = None):

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

    if isinstance(dtime, datetime):
        dtime = dtime.replace(tzinfo=pytz.UTC).isoformat()
    else:
        # WD 尚有缺陷，只好用往前3小時時間範圍的方式抓到最新觀測
        if dtime is None:
            dtime = datetime.utcnow() + timedelta(hours=-3)
            dtime = dtime.replace(tzinfo=pytz.UTC)
            dtime = dtime.replace(minute=0, second=0, microsecond=0)
            dt_from = dtime.isoformat()
            dt_to = (dtime + timedelta(hours=3)).isoformat()
        else:
            raise TypeError('argument dtime must be datetime, not string')

    if lat and lon and dtime:
        url = f'{WD_API_SERVER_HOST}api/obs/cb_grid/'
        res = requests.get(url, headers=get_wd_api_header(), verify=False, params={
            'lat': lat,
            'lon': lon,
            'from': dtime,
            'to': dtime
        })
        res.raise_for_status()
        # WD回傳是一個list 目前都只要單點時間，所以只會有一筆資料
        obs_data = res.json().get('data', None)
        if obs_data:
            return obs_data[-1]
        else:
            return obs_data


def get_wd_api_header():
    token = 'caccfc7087e0441591b531ba944f06b6'
    api_token = f'Token {token}'
    return {'Content-Type': 'application/json', 'Authorization': api_token}
