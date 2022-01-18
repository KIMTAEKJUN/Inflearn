grade = [88, 30, 61, 55, 95]
for i in range(0, 5): 
    if grade[i] >= 60:
        print("%d번 학생은 %s점으로 합격입니다." % (i+1,grade[i]))
    else:
        print("%d번 학생은 %s점으로 불합격입니다." % (i+1,grade[i]))