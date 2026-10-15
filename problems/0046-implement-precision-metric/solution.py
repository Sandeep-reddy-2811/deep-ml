import numpy as np
def precision(y_true, y_pred):
	# Your code here
	tp = 0
	fp = 0
	for i in range(len(y_true)):
		if(y_true[i] == 1 and y_pred[i] == 1):
			tp += 1
		elif(y_true[i] == 0 and y_pred[i] == 1):
			fp += 1
	if tp == 0 and fp == 0: return 0
	pre = tp/(tp+fp)

	return pre
	pass
