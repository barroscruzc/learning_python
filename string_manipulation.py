#  Hackerrank - Problem solving (beginner)
#  Task:
#  The included code stub will read an integer, n, from STDIN.
#  Without using any string methods, try to print the following:
#  123...n


if __name__ == '__main__':
    n = int(input())
    result = []
    vetor_string = ''
    for i in range(0, n+1, 1):
        result.append(i)
    for i in result:
        vetor_string = vetor_string + str(result[i])
    print(vetor_string[1:])