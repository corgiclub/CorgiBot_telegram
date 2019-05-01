# -*- coding: utf-8 -*
import requests
import json


def get_weather(city: str) -> json:
    req = requests.get("https://free-api.heweather.net/s6/weather?location="
                       "{}&key=89d6bbc3861844d59a6313c16448d293".format(city))
    json_data = json.loads(req.text, encoding="UTF8")
    return json_data


def get_info(city: str):
    try:
        resp = get_weather(city)
        resp_basic = resp['HeWeather6'][0]['basic']
        resp_update = resp['HeWeather6'][0]['update']
        resp_now = resp['HeWeather6'][0]['now']
        # resp_hourly = resp['HeWeather6'][0]['hourly']
        resp_daily_forecast = resp['HeWeather6'][0]['daily_forecast']
        resp_today = resp_daily_forecast[0]
        resp_tomorrow = resp_daily_forecast[1]

        status = resp['HeWeather6'][0]['status']

        str_weather = ""
        str_weather += "当前城市:{area}-{city}-{loc}\n".format(
            area=resp_basic['admin_area'], city=resp_basic['parent_city'], loc=resp_basic['location'])
        str_weather += "当前时间:{}\n".format(resp_update['loc'])
        str_weather += "当前天气:{},温度:{}℃,体感温度:{}℃\n".format(resp_now['cond_txt'], resp_now['tmp'], resp_now['fl'])
        str_weather += \
            "今日天气:{d},温度:{min}~{max}℃ 风力:{sc}级 相对湿度:{hum}% 降水概率:{pop}% 紫外线强度:{uv}\n". \
            format(d=resp_today['cond_txt_d'], min=resp_today['tmp_min'], max=resp_today['tmp_max'],
                   sc=resp_today['wind_sc'], hum=resp_today['hum'],
                   pop=resp_today['pop'], uv=resp_today['uv_index'])
        str_weather += "明日天气:{d},温度:{min}~{max}℃ 风力:{sc}级 相对湿度:{hum}% 降水概率:{pop}% 紫外线强度:{uv}\n". \
            format(d=resp_tomorrow['cond_txt_d'], min=resp_tomorrow['tmp_min'], max=resp_tomorrow['tmp_max'],
                   sc=resp_tomorrow['wind_sc'], hum=resp_tomorrow['hum'],
                   pop=resp_tomorrow['pop'], uv=resp_tomorrow['uv_index'])
        str_weather += "NM$L天气预报播报完毕"
    except Exception as e:
        print(f"Exception: {e}")
        status = -1
        str_weather = None
    return status, str_weather
