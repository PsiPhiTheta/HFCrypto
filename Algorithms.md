# 1. Trend Following (algo)

Description: Follows trends in moving averages, channel breakouts, price level movements and related technical indicators. Does not involve making any predictions or price forecasts. Trades are initiated based on the occurrence of desirable trends, which are easy and straightforward to implement through algorithms without getting into the complexity of predictive analysis.

Advantages: backtestable, easy to understand, simple to implement, heavily documented

Disadvantages: not very applicable to cryptocurrencies that fluctuate greatly and with little discernable trend.

> Include consensus: NO (Tom, ?, ?) 

# 2. Arbitrage Opportunity (algo)

Description: Buying a dual listed stock at a lower price in one market and simultaneously selling it at a higher price in another market offers the price differential as risk-free profit or arbitrage. The same operation can be replicated for stocks versus futures instruments, as price differentials do exists from time to time. Implementing an algorithm to identify such price differentials and placing the orders allows profitable opportunities in efficient manner.

Advantages: 

Disadvantages: may be complex to execute cross-market trades within the Poloniex API

> Include consensus: NO (Tom, ?, ?)

# 3. Description Index (algo)

Description: Index funds have defined periods of rebalancing to bring their holdings to par with their respective benchmark indices. This creates profitable opportunities for algorithmic traders, who capitalize on expected trades that offer 20-80 basis points profits depending upon the number of stocks in the index fund, just prior to index fund rebalancing. Such trades are initiated via algorithmic trading systems for timely execution and best prices.

Advantages: 

Disadvantages: 

> Include consensus: ? (?, ?, ?)

# 4. Mathematical Model-Based (algo)

Description: A lot of proven mathematical models, like the delta-neutral trading strategy, which allow trading on combination of options and its underlying security, where trades are placed to offset positive and negative deltas so that the portfolio delta is maintained at zero.

Advantages: easy to code

Disadvantages: takes time to develop model, cryptocurrencies will be difficult to fit to a model as their fluctuation is mostly random or based on real world events (Bitcoin and energy price in asian, Gridcoin and simplicity of UI...)

> Include consensus: NO (Tom, ?, ?)

# 5. Mean reversion (algo)

Description: Mean reversion strategy is based on the idea that the high and low prices of an asset are a temporary phenomenon that revert to their mean value periodically. Identifying and defining a price range and implementing algorithm based on that allows trades to be placed automatically when price of asset breaks in and out of its defined range.

Advantages: easy to code

Disadvantages: not found any evidence to suggest that cryptos revert to their mean periodically (mostly highly volatile behaviours without a mean)

> Include consensus: NO (Tom, ?, ?)

# 6. Volume Weighted Average (algo)

Description: Volume weighted average price strategy breaks up a large order and releases dynamically determined smaller chunks of the order to the market using stock specific historical volume profiles. The aim is to execute the order close to the Volume Weighted Average Price (VWAP), thereby benefiting on average price.

Advantages: 

Disadvantages: 

> Include consensus: ? (?, ?, ?)

# 7. Time Weighted Average Price (algo)

Description: Time weighted average price strategy breaks up a large order and releases dynamically determined smaller chunks of the order to the market using evenly divided time slots between a start and end time. The aim is to execute the order close to the average price between the start and end times, thereby minimizing market impact.

Advantages: 

Disadvantages: 

> Include consensus: ? (?, ?, ?)

# 8. Percentage of Volume (algo)

Description: Until the trade order is fully filled, this algorithm continues sending partial orders, according to the defined participation ratio and according to the volume traded in the markets. The related "steps strategy" sends orders at a user-defined percentage of market volumes and increases or decreases this participation rate when the stock price reaches user-defined levels.

Advantages: 

Disadvantages: 

> Include consensus: ? (?, ?, ?)

# 9. Implementation shortfall (algo)

Description: The implementation shortfall strategy aims at minimizing the execution cost of an order by trading off the real-time market, thereby saving on the cost of the order and benefiting from the opportunity cost of delayed execution. The strategy will increase the targeted participation rate when the stock price moves favorably and decrease it when the stock price moves adversely.

Advantages: 

Disadvantages: 

> Include consensus: ? (?, ?, ?)

# 10. Competition sniffing (algo)

Description: Searches for purchasing trends in the market and attempts to mimic the most sucessful buyers until their performance drops before mimicking another host.

Advantages:

Disadvantages: 

> Include consensus: ? (?, ?, ?)

# 11. Tom's Github tracking (algo)

Description: Monitors cryptocurrency's Github activity (number of issues resolved, commit rate, page hits...) to predict future performance of coin.

Advantages: simple to code

Disadvantages: may not be corrolated to currency performance

> Include consensus: YES (Tom, ?, ?)

# 12. Tom's google searches tracking (algo)

Description: Monitors cryptocurrency's google search frequency to predict future performance of coin.

Advantages: simple to code

Disadvantages: may not be corrolated to currency performance

> Include consensus: YES (Tom, ?, ?)

# 13. Tom's main webpage hits tracking (algo)

Description: Monitors cryptocurrency's main webpage hits frequency to predict future performance of coin.

Advantages: simple to code

Disadvantages: may not be corrolated to currency performance

> Include consensus: YES (Tom, ?, ?)

# 14. Twitter tracking (algo)

Description: Monitors twitter sentiments to predict future performance of coins.

Advantages: prooved to be corrolated to currency performance (http://cs229.stanford.edu/proj2015/029_report.pdf)

Disadvantages: may be extremely hard to code (requires AI analysis and translation of words into trading advantages) 

> Include consensus: YES (Tom, ?, ?)


# Sources

- investopedia.com 
