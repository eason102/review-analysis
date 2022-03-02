data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1
        if count % 1000 == 0:
            print(len(data))
sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print(sum_len / len(data) )

new = []
for d in data:    #從清單中讀取
    if len(d) < 100: #求長度小於一百
        new.append(d) #加到新的清單裡面
print(len(new)) #印出新清單裡面有幾筆資料

good = []
for c in data:          #讀取清單
    if 'good' in c:     #篩選清單裡面有good的字串
        good.append(c)  #加到good清單裡面
print(len(good))        #印出good清單裡面有多少項目
print(good[1])          #印出清單裡第二個項目