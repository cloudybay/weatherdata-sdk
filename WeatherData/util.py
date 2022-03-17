import re


def parse_city_town_to_region_code(city_town):
    city_county_text = ['縣', '市']
    town_text = ['鄉', '市', '鎮', '區']
    city_text = ['台北', '新北', '桃園', '台中', '台南', '高雄', '基隆']
    county_text = ['新竹', '苗栗', '彰化', '南投', '雲林', '嘉義', '屏東', '宜蘭', '花蓮', '台東', '澎湖', '金門', '連江']

    # 先統一 台
    city_town = city_town.replace('臺', '台')

    # 台北縣特殊處理
    city_town = city_town.replace('台北縣', '新北市')

    # 換掉空格跟一些特殊符號
    city_town = re .sub(r'[, |.]+', '', city_town)

    if len(city_town) < 3:
        raise ValueError(f'At least three charactor required. {city_town}')

    region_code = ''
    if city_town[:2] in ['新竹', '嘉義']:
        # 無法處理只有`新竹` or `嘉義`的情況
        msg = f'Cannot determin 縣 or 市 with {city_town}'
        try:
            if city_town[2] not in city_county_text:
                raise ValueError(msg)
        except IndexError:
            raise ValueError(msg)
        region_code = city_town[:3]
    elif city_town[:2] in county_text + city_text:
        # 除新竹嘉義外 只有七個市 直接判斷是不是這七個
        region_code = city_town[:2] + ('市' if city_town[:2] in city_text else '縣')
    else:
        raise ValueError(f'{city_town} is not a regular city town')

    try:
        # 決定鄉鎮地名要從哪裡開始擷取
        if city_town[2] not in city_county_text:
            sub_str_idx = 2
        else:
            sub_str_idx = 3
    except IndexError:
        return region_code

    # 先換成 list 才能替換
    town_txt = list(city_town[sub_str_idx:])

    # 台南的 新市 太特別了直接略過不做處理
    if city_town[sub_str_idx:] != '新市' and town_txt and town_txt[-1] in town_text:
        # 如果最後一個字元是 ['鄉', '市', '鎮', '區'] 任一個 換成空字串
        town_txt[-1] = ''
        region_code += ''.join(town_txt)
    else:
        region_code += city_town[sub_str_idx:]

    return region_code
