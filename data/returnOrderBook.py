import requests

url = 'https://poloniex.com/public?command=returnOrderBook&currencyPair=all&depth=10'


exchanges = ['USDT_REP', 'BTC_XVC', 'BTC_PINK', 'BTC_SYS', 'BTC_EMC2', 'BTC_RADS', 'BTC_NOTE', 'BTC_MAID', 'BTC_GNT', 'BTC_BCN', 'BTC_REP', 'BTC_BCY', 'BTC_GNO', 'XMR_NXT', 'USDT_ZEC', 'BTC_FCT', 'USDT_ETH', 'USDT_BTC', 'BTC_LBC', 'BTC_DCR', 'USDT_ETC', 'BTC_AMP', 'BTC_XPM', 'BTC_NXT', 'BTC_VTC', 'ETH_STEEM', 'XMR_BLK', 'BTC_PASC', 'XMR_ZEC', 'BTC_GRC', 'BTC_NXC', 'BTC_BTCD', 'BTC_LTC', 'BTC_DASH', 'BTC_NAUT', 'ETH_ZEC', 'BTC_ZEC', 'BTC_BURST', 'BTC_BELA', 'BTC_STEEM', 'BTC_ETC', 'BTC_ETH', 'BTC_HUC', 'BTC_STRAT', 'BTC_LSK', 'BTC_FLO', 'BTC_CLAM', 'ETH_REP', 'XMR_DASH', 'USDT_DASH', 'BTC_BLK', 'BTC_XRP', 'USDT_NXT', 'BTC_NEOS', 'BTC_BTS', 'BTC_DOGE', 'ETH_GNT', 'BTC_SBD', 'ETH_GNO', 'BTC_XCP', 'USDT_LTC', 'BTC_BTM', 'USDT_XMR', 'ETH_LSK', 'BTC_OMNI', 'BTC_NAV', 'BTC_FLDC', 'BTC_XBC', 'BTC_DGB', 'BTC_SC', 'XMR_BTCD', 'BTC_VRC', 'BTC_RIC', 'XMR_MAID', 'BTC_STR', 'BTC_POT', 'BTC_XMR', 'BTC_SJCX', 'BTC_VIA', 'BTC_XEM', 'BTC_NMC', 'ETH_ETC', 'XMR_LTC', 'BTC_ARDR', 'BTC_EXP', 'USDT_XRP', 'BTC_GAME', 'BTC_PPC', 'XMR_BCN', 'USDT_STR']
features = ['bids', 'asks']

response = requests.get(url)
data = response.json()
result = []

try:
    for exchange in exchanges:
        try:
            for feature in features:
                for li in data[exchange][feature]:
                    for numb in li:
                        result.append(float(numb))
            try:
                result.append(float(data[exchange]['isFrozen']))
            except:
                result.append((float('nan')))
            try:
                result.append(float(data[exchange]['seq']))
            except:
                result.append((float('nan')))
        except():
            result.append(20 * [float('nan')])
except():
    result.append(40 * [float('nan')])

print(result)
