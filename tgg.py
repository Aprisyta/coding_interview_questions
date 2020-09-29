''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    row, col = map(int, input().split())
    [[0,0],[0, 0]]
    arr = [[0] * col] * row
    for i in range(row):
        arr[i] = list(map(int, input().split()))
    visited = set()
    belt = 0
    for i in range(row - 1,2):
        for j in range(col - 1,2):
            if (i, j) in visited:
                continue
            visited.add((i, j))
            localBelt = belt + arr[i][j]
            if i + 1 < row:
                if (i + 1, j) not in visited:
                    visited.add((i + 1, j))
                    localBelt = max(localBelt, localBelt + arr[i + 1][j])
                if j - 1 > -1 and (i + 1, j - 1) not in visited:
                    visited.add((i + 1, j - 1))
                    localBelt = max(localBelt, localBelt + arr[i + 1][j - 1])
                if j + 1 < col and (i + 1, j + 1) not in visited:
                    visited.add((i + 1, j + 1))
                    localBelt = max(localBelt, localBelt + arr[i + 1][j + 1])
            if j + 1 < col:
                if (i, j + 1) not in visited:
                    visited.add((i, j + 1))
                    localBelt = max(localBelt, localBelt + arr[i][j + 1])
                if i - 1 > -1 and (i - 1, j + 1) not in visited:
                    visited.add((i - 1, j + 1))
                    localBelt = max(localBelt, localBelt + arr[i - 1][j + 1])
            # if localBelt == belt
            belt = max(localBelt, belt)
    print(belt)

 # Write code here 

main()

# 1 1 1 0 1
# 0 1 0 1 0
# 0 0 0 0 0
# 1 0 1 1 1

