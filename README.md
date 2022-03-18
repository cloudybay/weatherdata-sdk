<p align="center">
  <img src="./Logo.png?raw=true">
</p>

---

## 這是什麼?


**WeatherData** 是收集了氣象局的開放氣象資料以及安吉氣象決策的預報資料。

所有資料都整合在 WeatherData 的後台伺服器中，使用這個套件就不需要再自行開發爬蟲爬取氣象局，只要輸入位置(經緯度或縣市鄉鎮名)，即可取得天氣資料。

## Installation

```shell

$ pip install WeatherData

```


## Get start

```python
>>> import WeatherData as wd
>>> wd.obs.get(citytown='台北市中正區')
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

>>> wd.fcst.get(lat=21., lon=124., dtime=datetime(2022,3, 20, 0, 0))
{
    'dtime': '2022-03-20T00:00:00+00:00',
    'wd': 75.9,
    'ws': 8.9,
    'wg': 10.8,
    'precp': 0.0,
    'cloud': 95.2,
    'tx': 24.0,
    'rh': 85.6,
    'pres': 1014.3,
    'lat': 21.0,
    'lon': 124.0
}
```

### 參數說明

- dtime: 資料時間(UTC)
- wd: 風向(方位角 0~360度 北向為0)
- ws: 風速(m/s)
- wg: 最大陣風風速(m/s)
- prcep: 預報小時雨量(mm)
- prcep_hour: 觀測小時雨量(mm)
- cloud: 雲量 0~1
- tx: 溫度(攝氏溫度)
- rh: 相對濕度
- pres: 大氣壓力(hPa)
- lat: 緯度(度)
- lon: 經度(度)

## 資料來源

- [氣象資料開放平台](https://opendata.cwb.gov.tw/index)
- [安吉氣象決策](https://www.weatherangel.com.tw/company/services2.php)

所有預報資料均來自中央氣象局及安吉氣象決策公司等機構提供，本公司並未進行任何天氣預報。


## License

- [License Detail](./LICENSE)

## 免責聲明

本專案提供的所有內容均用於教育、非商業用途。資料僅供參考，對於資料內容任何錯誤、更新延誤或傳輸中斷，本公司均不負任何責任。
