import requests
import pandas as pd
from timeout import timeout

url = 'https://poloniex.com/public?command=returnOrderBook&currencyPair=all&depth=10'

exchanges = ['USDT_REP', 'BTC_XVC', 'BTC_PINK', 'BTC_SYS', 'BTC_EMC2', 'BTC_RADS', 'BTC_NOTE', 'BTC_MAID', 'BTC_GNT',
             'BTC_BCN', 'BTC_REP', 'BTC_BCY', 'BTC_GNO', 'XMR_NXT', 'USDT_ZEC', 'BTC_FCT', 'USDT_ETH', 'USDT_BTC',
             'BTC_LBC', 'BTC_DCR', 'USDT_ETC', 'BTC_AMP', 'BTC_XPM', 'BTC_NXT', 'BTC_VTC', 'ETH_STEEM', 'XMR_BLK',
             'BTC_PASC', 'XMR_ZEC', 'BTC_GRC', 'BTC_NXC', 'BTC_BTCD', 'BTC_LTC', 'BTC_DASH', 'BTC_NAUT', 'ETH_ZEC',
             'BTC_ZEC', 'BTC_BURST', 'BTC_BELA', 'BTC_STEEM', 'BTC_ETC', 'BTC_ETH', 'BTC_HUC', 'BTC_STRAT', 'BTC_LSK',
             'BTC_FLO', 'BTC_CLAM', 'ETH_REP', 'XMR_DASH', 'USDT_DASH', 'BTC_BLK', 'BTC_XRP', 'USDT_NXT', 'BTC_NEOS',
             'BTC_BTS', 'BTC_DOGE', 'ETH_GNT', 'BTC_SBD', 'ETH_GNO', 'BTC_XCP', 'USDT_LTC', 'BTC_BTM', 'USDT_XMR',
             'ETH_LSK', 'BTC_OMNI', 'BTC_NAV', 'BTC_FLDC', 'BTC_XBC', 'BTC_DGB', 'BTC_SC', 'XMR_BTCD', 'BTC_VRC',
             'BTC_RIC', 'XMR_MAID', 'BTC_STR', 'BTC_POT', 'BTC_XMR', 'BTC_SJCX', 'BTC_VIA', 'BTC_XEM', 'BTC_NMC',
             'ETH_ETC', 'XMR_LTC', 'BTC_ARDR', 'BTC_EXP', 'USDT_XRP', 'BTC_GAME', 'BTC_PPC', 'XMR_BCN', 'USDT_STR']
features = ['bids', 'asks']

@timeout(50)
def returnResult():
    result = []
    try:
        response = requests.get(url)
        data = response.json()
    except:
        for i in range(0, 3780):
            result.append(float('nan'))
        print("returnOrderBook failed, appending nan: " + str(len(result)))
        return result
    for exchange in exchanges:
        for feature in features:
            try:
                for li in data[exchange][feature]:
                    for numb in li:
                        try:
                            result.append(pd.to_numeric(numb, 'coerce'))
                        except:
                            result.append(float('nan'))
            except:
                for i in range(0, 20):  # 2 * depth = 20
                    result.append(float('nan'))
        try:
            result.append(pd.to_numeric(data[exchange]['isFrozen'], 'coerce'))
        except:
            result.append(float('nan'))
        try:
            result.append(pd.to_numeric(data[exchange]['seq'], 'coerce'))
        except:
            result.append(float('nan'))

    print("returnOrderBook: " + str(len(result)))
    return result
