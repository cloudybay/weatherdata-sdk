# -*- coding: utf-8 -*-
import os
from datetime import datetime

from WeatherData.util import parse
from WeatherData.region_code import RegionCodeInfo

# WD_API_SERVER_HOST = 'https://weatherdata.tw/'
WD_API_SERVER_HOST = 'http://gpu.cb:7705/'


def get(lat=None, lon=None, dtime=None, citytown=None, token=None):
    token = 'd37b1f609a094691bce1c197fc46f224'

    if lat == None and lon == None:
        if citytown:
            try:
                region_code = parse(citytown)
                lat, lon = RegionCodeInfo[region_code][1], RegionCodeInfo[region_code][0]
            except KeyError:
                return f'{citytown} 未找到符合的區域, 請重新嘗試'
        else:
            return '請輸入經緯度或縣市鄉鎮'

        # ex.25.068025 121.507228

    if dtime is not None:
        # parse dtime
        pass
    else:
        dtime = datetime.utcnow()

    if lat and lon and dtime and token:
        import requests
        # http://gpu.cb:7705/api/obs/cb_grid/?lat=25.068025&lon=121.507228&from=2022-03-02T15:00&to=2022-03-02T15:00&
        url = f'{WD_API_SERVER_HOST}api/obs/cb_grid/?lat={lat}&lon={lon}&from=2022-03-02T15:00&to=2022-03-02T15:00'
        res = requests.get(url, headers=get_wd_api_header(token), verify=False)
        if res.status_code == 200:
            obs_data = res.json().get('data', [])[0]
            print(obs_data)
        # else:
        #     log.diag(f'WD Server Error. Status Code {res.status_code}.')
        #     return []
    else:
        pass


def get_wd_api_header(token):
    api_token = f'Token {token}'
    return {'Content-Type': 'application/json', 'Authorization': api_token}

