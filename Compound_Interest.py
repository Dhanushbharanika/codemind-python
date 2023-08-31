p=int(input())
r=int(input())
t=int(input())
am=p*(1+r/100)**t
ci=round(am-p,2)
print(f"{ci:.2f}")