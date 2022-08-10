import random
r = random.randint(1, 100)
while True:
	num = int(input('請猜數字:'))
	if r == num:
		print('恭喜猜對了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')

