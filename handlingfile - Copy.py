#text=open('sample.txt','r+')
#text.write("sample")
#print(text.readlines())
#text=open('sample2.txt','w')
#text.write("sample file content")
#text.close()
'''text1=open('sample3.txt','w')
text1.write("Hello\n")
text1.close()
text2=open('sample3.txt','a')
text2.write("Good morning\n")
text2.write("Bye Bye")
text2.close()
text3=open("sample3.txt")
a=text3.read()
b=text3.readline()
print(b)
for x in b:
    print(x.rstrip('\n'))'''
text=open('sample3.txt','r+')
a=text.readlines()
#text1=open('sample3.txt')
#b=text.readline()
#print(text1.readlines())
#text1.close()
print(a)
text.seek(0,0)
b=text.readline()
print(b)
text.seek(0,3)
c=text.tell()
print(c)
x=['abc','bcd','cde','def']
d=text.writelines(x)
text.seek(0,0)
print(text.read())
text.close()
#print(text.tell())
#print(b)
