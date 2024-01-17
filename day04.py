###################################### 7.1 튜플 #####################################
# empty_tuple = ()
# print(empty_tuple)
#
# one_marx = ('Groucho') # 예상과 달리 one_marx => 문자열 출력
# print(one_marx)
# print(type(one_marx)) # class <str>
#
# marx_tuple = ('a', 'b', 'c')
# print(marx_tuple)
#
# one_marx = 'Groucho',
# print(type(one_marx))
# print(type(('Groucho',)))
#
# # tuple unpacking
# max_tuple = ('Groucho','Chico','Harpo')
# a,b,c = max_tuple
#
# 값 교환
# password = 'swordfish'
# icecream = 'tuttifutti'
# print(id(password))
# print(id(icecream))
# password, icecream = icecream, password # password 가 가리키는 주소가 icecream 주소로 바뀜 // 반대도 마찬가지
# print(id(password))
# print(id(icecream))
# print(password)
# print(icecream)

# tuple(list) : []가 ()로 바뀐다
# tuple + tuple 가능하다 (이어붙이기)
# # *연산자를 이용하자
# tup = ('a','b','c')
# print(tup * 3)

# words = ('fresh','out','of','ideas')
# for word in words :
#     print(word)
#
# # += 는 해당 변수에 새로운 번지수를 할당한다
# t1 = ('Fee','Fie','Foe')
# t2 = ('Floop',)
# print(id(t1))
# t1 += t2
# print(id(t1))
#
# a = 2
# print(id(a))
# a += 2
# print(id(a))

###################################### 7.2 리스트 #####################################
# empty_list = []
# weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
# big_birds = ['emu','ostrich','cassowary']
# leap_years = [2000,2004,2008]
# randomness = ['Punxsatawney',{'groundhog':'Phil'},'Feb.2']
# first = [1,1,2]
# print(first)
# print(empty_list)
#
# print(list('cat'))
# print(list(('a','b','c')))
#
# one = '9/19/2019'
# print(one.split('/'))
# print(one)
#
# splitme = 'a/b//c/d///e'
# print(splitme.split('//'))
#
# marxes = ['Groucho','Chio','Harpo']
# print(marxes[0:1])
#
# # print(marxes[::-1])
# ## .reverse()는 리스트 자체를 바꿔버린다
# # marxes.reverse()
# # print(marxes)
# # print(marxes.reverse())
#
# marxes.append("hello")
# print(marxes)
#
# marxes.insert(1, "GrChio")
# print(marxes)
#
# others = ['a', 'b']
# marxes.extend(others)
# print(marxes)

# numbers = [1,2,3,4]
# numbers[1:3] = [8,9]
# print(numbers)
# numbers[1:3] = []
# print(numbers)
#
# numbers = [1,2,3,4]
# numbers[1:3] = 'wat'
# print(numbers)
#
# numbers[3:5] = []
# print(numbers)
#
# marxes = ['Groucho','Chio','Harpo']
# print(marxes.pop())
# print(marxes)
# marxes = []
# print(marxes)

