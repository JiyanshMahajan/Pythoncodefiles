num =int(input("153:"))
original_num =num
order=len(str(num))
sum_of_powers=0
temp=num
while temp > 0:
    digit=temp%10
    sum_of_powers += digit **order
    temp //=10
if sum_of_powers== original_num:
    print(original_num,"is an Armstrong number")
else:
    print(original_num,"is not an Armstrong number")