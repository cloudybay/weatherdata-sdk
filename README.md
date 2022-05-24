<p align="center">
  <img src="https://raw.githubusercontent.com/cloudybay/weatherdata-sdk/main/Logo.png">
</p>



## 這是什麼?


**WeatherData** 是收集了氣象局的開放氣象資料以及安吉氣象決策的預報資料。

所有資料都整合在 WeatherData 的後台伺服器中，使用這個套件就不需要再自行開發爬蟲爬取氣象局，只要輸入位置(經緯度或縣市鄉鎮名)，即可取得天氣資料。

## 安裝

```shell

$ pip install WeatherData

```


## 如何開始

```python
>>> import WeatherData as wd
>>> wd.obs.get(citytown='台北市中正區')
# 回傳最新一次觀測時間的資料
{
    'lat': 25.046058,
    'lon': 121.516565,
    'dtime': '2022-03-17T08:00+00:00',
    'ws': 2.7,
    'tx': 26.7,
    'rh': 58.3,
    'pres': 1004.1,
    'wd': 307.3039482779834,
    'precp_hour': 0.0,
    'cloud': 0.28
}

>>> from datetime import datetime
>>> wd.obs.get(lat=21., lon=124., dtime=datetime(2021,12,31))
# 回傳指定觀測時間的資料
{
    'lat': 21.0,
    'lon': 124.0,
    'dtime': '2021-12-31T00:00+00:00',
    'ws': 0.0,
    'tx': 0.0,
    'rh': 0.0,
    'pres': 0.0,
    'wd': 270.0,
    'precp_hour': 0.0,
    'cloud': 0
}

>>> wd.fcst.get(lat=21., lon=124.)
# 回傳最新一次預報的所有資料，總共資料長度 14 天，每小時一筆，共 336 筆資料
[{
    'dtime': '2022-04-13T00:00:00+00:00',
    'wd': 97.5,
    'ws': 6.1,
    'wg': 7.3,
    'precp': -999.0,
    'cloud': 50.9,
    'tx': 25.5,
    'rh': 73.5,
    'pres': 1008.5,
    'lat': 20.0,
    'lon': 120.0
}, {
    'dtime': '2022-04-13T01:00:00+00:00',
    'wd': 99.1,
    'ws': 5.5,
    'wg': 6.5,
    'precp': 0.0,
    'cloud': 47.8,
    'tx': 25.6,
    'rh': 75.0,
    'pres': 1008.4,
    'lat': 20.0,
    'lon': 120.0
}, {
    'dtime': '2022-04-13T02:00:00+00:00',
    'wd': 104.2,
    'ws': 5.1,
    'wg': 6.0,
    'precp': 0.0,
    'cloud': 49.4,
    'tx': 25.6,
    'rh': 74.6,
    'pres': 1008.3,
    'lat': 20.0,
    'lon': 120.0
}...]
```

### 參數說明

#### 輸入參數
- dtime: 資料時間(UTC)
- citytown: 縣市+鄉鎮
- lat: 緯度
- lon: 經度

#### 輸出參數
- dtime: 資料時間(UTC)
- wd: 風向(方位角 0~360度 北向為0)
- ws: 風速(m/s)
- wg: 最大陣風風速(m/s)
- precp: 預報小時雨量(mm)
- precp_hour: 觀測小時雨量(mm)
- cloud: 雲量 0~100
- tx: 溫度(攝氏溫度)
- rh: 相對濕度
- pres: 大氣壓力(hPa)
- lat: 緯度(度)
- lon: 經度(度)

### 錯誤排除


```
requests.exceptions.HTTPError: 503 Server Error: Service Temporarily Unavailable
```

如果出現以上 503 Server Error ， 可以等個 10 秒鐘再試試看。

## 資料來源

- [氣象資料開放平台](https://opendata.cwb.gov.tw/index)
- [安吉氣象決策](https://www.weatherangel.com.tw/company/services2.php)

所有預報資料均來自中央氣象局及安吉氣象決策公司等機構提供，本公司並未進行任何天氣預報。


## License

- [License Detail](./LICENSE)

## 免責聲明

本專案提供的所有內容均用於教育、非商業用途。資料僅供參考，對於資料內容任何錯誤、更新延誤或傳輸中斷，本公司均不負任何責任。
