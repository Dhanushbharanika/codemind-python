s=int(input())
H=s//3600
M=(s%3600)//60
K=(s%3600)%60
print(f"H:M:S-{H}:{M}:{K}")