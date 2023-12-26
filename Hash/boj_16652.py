from sys import stdin
n, k = map(int,stdin.readline().split())
mails = [stdin.readline().split() for i in range(k)]
print(mails)
mail_list = dict()
tmp_re = 0

for mail in mails:
    mail_list[mail[-1]] = 0
    
for mail in mails:
    sub = mail[-1]
    tmp_re = mail.count('Re:') + 1
    if mail_list[sub] < tmp_re:
        mail_list[sub] = tmp_re
mail_sum = 0
for max_re in mail_list.values():
    mail_sum += max_re

if n >= mail_sum:
    print('YES')
else:
    print('NO')
