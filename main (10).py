
item1 = input().split()
cod1 = int(item1[0])
qnt1 = int(item1[1])
val1 = float(item1[2])


item2 = input().split()
cod2 = int(item2[0])
qnt2 = int(item2[1])
val2 = float(item2[2])


total = (qnt1 * val1) + (qnt2 * val2)


print(f"VALOR A PAGAR: R$ {total:.2f}")