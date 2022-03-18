
conda create --name wd python=3.6
```python
>>> import WeatherData as wd
>>> wd.obs.get(citytown='台北市中正區')
{'lat': 25.046058, 'lon': 121.516565, 'dtime': '2022-03-17T08:00+00:00', 'ws': 2.7, 'tx': 26.7, 'rh': 58.3, 'pres': 1004.1, 'wd': 307.3039482779834, 'precp_hour': 0.0, 'cloud': 0.28}
```