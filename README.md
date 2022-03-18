<p align="center">
  <img src="./Logo.png?raw=true">
</p>

---

## 這是什麼?


**WeatherData** 是收集了氣象局、農委會的開源氣象觀測資料以及安吉氣象決策的預報資料。

所有資料都整合在 WeatherData 的後台伺服器中，使用這個套件就不需要再自行開發爬蟲爬取氣象局，隨便輸入一個經緯度或者縣市鄉鎮以及所需要的時間就可以取得天氣資料。


## Quickstart

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
```

## 資料來源

- [氣象資料開放平台](https://opendata.cwb.gov.tw/index)
- [農業氣象觀測網監測系統](https://agr.cwb.gov.tw/)
- [安吉氣象決策](https://www.weatherangel.com.tw/company/services2.php)

所有預報資料均來自中央氣象局及安吉氣象決策公司等機構提供，本公司並未進行任何天氣預報。


## License

- [License Detail](./LICENSE)

- 本專案提供的所有內容均用於教育、非商業用途。資料僅供參考，對於資料內容任何錯誤、更新延誤或傳輸中斷，本公司均不負任何責任。
