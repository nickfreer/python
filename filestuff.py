f = open("testdata")
n = open("resultdata","a")

for c in f.read():
    print(c)
    n.write('NDF:'+c)
f.close()
n.close()
f = open("testdata")
for l in f:
    print(l)