while True:
    num=input()
    if int(num)==0:
        break
    if num==''.join(list(num)[::-1]):
        print('yes')
    else:
        print('no')