a=10#Global Variable
def friends():
    a= 69# Global Variable inside function which is given more preference than a=10
    x=globals()['a']
    print("Koushik",a)
    globals()['a']=15# Global Variable outside function for Nagaraju Where preference is given more for a=15
friends()
print("Nagaraju",a)