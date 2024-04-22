'''def m_to_foot(length):
    return length *3.28

def foot_to_m(length):
    return length /3.28'''

def find_max(numbers):
    max = numbers[0]

    for i in numbers:
        if i > max:
            max = i
    return max