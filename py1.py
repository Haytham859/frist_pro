""""

"""


# def copies(word,n):
#     if (n>0):
#         for x in range(0,n):
#             print(word)
            
    



# copies("haythem",5)


def vowel(word):
    count=0
    for x in range(0,len(word)):
        if(word[x]=='a' or word[x]=='e'or word[x]=='i'or word[x]=='o' or word[x]=='u'):
            count=count+1
            
    for x in range(0,len(word)):
        if(word[x]=='a' or word[x]=='e'or word[x]=='i'or word[x]=='o' or word[x]=='u'):
            count=count+1
            
    if (count==0):
        print("not found vowel")
    else:
        print("found vowel")

vowel("hello")



l=[1,2,4,20,4]
for x in range(0,len(l)):
    for y in range(0,l[x]):
        print("@",end="  ")
    
    print("")
    
    
# word="hello"
# dec={}
# for x in range(0,len(word)):
#         if x in dec:
#             dec[word[x]]+=1
#         else:
#             dec[word[x]]=1
        
# print(dec)
    





