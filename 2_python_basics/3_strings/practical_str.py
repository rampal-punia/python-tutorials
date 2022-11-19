invoice = '''
0.........11..............27......36.........
Bill No.    Item            Qty     Amount
=============================================
9801        Laptop          2       180000   
9802        Head Phone      5       25000    
9803        Monitor         10      200000   
9804        Smart Phone     2       80000   
9805        PC              5       300000   
'''

line_items = invoice.splitlines()
line_items = line_items[4:]
# print(line_items)

prices = []
for item in line_items:
    # price = int(item[36:None].rstrip())
    price = item[36:None]
    price = price.rstrip()
    price = int(price)
    prices.append(price)

print(sum(prices))
