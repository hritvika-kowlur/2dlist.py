import random

marks = [random.randint(0, 100) for _ in range(20)]

low_marks = []   
mid_marks = []   
high_marks = []  

for m in marks:
    if m <= 30:
        low_marks.append(m)
    elif 31 <= m <= 69:
        mid_marks.append(m)
    else:
        high_marks.append(m)
       
print("Marks less then or equal to 30:", low_marks)
print("Marks between 31 and 69:", mid_marks)
print("Marks  more then or equal to 70 :", high_marks)