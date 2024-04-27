def prefix_function(a):
    n = len(a)
    prefix = [0] * n
    for i in range(1, n):
        j = prefix[i - 1]
        while j > 0 and a[i] != a[j]:
            j = prefix[j - 1]
        j += (a[i] == a[j])
        prefix[i] = j
    return prefix

def occurrences_of_each_prefix(prefix, n):
    ret = [0] * (n + 1)
    for i in range(n):
        ret[prefix[i]] += 1
    for i in range(n - 1, 0, -1):
        ret[prefix[i - 1]] += ret[i]
    for i in range(n + 1):
        ret[i] += 1
    return ret
