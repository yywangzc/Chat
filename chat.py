
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: # 會把記事本多存的\ufeff去掉
		for line in f:
			lines.append(line.strip()) # strip()把換行符號去掉
	return lines

def convert(lines):
	new = []
	#person = '123' # 為避免當第一欄非人名時程式會當掉
	person = None # 預設值設定成 "無"
	for line in lines:
		if line == 'Dustin':
			person = 'Dustin'
			continue
		elif line == 'Andy':
			person = 'Andy'
			continue
		
		#if person != '123':
		if person:
			new.append(person + ': ' + line)
	return new
		
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	#print(lines)
	lines = convert(lines)
	write_file('output.txt', lines)

main() # 程式的進入點