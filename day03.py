# numbers = input("Firstnumber SecondNumber : ").split()
# print(numbers[0] + numbers[1])
# print(int(numbers[0])+int(numbers[1]))

# course = "2024 KEB bootcamp"
# print(course)
# list_course = course.split()
# print(list_course)

# split = 문자열을 구분자로 분해해서 list에 담음
# .split('구분자')
# return type = list

# join = list 원소를 합쳐서 문자열 생성
# 'list 원소사이에 집어넣을 구분자'.join(list)
# 문자열을 return

# replace = 문자열 수정(대체)
# course = "2024 KEB boot KEB camp"
# print(course.replace('KEB','Inha',2)) #course 변수 수정x, 따로 메모리값 담김
# print(course)

# strip = 문자열 중에 내가원하는 문자를 빼줌(양쪽끝만 지워준다)
# course = "**   2024 KEB# boot KEB camp KEB...*!#"
# print(course)
# print(course.strip())
# print(course.strip("!#.*"))

# course = "**   2024 KEB# boot KEB camp KEB...*!#"
# print(course.find('KEB'))
# print(course.rfind('KEB')) # 뒤에서 찾아라
# print(course.index('KEB')) # .index = .find, rindex 도 동일기능
# print(course.find('KEC')) # -1 return (can't find) /// index는 오류 발생

# subjects = "python c++ database linux"
# print(subjects.isalnum())
# subject = input("수강신청과목 입력 : ")
# try:
#     print(f"해당 과목이 존재합니다. 위치는 {subjects.index(subject)}번 인덱스입니다.")
# except ValueError:
#     print('해당 과목 존재 x')

# print('%e' %0.703)
# print('%d%%'%100)
# print("Our %s Chester weighs %d pounds"%('cat',28))

# subjects = {'python': 'Kim', 'c++': 'sung', 'datastructure': 'Kim', 'database': 'kang'}
# print("{0[python]} {0[datastructure]}".format(subjects))

# prime number
number = int(input("Input number : "))
is_prime = True # int -> bool
i = 2
while i < number:
    if number % i == 0:
        is_prime = False # remove +
        break
    i += 1

#if cnt == 0 :
if is_prime: # remove ==
    print(f'{number} is prime number')
else :
    print(f'{number} is NOT prime number')
