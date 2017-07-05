def my_abs(num):
	if type(num)== int or type(num) == float:
		return abs(num)
	else: 
		try:
			num_trans=float(num)
			return abs(num_trans)
		except:
			return '数据不符合类型'