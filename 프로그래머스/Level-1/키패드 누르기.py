def solution(numbers, hand):
    answer = ''
    phoneL = [[1,2,3], [4,5,6], [7,8,9], ["*",0,"#"]]
    left = [3,0]
    right = [3,2]
    
    for i in numbers:
        if i in [1,4,7]:
            left = [i//3, 0]
            answer+='L'
        elif i in [3,6,9]:
            right = [(i//3)-1, 2]
            answer+='R'
        else:
            if i==0:
                m = [3,1]
            else:
                m = [i//3,1]
            if (abs(left[0]-m[0])+abs(left[1]-m[1])) < (abs(right[0]-m[0])+abs(right[1]-m[1])):
                left = m
                answer+='L'
            elif (abs(left[0]-m[0])+abs(left[1]-m[1])) > (abs(right[0]-m[0])+abs(right[1]-m[1])):
                right = m
                answer+='R'
            else:
                if hand=="left":
                    left = m
                    answer+='L'
                else:
                    right = m
                    answer+='R'
    return answer