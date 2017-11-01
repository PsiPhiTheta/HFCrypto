import time
import returnOrderBook
import returnTicker
import returnLoanOrders
import return24hVolume
import returnCurrencies
import githubParser

NUMBER_EXPECTED_FEATURES = 6222

def introduceNan(amount):
    for i in range(amount):
        outfile.write('nan,')
    return []

while(True):
    actualTime = time.time()
    data = []
    data.append(time.time())

    with open('data.txt', 'a') as outfile:
        numberFeatures = 0
        outfile.write(str(actualTime))

        try:
            resultOrderBook = returnOrderBook.returnResult()
            if(len(resultOrderBook) < 3780):
                raise TimeoutError('API failed')
        except:
            print('Error of resultOrderBook')
            resultOrderBook = introduceNan(3780)

        try:
            resultTicker = returnTicker.returnResult()
            if(len(resultTicker) < 900):
                raise TimeoutError('API failed')
        except:
            print('Error of resultTicker')
            resultTicker = introduceNan(900)

        try:
            resultLoanOrders = returnLoanOrders.returnResult()
            if(len(resultLoanOrders) < 32):
                raise TimeoutError('API failed')
        except:
            print('Error of resultLoanOrders')
            resultLoanOrders = introduceNan(32)

        try:
            result24hVolume = return24hVolume.returnResult()
            if(len(result24hVolume) < 180):
                raise TimeoutError('API failed')
        except:
            print('Error of result24hVolume')
            result24hVolume = introduceNan(180)

        try:
            resultCurrencies = returnCurrencies.returnResult()
            if(len(resultCurrencies) < 1325):
                raise TimeoutError('API failed')
        except:
            print('Error of resultCurrencies')
            resultCurrencies = introduceNan(1325)

        try:
            githubFeature = githubParser.returnResult()
            if(len(githubFeature) < 5):
                raise TimeoutError('API failed')
        except:
            print('Error of resultCurrencies')
            githubFeature = introduceNan(5)

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
        time.sleep(300 - (300 % abs(time.time() - actualTime)))
