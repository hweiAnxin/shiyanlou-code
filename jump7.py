for num in range(1,101):
    if num % 7 != 0 and num % 10 != 7 and num // 10 != 7:
        print('这个数字是{}'.format(num))
