# -*- coding: utf-8 -*-
import os
from datetime import datetime, timedelta
import pytz

from WeatherData.util import parse_city_town_to_region_code
from WeatherData.region_code import RegionCodeInfo

import urllib3
# 讓local端開發，測試呼叫Func時不會出現InsecureRequestWarning: Unverified HTTPS request is being made
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

WD_API_SERVER_HOST = 'https://weatherdata.tw/'


def get(lat: str = None, lon: str = None, dtime: datetime = None, citytown: str = None):

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
            dtime = dtime.replace(minute=0, second=0, microsecond=0)
        else:
            raise TypeError('argument dtime must be datetime, not string')

    if lat and lon and dtime:
        import requests
        _tau = dtime.hour % 6
        _from = dtime - timedelta(hours=_tau)
        _to = _from + timedelta(hours=6)
        url = f'{WD_API_SERVER_HOST}api/fcst/cwb_wrf/?lat={lat}&lon={lon}&from={_from}&to={_to}'
        res = requests.get(url, headers=get_wd_api_header(), verify=False)
        if res.status_code == 200:
            # WD的CWB Wrf逐六小時報， 找出使用者的時間點最接近的前後時間點預報值回傳 [{}, {}]
            obs_data = res.json().get('data', [])
            return obs_data


def get_wd_api_header():
    token = 'caccfc7087e0441591b531ba944f06b6'
    api_token = f'Token {token}'
    return {'Content-Type': 'application/json', 'Authorization': api_token}
