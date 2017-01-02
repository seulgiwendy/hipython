def calculate_change(payment, cost):
    omanwon=50000
    manwon=10000
    ocheonwon=5000
    cheonwon=1000
    changeamount=payment-cost
    
    print("5manwon %d jang" %(changeamount/omanwon))
    changeamount = changeamount % omanwon
    print("manwon %d jang" %(changeamount/manwon))
    changeamount = changeamount % manwon
    print("5cheonwon %d jang" %(changeamount/ocheonwon))
    changeamount = changeamount % ocheonwon 

    print("cheonwon %d jang" %(changeamount/cheonwon))
    changeamount = changeamount % cheonwon 

calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
print()


