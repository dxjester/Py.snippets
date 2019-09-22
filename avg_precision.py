# 1.0.6
def report_exam_avg(a, b, c):
    test_count = 3
    raw_score = a + b + c
    average = raw_score / test_count
    average = '%.1f'%average  # set the precision
    return ("Your average score: " + average)
