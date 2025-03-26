left =  [3,4,2,1,3,3]
right = [4,3,5,3,9,3]

left.sort()
right.sort()

distance_sum = sum(abs(l-r) for l,r in zip(left,right))
print(distance_sum)


