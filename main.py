def parallel_processing(n, m, data):
    out = []
    timeCurrent = [0] * n

    for i in range(m):
        jobT = data[i]
        IDthread = min(range(n), key=lambda i: timeCurrent[i])
        out.append((IDthread, timeCurrent[IDthread]))
        timeCurrent[IDthread] += jobT

    return out


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for IDthread, start_time in result:
        print(IDthread, start_time)


if __name__ == "__main__":
    main()
