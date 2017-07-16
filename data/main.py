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
        resultOrderBook = returnOrderBook.returnResult()
        resultTicker = returnTicker.returnResult()
        resultLoanOrders = returnLoanOrders.returnResult()
        result24hVolume = return24hVolume.returnResult()
        resultCurrencies = returnCurrencies.returnResult()

        for i in resultOrderBook:
            numberFeatures += 1
            outfile.write(str(i) + ',')
        for i in resultCurrencies:
            numberFeatures += 1
            outfile.write(str(i) + ',')
        for i in result24hVolume:
            numberFeatures += 1
            outfile.write(str(i) + ',')
        for i in resultLoanOrders:
            numberFeatures += 1
            outfile.write(str(i) + ',')
        for i in resultTicker:
            numberFeatures += 1
            outfile.write(str(i) + ',')
        for i in githubParser.returnResult():
            numberFeatures += 1
            outfile.write(str(i) + ',')
        outfile.write('\n')
        print("Number of features: " + str(numberFeatures) + " | Time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
        time.sleep(300 - (time.time() - actualTime))