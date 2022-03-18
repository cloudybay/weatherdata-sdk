import os
from datetime import datetime
import pytz

from WeatherData.util import parse_city_town_to_region_code
from WeatherData.region_code import RegionCodeInfo

import urllib3
# 讓local端開發，測試呼叫Func時不會出現InsecureRequestWarning: Unverified HTTPS request is being made
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

WD_API_SERVER_HOST = 'https://weatherdata.tw/'


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
        dtime = dtime.replace(tzinfo=pytz.UTC)
    else:
        if dtime is None:
            dtime = datetime.utcnow()
            dtime = dtime.replace(tzinfo=pytz.UTC)
            dtime = dtime.replace(minute=0, second=0, microsecond=0).isoformat()
        else:
            raise TypeError('argument dtime must be datetime, not string')

    if lat and lon and dtime:
        import requests
        # http://gpu.cb:7705/api/obs/cb_grid/?lat=25.068025&lon=121.507228&from=2022-03-02T15:00&to=2022-03-02T15:00&
        url = f'{WD_API_SERVER_HOST}api/obs/cb_grid/?lat={lat}&lon={lon}&from={dtime}&to={dtime}'
        res = requests.get(url, headers=get_wd_api_header(), verify=False)
        if res.status_code == 200:
            # WD回傳是一個list 目前都只要單點時間，所以只會有一筆資料
            obs_data = res.json().get('data', None)
            if obs_data:
                return obs_data[0]
            else:
                return obs_data


def get_wd_api_header():
    token = 'caccfc7087e0441591b531ba944f06b6'
    api_token = f'Token {token}'
    return {'Content-Type': 'application/json', 'Authorization': api_token}
