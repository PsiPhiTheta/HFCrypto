import time
import returnOrderBook
import returnTicker
import returnLoanOrders
import return24hVolume
import returnCurrencies
import githubParser

while(True):
    actualTime = time.time()
    data = []
    data.append(time.time())

    with open('data.txt', 'a') as outfile:
        outfile.write(str(actualTime))
        for i in returnOrderBook.returnResult():
            outfile.write(str(i) + ',')
        for i in returnCurrencies.returnResult():
            outfile.write(str(i) + ',')
        for i in return24hVolume.returnResult():
            outfile.write(str(i) + ',')
        for i in returnLoanOrders.returnResult():
            outfile.write(str(i) + ',')
        for i in returnTicker.returnResult():
            outfile.write(str(i) + ',')
        for i in githubParser.returnResult():
            outfile.write(str(i) + ',')
        outfile.write('\n')
        time.sleep(300 - (time.time() - actualTime))