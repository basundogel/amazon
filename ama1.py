data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1  # count = count + 1
		if count % 1000 == 0: 
			print(len(data))
print('讀取完畢,總共有', len(data), '筆資料>.^')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均度是', sum_len / len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)	
		sum_len = sum_len + len(d)
print('共有', len(new), '筆留言 字數<100')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('There are', len(good), 'reviews including "good"')
print(good[0])


# 清單快寫法
bad = [d.strip() + 'QQ' for d in data if 'bad' in d]
print(bad)

# bad = []
# for d in data:
# 	if 'bad' in d:
# 		bad.append(d.strip())
# print(bad)

bad = ['bad' in d for d in data]
print(bad)


# 文字計數
wc = {} # word_count 
for d in data:
	words = d.strip().split() #split()預設是空白鍵 #若有連續空白鍵，不會切成空字串
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc)) 
print(wc['Andy'])

while True:
	word = input('請輸入要找的字:')
	if word == 'q':
		break
	elif word in wc:
		print(word, '出現過', wc[word], '次')
	else:
		print('這個字沒出現過喔~')

print('感謝使用本查詢功能')



