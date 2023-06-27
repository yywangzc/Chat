
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in  lines:
	s = line.split(' ')
	time = s[0][:5] # 字串 str 可以當成清單來看待, 也可用清單切割法
	name = s[0][5:]
	print(name)
