def printTransactions(m, k, d, name, owned, prices):
    transactions = []
    for i in range(k):
        avg_4_days = sum(prices[i][:4]) / 4
        current_price = prices[i][4]
        
        if current_price < avg_4_days and m >= current_price:
            shares_to_buy = int(m // current_price)
            if shares_to_buy > 0:
                transactions.append(f"{name[i]} BUY {shares_to_buy}")
                m -= shares_to_buy * current_price
                
        elif current_price > avg_4_days and owned[i] > 0: 
            transactions.append(f"{name[i]} SELL {owned[i]}")
    print(len(transactions))
    for transaction in transactions:
        print(transaction)
m = 90
k = 2
d = 400
name = ["iStreet", "HR"]
owned = [10, 0]
prices = [
    [4.54, 5.53, 6.56, 5.54, 7.60],
    [30.54, 27.53, 24.42, 20.11, 17.50]
]
printTransactions(m, k, d, name, owned, prices)
