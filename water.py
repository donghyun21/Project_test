user_input = input("값들을 공백으로 구분하여 입력하세요: ")

lst = list(map(int, user_input.split()))

maximum_height = max(lst)
water = [0] * maximum_height
sum = 0

for i in range(maximum_height):
    height = i+1
    first = True
    temp = 0
    for j in range(len(lst)):
        if lst[j] >= height:
            if first:
                first = False
                temp = 0
            else:
                water[i] += temp
                temp = 0
        else:
            temp += 1
    sum += water[i]
print(water)
print(sum)
        
        