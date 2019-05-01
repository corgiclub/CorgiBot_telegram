import xml.etree.cElementTree as ET
import requests
citylist = requests.get('http://mobile.weather.com.cn/js/citylist.xml')
cityTree = ET.ElementTree(citylist)
root = cityTree.getroot()
for element in root:
    print(element)