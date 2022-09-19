import requests
import json


def get_data():

    cookies = {
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_AB_PDP_CHAR': '0',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLP': 'true',
        'MVID_GUEST_ID': '21470185705',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_HANDOVER': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'flacktory': 'no',
        'searchType2': '3',
        '_gid': 'GA1.2.1468748700.1663418650',
        '_ym_uid': '1640028942755419221',
        '_ym_d': '1663418650',
        '_ym_isad': '2',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '3c9ca1313469deb6c6a7d03c0f5170de',
        'tmr_lvidTS': '1650196534705',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'ea68e12c-205e-41b5-9af5-2b393403fdbe',
        'advcake_track_id': '78689945-3c1d-a30b-05e4-4bbef43e7313',
        'advcake_session_id': '0660bf1d-a78f-2deb-b964-79aa4bc87a81',
        'flocktory-uuid': 'fd0546d7-5af0-4f5e-9190-2c83644971fa-1',
        'afUserId': '48af9f05-383f-4915-97c6-deab956bc836-p',
        'AF_SYNC': '1663418653885',
        '__lhash_': '1a3d91d06eab6a0389182f59f8bd2aa3',
        '__ttl__widget__ui': '1663419260645-040218726071',
        '_sp_id.d61c': 'd94663d8-0519-4e59-9b2e-e413a6e30c35.1663418650.1.1663419337..8040affd-0f1f-462a-9d74-c96a134484ce..7ee51b32-ab9b-4b18-898e-e95e92461554.1663418649708.4',
        '_ga': 'GA1.2.340667555.1663418650',
        'tmr_detect': '0%7C1663419342686',
        'tmr_reqNum': '91',
        '__hash_': '8ccf93cb3f5473a56391b46edec8863c',
        'JSESSIONID': 'KmZwjlMbvygyNj8D77Xr9tQTm7hsqPyFnWXNYlH2vvhLd8xyPxl4!-393459413',
        'bIPs': '-1178626581',
        'MVID_ENVCLOUD': 'prod1',
        '_ga_CFMZTSS5FM': 'GS1.1.1663421692.2.0.1663421692.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1663421692.2.0.1663421692.60.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=3d15e27cb89442da8f0459aa40e57a22,sentry-sample_rate=0%2C5',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_AB_PDP_CHAR=0; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GLP=true; MVID_GUEST_ID=21470185705; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_HANDOVER=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; searchType2=3; _gid=GA1.2.1468748700.1663418650; _ym_uid=1640028942755419221; _ym_d=1663418650; _ym_isad=2; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; tmr_lvid=3c9ca1313469deb6c6a7d03c0f5170de; tmr_lvidTS=1650196534705; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=ea68e12c-205e-41b5-9af5-2b393403fdbe; advcake_track_id=78689945-3c1d-a30b-05e4-4bbef43e7313; advcake_session_id=0660bf1d-a78f-2deb-b964-79aa4bc87a81; flocktory-uuid=fd0546d7-5af0-4f5e-9190-2c83644971fa-1; afUserId=48af9f05-383f-4915-97c6-deab956bc836-p; AF_SYNC=1663418653885; __lhash_=1a3d91d06eab6a0389182f59f8bd2aa3; __ttl__widget__ui=1663419260645-040218726071; _sp_id.d61c=d94663d8-0519-4e59-9b2e-e413a6e30c35.1663418650.1.1663419337..8040affd-0f1f-462a-9d74-c96a134484ce..7ee51b32-ab9b-4b18-898e-e95e92461554.1663418649708.4; _ga=GA1.2.340667555.1663418650; tmr_detect=0%7C1663419342686; tmr_reqNum=91; __hash_=8ccf93cb3f5473a56391b46edec8863c; JSESSIONID=KmZwjlMbvygyNj8D77Xr9tQTm7hsqPyFnWXNYlH2vvhLd8xyPxl4!-393459413; bIPs=-1178626581; MVID_ENVCLOUD=prod1; _ga_CFMZTSS5FM=GS1.1.1663421692.2.0.1663421692.0.0.0; _ga_BNX5WPP3YK=GS1.1.1663421692.2.0.1663421692.60.0.0',
        'pragma': 'no-cache',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '3d15e27cb89442da8f0459aa40e57a22-859ba17ddc4c81aa-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-set-application-id': 'a795dd4e-e8e2-4ea9-bce7-66e3daef3227',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    product_ids = response.get("body").get("products")

    with open("1_product_ids.json", "w") as file:
        json.dump(product_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': product_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

    with open("2_items.json", "w") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    product_ids_str = ",".join(product_ids)

    
    params = {
        'productIds': product_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    with open("3_prices.json", "w") as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    item_prices = {}

    material_prices = response.get("body").get("materialPrices")

    for item in material_prices: 
        item_id = item.get("price").get("productId")
        item_base_price = item.get("price").get("basePrice")
        item_sale_price = item.get("price").get("salePrice")
        item_bonus = item.get("bonusRubles").get("total")

        item_prices[item_id] = {
            "item_basePrice" : item_base_price,
            "item_salePrice" : item_sale_price,
            "item_bonus" : item_bonus,
        }
    
    with open("4_item_prices.json", "w") as file:
        json.dump(item_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open("2_items.json") as file: 
        products_data = json.load(file)
    
    with open("4_item_prices.json") as file: 
        products_prices = json.load(file)

    products_data = products_data.get("body").get("products")

    for item in products_data:
        product_id = item.get("productId")

        if product_id in products_prices:
            prices = products_prices[product_id]

        item["item_basePrice"] = prices.get("item_basePrice")
        item["item_salePrice"] = prices.get("item_salePrice")
        item["item_bonus"] = prices.get("item_bonus")

    with open("5_result.json", "w") as file: 
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == "__main__":
    main()
