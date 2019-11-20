for i in range(5):
    print (i)
    if i == 3:
        break
else:
    print("here")

print("zy90".isalnum())

l=[0,1,-2,3,-4]
print([x for x in l if x<0])

x=456
print("%-006d"%x)

print(2+4.00, 2**4.0)

x=-122
print("-%006d"%x)

print(float(26//3+3/3))

print('abc'.encode())

s={4>3,0,3-3}
print(all(s))
print(any(s))

print(list(enumerate([2,3])))
x=2
print(x>>2)

print('abcd'.translate('a'.maketrans('abc','bcd')))

print(float('-infinity'))
print(float('inf'))

a={3,4,5}
a.update([1,2,3])
print(a)
print('new' 'line')

a=[(2,4),(1,2),(3,9)]
a.sort()
print(a)

t1=(1,2,3,4)
t2=(1,2,4,3)
print(t1<t2)

str="hello"
print(str[:2])

lst=[3,4,6,]

print('abcdefcdghcd'.split('cd',2))

list1=[1,3]
list2=list1
list1[0]=4
print(list2)

print('abcdef12'.replace('cd','12'))

print('abcdefcdghcd'.split('cd',0))
x=3
print(eval('x^2'))

print("abcdef".find("cd"))

d={"john":40,"peter":45}
print(d)
del d["john"]
print(d)

print(''.isdigit())

str="hello"
print(str[-1:])

for i in [1,2,3,4][::-1]:
    print(i)


s={2,5,6,6,7}
print(s)

print("Hello".replace("l","e"))

data={1}