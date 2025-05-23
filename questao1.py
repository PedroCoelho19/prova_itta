
def gerar():
    for i in range(2,101,2):
        yield i
for par in gerar():
    print(par)
    