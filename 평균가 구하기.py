o=[]
o.append(int(input("1등 상품 가격 : ")))
o.append(int(input("2등 상품 가격 : ")))
o.append(int(input("3등 상품 가격 : ")))
o.append(int(input("4등 상품 가격 : ")))
o.append(int(input("5등 상품 가격 : ")))

avg = sum(o) / len(o)
print()
print()
print()
print("평균가 : ",avg,"￦")