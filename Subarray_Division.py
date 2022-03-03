def birthday(s, d, m):
    # Write your code here
    total_sum = 0
    results = 0
    
    for index in range(len(s) - m +1):
        current_sum = 0
        for index_j in range(m):
            current_sum += s[index + index_j]
        if current_sum == d:
            results +=1
                   
    return results
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
