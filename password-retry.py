password = 'a123456'
i = 3

while i > 0:
    i = i - 1
    psw = input('請輸入您的密碼： ')
    if psw == password:
    	print('登入成功！')
    	break
    elif i > 0:
    	print('密碼錯誤！你還有', i, '機會')
    else:
    	print('密碼已被鎖定')
    
