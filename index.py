num = int(input("Enter a number: "))
odd = 1
for i in range(num):
    odd += 2
    print(odd,end = ",")


# string = input("enter a word: ")
# vowels = ("a","e","i","o","u","A","E","I","O","U")
# for char in string:
#     if char in vowels:
#         string = string.replace(char,"")
# print(string)        



# word = input("Enter a word: ")
# reverse =""
# for char in word:
#     reverse= char + reverse 
# print(reverse)    



# string = input("enter a sentence: ")
# result = "".join(sorted(string))
# print(result)




# list =[9,2,4,5,3,8,6,7,1]
# asc = sorted(list)
# index = len(asc)-2
# second_largest = asc[index]
# print(second_largest)



# input = input("Enter: ")
# if input.isdigit()==True:
#     print("Given input is number")
# else:
#     print("Given input is Alphabet")


# factorial of a number

# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1,num+1):
#     if num<0:
#         print("Not possible")
#     else:
#         fact = fact * i
# print("factorial of",num,"is",fact)


# ascending order
# word = input("enter a set: ").split()
# result = " ".join(sorted(word))
# print(result)



# num = 1222
# reverse = int(str(num)[::-1])
# if reverse==num:
#     print("palindrome")
# else:
#     print("not a palindrome")


# reverse a each word


# sentence = input("enter a sentence: ").split()
# for i in range(0,len(sentence)):
#     sentence[i]=sentence[i][::-1]
# result = " ".join(sentence)
# print(result)


# k sum pairs

# def get_unique_pairs(int_list,pair_sum):
#     step_index = len(int_list)-1
#     unique_pairs_set= set()
#     for i in range(step_index):
#         num_1 = int_list[i]
#         num_2 = pair_sum - num_1
#         remaining_list = int_list[i+1:]
#         if num_2 in remaining_list:
#             pair = (num_1,num_2)
#             sorted_pair = tuple(sorted(pair))
#             unique_pairs_set.add(sorted_pair)
#     return unique_pairs_set

# str_num_list = input("enter: ")
# pair_sum = int(input("enter: "))
# int_list = list(map(int,str_num_list.split(",")))
# unique_pairs = get_unique_pairs(int_list,pair_sum)
# unique_pairs = list(unique_pairs)
# unique_pairs.sort() 
# for pair in unique_pairs:
#     print(pair)



num = int(input("enter: "))
fact = set()
for i in range(2,num+1):
    if i<0:
        print("No factors")
    elif num%i==0:
           fact.add(i)
print("factotrs of", num ,"is" ,fact)


# convert to binary
def convertBinary(num):
    binaryArray = []
    while num>0:
        binaryArray.append(num%2)
        num = num//2
    return binaryArray
decimal_num = 10
rev = convertBinary(decimal_num)
new = []
for i in rev:
    if i==0:
        new.append(1)
    else:
        new.append(0)
s = str(int("".join(map(str, new))))
print(rev)
print(new)
print(s)


