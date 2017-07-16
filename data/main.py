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
        numberFeatures = 0
        outfile.write(str(actualTime))
        for i in returnOrderBook.returnResult():
            numberFeatures += 1
            outfile.write(str(i) + ',')
        for i in returnCurrencies.returnResult():
            numberFeatures += 1
            outfile.write(str(i) + ',')
        for i in return24hVolume.returnResult():
            numberFeatures += 1
            outfile.write(str(i) + ',')
        for i in returnLoanOrders.returnResult():
            numberFeatures += 1
            outfile.write(str(i) + ',')
        for i in returnTicker.returnResult():
            numberFeatures += 1
            outfile.write(str(i) + ',')
        for i in githubParser.returnResult():
            numberFeatures += 1
            outfile.write(str(i) + ',')
        outfile.write('\n')
        print("Number of features: " + str(numberFeatures) + " | Time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
        time.sleep(300 - (time.time() - actualTime))