#Accessing string
s="learning python"
print(s[2])
print(s[5])

#Indexing string
s="learning python"
print(s[0:12:2])

l=len(s)
for i in range(1):
    if (s[i]=="p"):
        print(i)
        #manipulating string (concatenation ,repetation)
        s1="python"
        s2="django"
        print(s1+s2)
        print(s1+" "+s2)

        print((s1+" ")*10)
        print(s1*5 +s2*5)
        #string methods: find
        word="learning python is very essay"
        print(word.find("p"))
        print(word.find("h"))
        #count()
        word="learning python is very essay"
        print(word.count("r"))
        w="learning"
        print(len(w))
        w1=w.strip()
        print(len(w))
        #rstrip
        w="learning"
        w1=w.rstrip()
        print(len(w1))
        #split()
        w="learning python is very essay"
        print(word.split("e"))
        w="learning python is very essay"
        print(len(word))
        l=word.split("n")
        print(len(1))

        #slicing for string collection
        st="python is essay"
        print(st[-14:-9+1])
        print(st[-1:14-1:-1])
        print(st[-9:-14-1:-1])
