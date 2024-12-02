from helpers import get_lists

def calculate_similarity_score(left_list, right_list) :
    similarity_score = 0
    
    for element in left_list :
        similarity_score += element * right_list.count(element)

    return similarity_score

left_list, right_list = get_lists("input.txt")
print(calculate_similarity_score(left_list,right_list))