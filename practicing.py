# def h_e(h,l):
#     n=h+l
#     return n
# l= input("enter first number ")
# h= input("enter second number ")
# print(h_e(h,l))


def mixstrings(s1,s2):
    s2=s2[::-1]
    s3=""
    for i in range(len(s1)):
        s3=s3+s1[i]+s2[i]
    return s3
s1=input("Please enter your first word: ")
s2=input("Please enter your second word: ")
print(mixstrings(s1,s2))
