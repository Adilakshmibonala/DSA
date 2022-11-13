def find(N, K, A):
    """
    Time complexity is not good for this. O(n^2)
    """
    out_start, out_end = 0, 0
    window_size = 0
    for i in range(N):
        if window_size > N // 2:
            break
        flips = K
        end = i
        for index in range(i, N):
            if A[index] == 1:
                end += 1
            elif flips:
                flips -= 1
                end += 1
            else:
                break
        if (end - i) > window_size:
            window_size = end - i
            out_start = i
            out_end = end

    print(out_start, out_end - 1)


if __name__ == "__main__":
    number_and_k = input().split(" ")
    N = int(number_and_k[0])
    K = int(number_and_k[1])
    A = list(map(int, input().split(" ")))
    find(N, K, A)


