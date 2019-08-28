instr=input("enter the string")
vowal=['a','e','i','o','u']
cgroup=dict()
vgroup=[]
outstr=''
for h in instr:
    i=h.lower()
    if (i in vowal):
        vgroup.append(h)
    else:

        if i in cgroup.keys():
            cgroup[i]=cgroup[i]+h
        else:
            cgroup[i]=h
vgroup=sorted(vgroup)
cgroup1=sorted(cgroup.keys())
cgroup2=[]
for i in range(len(instr)):
    if i<len(cgroup1)-1:
        outstr=outstr+cgroup[cgroup1[i]]
        cgroup2.append(cgroup[cgroup1[i]])
    if i < len(vgroup)-1:
        outstr=outstr+vgroup[i]
print(cgroup2)
print(vgroup)
print(outstr)








