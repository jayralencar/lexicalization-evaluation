# import fscore

# gold = [1,2,34,52,3,4,56,2,1,4,53,6]
# test = [1,2,34,52,3,0,56,2,1,4,5,36,43]

# pre = fscore.precision(gold, test)
# rec = fscore.recall(gold, test)

# fs = fscore.f1score(gold, test)

# print(pre,rec,fs)

from nltk.metrics.scores import (precision, recall,f_measure)
import collections
import nltk.metrics

reference = set(["die","eat","play","calc"])
test = set(["walk","eat","play","calc", "make"])

p = precision(reference, test)
r = recall(reference, test)
f = f_measure(reference,test)

print(p,r,f)