if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # get the marks of the queried student
    marks = student_marks[query_name]
    # calculate the average
    average = sum(marks)/len(marks)

    #print with 2 decimal places
    print(f"{average:.2f}")
















