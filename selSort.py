def selSort(L):
	for i in range(len(L)-1):
		print L
		minIndx = i
		minVal = L[i]
		j = i + 1
		while j < len(L):
			if minVal > L[j]:
				minIndx = j
				minVal = L[j]
			j = j + 1
		temp = L[i]
		L[i] = L[minIndx]
		L[minIndx] = temp 
