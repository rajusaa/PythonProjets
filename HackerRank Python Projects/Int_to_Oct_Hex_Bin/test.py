N = int(input())
width = len(bin(N))
for i in range(N+1):
	print( str(i).rjust(width),oct(i).rjust(width),hex(i).rjust(width),bin(i).rjust(width))
