# 清單的分割寫法:
# n[開始值:結束值] (開始有包含, 結束不包含)
# 範例:
# n = [2, 6, 6, 8, 4]
# n[:3] 可以拿到前三個 (開始值是0可以不用寫) --> [2, 6, 6]
# n[2:4] 可以拿到一個清單裝著n[2]跟n[3] --> [6, 8]
# n[-2:] 可以拿到最後兩個, 結尾值不寫表示到底 --> [8, 4]


def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # 會把記事本多存的\ufeff去掉
		for line in f:
			lines.append(line.strip()) # strip()把換行符號去掉
	return lines


def convert(lines):
	person = None # 預設值設定成 "無"
	yy_word_count = 0
	yy_sticker_count = 0
	yy_image_count = 0
	andy_word_count = 0
	andy_sticker_count = 0
	andy_image_count = 0
	for line in lines:
		s = line.split(' ') # 遇到空白鍵做切割成清單
		time = s[0]
		name = s[1]
		if name == '歪歪':
			if s[2] == '貼圖':
				yy_sticker_count += 1
			elif s[2] == '圖片':
				yy_image_count += 1
			else:
				for m in s[2:]:
					yy_word_count += len(m)
		elif name == 'Andy':
			if s[3] == '貼圖':
				andy_sticker_count += 1
			elif s[3] == '圖片':
				andy_image_count += 1
			else:
				for m in s[3:]:
					andy_word_count += len(m)
	print('歪歪說了', yy_word_count, '個字')
	print('歪歪傳了', yy_sticker_count, '個貼圖')
	print('歪歪傳了', yy_image_count, '張圖片')

	print('Andy Chen說了', andy_word_count, '個字')
	print('Andy Chen傳了', andy_sticker_count, '個貼圖')
	print('Andy Chen傳了', andy_image_count, '張圖片')

		#print(s)

		
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE]Andy.txt')
	#print(lines)
	lines = convert(lines)
	#write_file('output.txt', lines)

main() # 程式的進入點