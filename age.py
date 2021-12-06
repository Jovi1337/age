driving = input('請問你有沒有開過車?')
if driving != '有' or '沒有':
	print('請輸入【有】 或者 【沒有】')
	raise SystemExit

age = input('請你的年齡?')

age = int(age)


if driving == '有':
	if age >= 18:
		print('你是在合法年齡開車')
	else:
		print('非法年齡')
elif driving == '沒有':
	if age < 18:
		print('你還不到合法年齡')
	else:
		print('你已經到了合法年齡，可以考取汽車駕照')
else:
	print('請輸入【有】 或者 【沒有】')
