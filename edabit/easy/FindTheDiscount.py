def dis(price, discount):
	dis = price * (discount/100)
	saleprice = price - dis
	saleprice = round(saleprice,2)
	return saleprice