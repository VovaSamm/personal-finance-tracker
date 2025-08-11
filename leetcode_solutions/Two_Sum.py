# def valid_of_list_number(list_number:list):
#     while True:
#         for i in list_number:
#             try:
#                 float(i)
#             except Exception:
#                 i=float(input('enter corect information'))
#

# def valid_of_sum_number(number:float):
#     while True:
#             try:
#                 float(number)
#             except Exception:
#                 i = float(input('enter corect information'))

def two_sum(list_of_number: list,sum_two:(int,float),):
    #list_of_number=valid_of_list_number(list_of_number)
    #sum_two=valid_of_sum_number(sum_two)

    for i in range(len(list_of_number)):
        for j in range(len(list_of_number)):
            if i!=j and  list_of_number[i]+ list_of_number[j]==sum_two:
                return list_of_number[i], list_of_number[j]

    return 'Not sum'

print(two_sum([1,2,3,4,5,6,7,8],15))