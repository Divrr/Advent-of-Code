def build_frequency_dict(list):
    result = {}

    for item in list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
        
    return result

def similarity_score(left, right):
    freq_right = build_frequency_dict(right)

    total_similarity = 0

    for number in left:
        freq_r = 0
        if number in freq_right:
            freq_r = freq_right[number]
        
        total_similarity += number * freq_r
    
    return total_similarity

f = open("2024/1in.txt", "r")
left, right = [], []

for line in f.readlines():
    l, r = [int(n) for n in line.split()]
    left.append(l)
    right.append(r)

print(similarity_score(left, right))