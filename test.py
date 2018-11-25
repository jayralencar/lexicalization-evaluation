import evaluation

print ("OntoRisco:")

evaluation.evalues('ontorisco')

print("\n")

print ("DbPedia:")

evaluation.evalues('dbpedia_en')

print("\n")

print ("QALD3 train:")

evaluation.evalues('qald_train')

print("\n")
print ("QALD3 test:")

evaluation.evalues('qald_test')