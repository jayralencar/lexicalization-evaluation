import numpy as np

def recall(relevant, retrieved):
    inter = intersection(relevant, retrieved)
    return inter/len(relevant)

def precision(relevant, retrieved):
    inter = intersection(relevant, retrieved)
    return inter/len(retrieved)

def f1score(relevant, retrieved):
    rec = recall(relevant, retrieved)
    pre = precision(relevant, retrieved)

    return 2*((pre*rec)/(pre+rec))

def intersection(lst1,lst2):
    lst3 = [value for value in lst1 if value in lst2] 
    return len(lst3) 
    