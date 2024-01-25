#input
com_rate = float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))
float(input("Enter commission rate percentage (ex 0.03) on stock sale: "))
num_shares = int(input("Enter number of shares purchased: "))
int(input("Enter number of shares sold: "))
purchase_price = float(input("Enter purchase price per share: "))
sell_price = float(input("Enter selling price per share: "))

#setting formula

amountpaid = num_shares * purchase_price
purch_comish = com_rate * amountpaid
totalpaid = amountpaid + purch_comish
stocksoldfor = num_shares * sell_price
sell_comish = com_rate * stocksoldfor
recieved = stocksoldfor - sell_comish
profitorloss = recieved - totalpaid

#display
print("----------------------------------------------------------------------------")

print("Amount paid for stock:", "$" + format(amountpaid, ",.2f" ))

print("Commission paid on the purchase:", "$" + format(purch_comish, ",.2f"))

print("Amount the stock sold for:", "$" + format(stocksoldfor, ",.2f"))

print("Commission paid on the sale:", "$" +format(sell_comish, ",.2f"))

print("Profit (or loss if negative:",  "$" +format(profitorloss, ",.2f"))
