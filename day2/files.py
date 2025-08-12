file_name='file_numbers'
with open('number.txt', 'r',) as file:
    num=file.read()
    while ' ' in num:
        num=num.replace(' ','')
    num=num.split(',')
    nums_2=[ int(i) for i in num if i.isdigit() and int(i)%2==0]
with open(f'{file_name}.txt', 'w',) as file2:
    for i in nums_2:
        file2.write(str(i)+'\n')



