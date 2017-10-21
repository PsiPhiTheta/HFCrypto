import requests
import pandas as pd

url = "https://poloniex.com/public?command=returnTicker"
features = ['last', 'quoteVolume', 'high24hr', 'isFrozen', 'highestBid', 'percentChange', 'low24hr', 'lowestAsk', 'id', 'baseVolume']

exchanges = ['USDT_REP', 'BTC_XVC', 'BTC_PINK', 'BTC_SYS', 'BTC_EMC2', 'BTC_RADS', 'BTC_SC', 'BTC_MAID', 'BTC_GNT', 'BTC_BCN', 'BTC_REP', 'BTC_BCY', 'BTC_GNO', 'XMR_NXT', 'USDT_ZEC', 'BTC_FCT', 'USDT_ETH', 'USDT_BTC', 'BTC_LBC', 'BTC_DCR', 'USDT_ETC', 'BTC_AMP', 'BTC_XPM', 'BTC_NXT', 'BTC_VTC', 'ETH_STEEM', 'XMR_BLK', 'BTC_PASC', 'XMR_ZEC', 'BTC_GRC', 'BTC_NXC', 'BTC_BTCD', 'BTC_LTC', 'BTC_DASH', 'BTC_NAUT', 'ETH_ZEC', 'BTC_ZEC', 'BTC_BURST', 'BTC_BELA', 'BTC_STEEM', 'BTC_ETC', 'BTC_ETH', 'BTC_HUC', 'BTC_STRAT', 'BTC_LSK', 'BTC_EXP', 'BTC_CLAM', 'ETH_REP', 'XMR_DASH', 'USDT_DASH', 'BTC_BLK', 'BTC_XRP', 'USDT_NXT', 'BTC_NEOS', 'BTC_BTS', 'BTC_DOGE', 'ETH_GNT', 'BTC_SBD', 'ETH_GNO', 'BTC_XCP', 'USDT_LTC', 'BTC_BTM', 'USDT_XMR', 'ETH_LSK', 'BTC_OMNI', 'BTC_NAV', 'BTC_FLDC', 'BTC_XBC', 'BTC_DGB', 'BTC_NOTE', 'XMR_BTCD', 'BTC_VRC', 'BTC_RIC', 'XMR_MAID', 'BTC_STR', 'BTC_POT', 'BTC_XMR', 'BTC_SJCX', 'BTC_VIA', 'BTC_XEM', 'BTC_NMC', 'ETH_ETC', 'XMR_LTC', 'BTC_ARDR', 'BTC_FLO', 'USDT_XRP', 'BTC_GAME', 'BTC_PPC', 'XMR_BCN', 'USDT_STR']

def returnResult():
    result = []
    try:
        response = requests.get(url)
        data = response.json()
    except:
        for i in range(0, 900):
            result.append(float('nan'))
        print("returnTicker failed, appending nan: " + str(len(result)))
        return result
    for exchange in exchanges:
        for feature in features:
            try:
                result.append(pd.to_numeric(data[exchange][feature], 'coerce'))
            except KeyboardInterrupt:
                quit()
            except:
                result.append(float('nan'))

    print("returnTicker: " + str(len(result)))
    return result
