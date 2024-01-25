# Complete the solve function below.
def solve(s):
    word = s.split(' ')
    c=(((i.capitalize() for i in word)))
    return ' '.join(c)
