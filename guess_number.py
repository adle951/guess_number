import random
start = int(input('初始範圍'))
end = int(input('結束範圍'))
r = random.randint(start, end)
count = 0
while True:
	num = int(input('請猜數字:'))
	count += 1
	if r == num:
		print('恭喜猜對了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是第:', count, '次' )



