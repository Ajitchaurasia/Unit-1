#tes1
price=20  #$20
original_price = 25  #$25
if price>=original_price:
    print("expected price is: ",original_price);
else:
    original_price=(original_price*0.1)+price;
print("expected price is:",original_price);

#test2
price=20  #$20
original_price= 20 #$20
if price>=original_price:
    print("expected price is:", original_price);
else:
    original_price=(original_price*0.1)+price;
print("expected price id: ",original_price);


#test3
price=20 #$20
original_price= 15 #$25
if price>=original_price:
    print("expected price is:", original_price);
else:
    original_price=(original_price*0.1)+price;
print("expected price is:",original_price);