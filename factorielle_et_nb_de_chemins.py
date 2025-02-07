from functools import cache
# ~ row=5
# ~ col=4
row=int(input("row ? : "))
col=int(input("col ? : "))

# ~ def fac(n):
	# ~ if n==0:return 1
	# ~ r=n
	# ~ while n>2:
		# ~ n-=1
		# ~ r*=n
	# ~ return r
@cache
def fac(n):
	if n==0:return 1
	return n*fac(n-1)
# ~ print(fac(5))
# ~ print(fac(10))
# ~ print(fac(0))

R=col-1
B=row-1
D=0
tt=0
while True:
	res=fac(R+B+D)/fac(R)/fac(B)/fac(D)
	print(res)
	tt+=res
	if R>0 and B>0:
		R-=1
		B-=1
		D+=1
	else:break
print("methode math des permutations :",int(tt))
ca=0

RC={}
def gnp(r,c):
	if (r,c) in RC:return RC[r,c]
	if c==col-1:return 1
	if r==row-1:return 1
	v=gnp(r+1,c)+gnp(r,c+1)+gnp(r+1,c+1)
	RC[r,c]=v
	return v
print("methode grille recursive:",gnp(0,0))
@cache
def gnp(r,c):
	if c==col-1:return 1
	if r==row-1:return 1
	v=gnp(r+1,c)+gnp(r,c+1)+gnp(r+1,c+1)
	return v
print("methode grille recursive (cached):",gnp(0,0))
print(ca)


