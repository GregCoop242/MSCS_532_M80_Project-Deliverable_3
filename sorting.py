def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].influence_score > right[j].influence_score:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(users):
    if len(users) <= 1:
        return users

    mid = len(users) // 2
    left = merge_sort(users[:mid])
    right = merge_sort(users[mid:])
    return merge(left, right)