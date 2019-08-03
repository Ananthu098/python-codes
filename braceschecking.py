str=input("enter the string")
arr1=['{','[','(']
arr2=['}',']',')']
a=len(str)
arr3=[]
i=0
ar=0
while i<a:
 
 j=0
 while j<3:
     if str[i]==arr1[j]:
      arr3.append(str[i])
      break
     else:
      if str[i]==arr2[j]:
          n=len(arr3)
          k=n-1
          while k>=0:
              if arr3[k]==arr1[j]:
               arr3.pop(k)
               break
              k-=1
          if n==len(arr3):
           arr3.append(str[i])
          break
     j+=1
 i+=1
print(arr3)
print("no of unclosed braces:",len(arr3))






