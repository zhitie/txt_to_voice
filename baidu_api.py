# coding=utf-8
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '**************'
API_KEY = '*******************'
SECRET_KEY = '*********************'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result  = client.synthesis('舍利子，是诸法空相，不生不灭，不垢不净，不增不减。是故空中无色，无受想行识，无眼耳鼻舌身意，无色声香味触法，无眼界乃至无意识界，无无明亦无无明尽，乃至无老死，亦无老死尽，无苦集灭道，无智亦无得，以无所得故，菩提萨埵。', 'zh', 1, {
    'vol': 5,})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)