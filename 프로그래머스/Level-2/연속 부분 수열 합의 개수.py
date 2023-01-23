def solution(elements):
    li = set()
    answer = 0
    
#     for le in range(2, len(elements)):
#         for index in range(len(elements)):
#             sum = 0
#             for start in range(le):
#                 id = index+start
#                 if (id >= len(elements)):
#                     id -= len(elements)
#                 sum += elements[id]
#             li.add(sum) 
#     sum=0
    
#     for i in range(len(elements)):
#         li.add(elements[i])
#         sum+=elements[i]
#     li.add(sum)
    
#     return len(li)


    elements+=elements
    
    for i in range(0, len(elements)//2):
        sum=0
        for k in range(0, len(elements)//2):
            sum += elements[i+k]
            li.add(sum)
    return len(li)
    
