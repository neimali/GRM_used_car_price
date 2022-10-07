from bs4 import BeautifulSoup
from urllib.request import urlopen
import datetime
import re
import time

import pandas as pd


def get_page_num(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    try:
        page_info = bs.find(class_="resultsShowingCount-1707762110").text
        page_num = page_info.split()[-2].replace(',', '')
        page_num = int(int(page_num) / 20)
    except:
        page_num = 1
        pass

    return page_num


def get_item_info(url):
    time.sleep(1.5)
    item_info_list = []

    html = urlopen(url)
    bs_item = BeautifulSoup(html, 'html.parser')

    try:
        item_brand = bs_item.find(itemprop='brand').text
    except:
        item_brand = 'na'

    try:
        item_model = bs_item.find(itemprop='model').text
    except:
        item_model = 'na'

    try:
        item_date = bs_item.find(itemprop='vehicleModelDate').text
    except:
        item_date = 'na'

    try:
        item_price = bs_item.find('span', itemprop='price').text
    except:
        item_price = 'na'

    try:
        item_color = bs_item.find(itemprop='color').text
    except:
        item_color = 'na'

    try:
        item_config = bs_item.find(itemprop='vehicleConfiguration').text
    except:
        item_config = 'na'

    try:
        item_condition = bs_item.find(itemprop='itemCondition').text
    except:
        item_condition = 'na'

    try:
        item_bodytype = bs_item.find(itemprop='bodyType').text
    except:
        item_bodytype = 'na'

    try:
        item_wheelConfig = bs_item.find(itemprop='driveWheelConfiguration').text
    except:
        item_wheelConfig = 'na'

    try:
        item_transmission = bs_item.find(itemprop='vehicleTransmission').text
    except:
        item_transmission = 'na'

    try:
        item_fueltype = bs_item.find(itemprop='fuelType').text
    except:
        item_fueltype = 'na'

    try:
        item_mileage = bs_item.find(itemprop='mileageFromOdometer').text
    except:
        item_mileage = 'na'

    item_carfax = bs_item.find('a', href=re.compile('^(https://reports.carproof.com)((?!:).)*$'))
    try:
        item_carfax_link = item_carfax.attrs['href']
    except:
        item_carfax = bs_item.find('a', href=re.compile('^(https://www.carproof.com)((?!:).)*$'))
        try:
            item_carfax_link = item_carfax.attrs['href']
        except:
            item_carfax_link = 'na'

    try:
        item_dealer_add = bs_item.find(itemprop='address').text
    except:
        item_dealer_add = 'na'

    item_info_list.append(item_brand)
    item_info_list.append(item_model)
    item_info_list.append(item_date)
    item_info_list.append(item_price)
    item_info_list.append(item_color)
    item_info_list.append(item_config)
    item_info_list.append(item_condition)
    item_info_list.append(item_bodytype)
    item_info_list.append(item_wheelConfig)
    item_info_list.append(item_transmission)
    item_info_list.append(item_fueltype)
    item_info_list.append(item_mileage)
    item_info_list.append(item_carfax_link)
    item_info_list.append(item_dealer_add)

    return item_info_list

if __name__ == '__main__':


    link='https://www.kijiji.ca/b-autos-camions/grand-montreal/cars/used/k0c174l80002a49'
    nums=get_page_num(link)
    print(nums)
