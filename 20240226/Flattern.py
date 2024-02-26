for tc in range(10):
    dump = int(input())
    arr = list(map(int, input().split()))

    for _ in range(dump):
        max_box, min_box = 0, 101
        max_index, min_index = 0, 0

        for i in range(len(arr)):
            if min_box > arr[i]:
                min_box = arr[i]
                min_index = i

            if max_box < arr[i]:
                max_box = arr[i]
                max_index = i
        arr[max_index] -= 1
        arr[min_index] += 1

    max_h = 0
    min_h = 101

    for box in arr:
        if max_h < box:
            max_h = box

        if min_h > box:
            min_h = box

    print(max_h - min_h)