import requests
import pandas as pd

url = 'https://poloniex.com/public?command=returnCurrencies'

currencies = ['OPAL', 'MYR', 'BBR', 'LTBC', 'LBC', 'NOXT', 'DRKC', 'SUN', 'BITUSD', 'MRC', 'DCR', 'GLB', 'WIKI', 'CHA', 'NXTI', 'FRAC', 'XPM', 'NTX', 'BTCS', 'IXC', 'URO', 'TAC', 'GPC', 'DASH', 'XAI', 'FVZ', 'NXC', 'YIN', 'QBK', 'GRCX', 'BTCD', 'CINNI', 'YACC', 'VIA', 'BURST', 'GIAR', 'XAP', 'SYS', 'MAID', 'APH', 'GML', 'MAX', 'BONES', 'NAV', 'PASC', 'HZ', 'INDEX', 'Q2C', 'XSV', 'GUE', 'USDE', 'BELA', 'BURN', 'FLT', 'SSD', 'FLO', 'IFC', 'METH', 'XSI', 'PTS', 'BLOCK', 'GRS', 'SILK', 'SHIBE', 'JUG', 'HUC', 'QCN', 'XDN', 'LSK', 'WOLF', 'SPA', 'MTS', 'AMP', 'REP', 'UVC', 'GEO', 'ZEC', 'FIBRE', 'BDG', 'ENC', 'LOVE', 'FLAP', 'BDC', 'BLU', 'MZC', 'FOX', 'FRK', 'SJCX', 'EFL', 'GRC', 'DSH', 'BNS', 'FCT', 'XEM', 'XRP', 'UTC', 'ULTC', 'USDT', 'MMXIV', 'LEAF', 'LTCX', 'BTS', 'VOOT', 'XCH', 'DOGE', 'XCN', 'XCR', 'XCP', 'RADS', 'MMC', 'BTC', 'BTM', 'EMC2', 'LCL', 'VOX', 'JLH', 'STEEM', 'BCN', 'STRAT', 'BLK', 'DVK', 'SLR', 'CRYPT', 'FZ', 'ACH', 'BCC', 'UTIL', 'ETC', 'GAME', 'CURE', 'TWE', 'BCY', 'NL', 'ETH', 'MUN', 'SMC', 'FLDC', 'CON', 'DGB', 'CLAM', 'ECC', 'GOLD', 'PRT', 'CGA', 'GEMZ', 'OMNI', 'UIS', 'XLB', 'KDC', 'VRC', 'TOR', 'MAST', 'PMC', 'C2', 'QTL', 'BITS', 'EMO', 'FCN', 'VTC', 'CORG', 'SRG', 'PAWN', 'DIME', 'CC', 'XC', 'QORA', 'SYNC', 'LTC', 'RDD', 'FRQ', 'AUR', 'COMM', 'FZN', 'DNS', 'DIEM', 'ADN', 'MINT', 'AEON', 'XMR', '1CR', 'MEC', 'HIRO', 'IOC', 'HVC', 'XDP', 'NAUT', 'ITC', 'PLX', 'H2O', 'NMC', 'KEY', 'SC', 'XMG', 'BITCNY', 'GDN', 'XHC', 'GNS', 'SHOPX', 'GNT', 'NXT', 'MNTA', 'YC', 'STR', 'RIC', 'LOL', 'AIR', 'HYP', 'CAI', 'BBL', 'WDC', 'ARCH', 'GNO', 'DIS', 'PPC', 'HUGE', 'SOC', 'SBD', 'LC', 'EAC', 'DAO', 'XPB', 'X13', 'GAP', 'CYC', 'BOST', 'YANG', 'MMNXT', 'FAC', 'NSR', 'MON', 'NBT', 'AC', 'BALLS', 'SUM', 'RBY', 'GPUC', 'AERO', 'CNOTE', 'NEOS', 'HOT', 'RZR', 'N5X', 'PAND', 'CNMT', 'ABY', 'CNL', 'MRS', 'CACH', 'BANK', 'PINK', 'MCN', 'DICE', 'LGC', 'JPC', 'SQL', 'UNITY', 'XST', 'EBT', 'ARDR', 'eTOK', 'SDC', 'NRS', 'TRUST', 'POT', 'PIGGY']
features = ['txFee', 'minConf', 'disabled', 'delisted', 'frozen']

def returnResult():
    result = []
    try:
        response = requests.get(url)
        data = response.json()
    except:
        for i in range(0, 1325):
            result.append(float('nan'))
        print("returnCurrencies failed, appending nan: " + str(len(result)))
        return result
    for currency in currencies:
        for feature in features:
            try:
                result.append(pd.to_numeric(data[currency][feature], 'coerce'))
            except:
                result.append(float('nan'))

    print("returnCurrencies: " + str(len(result)))
    return(result)
