# challengez

Armstrong

num = int(input("Enter a number: "))
original_num = num
digits_count = len(str(num))
total = 0

while num > 0:
    digit = num % 10          
    total = total + (digit ** digits_count)  
    num = num // 10           
if total == original_num:
    print("It is an Armstrong number, this is the sum:", total)
else:
    print("It is NOT an Armstrong number, this is the sum:", total)
