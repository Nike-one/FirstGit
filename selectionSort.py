#selection sorting
l = [1,6,4,5,3,2]
for i in range(len(l)):
	min_ = i
	for j in range(i+1, len(l)):
		if(l[min_]>l[j]):
			min_ = j

	l[i] , l[min_] = l[min_], l[i]
for i in range(len(l)):
	print(l[i], end = " ")

#Output 1 2 3 4 5 6