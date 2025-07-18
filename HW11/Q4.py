def segment_tree(a, tree, node, source, target, mid):
    if source == target:
        tree[node] = a[source]
        return
    
    right_child = 2 * node + 1

    left_child = 2 * node

    avg = (source + target) // 2
    
    segment_tree(a, tree, left_child, source, avg, avg)

    segment_tree(a, tree, right_child, avg + 1, target, avg)

    tree[node] = min(tree[left_child], tree[right_child])


def update(tree, node, source, target, i, v):
    if source == target:
        tree[node] = v
        return

    mid = (source + target) // 2
    left_child = 2 * node
    right_child = 2 * node + 1

    if i <= mid:
        update(tree, left_child, source, mid, i, v)
    else:
        update(tree, right_child, mid + 1, target, i, v)

    tree[node] = min(tree[left_child], tree[right_child])


def query(tree, node, source, target, left, right):
    if left > target or right < source:
        return float('inf')
    if left <= source and right >= target:
        return tree[node]

    mid = (source + target) // 2
    left_node = 2 * node
    right_node = 2 * node + 1

    min1 = query(tree, left_node, source, mid, left, right)
    min2 = query(tree, right_node, mid + 1, target, left, right)

    return min(min1, min2)
def op2(tree, node, source, target, i, value):
    update(tree, node, source, target, i, value)

n, m = map(int, input().split())

a = list(map(int, input().split()))

tree = [0] * (4 * n)
segment_tree(a, tree, 1, 0, n - 1, 0)

for _ in range(m):
    q, x, y = map(int, input().split())

    if q == 1:
        x = x - 1
        y = y - 1
        if x > y or y < 0:
            print(float('inf'))
        elif x <= 0 and y >= n - 1:
            print(tree[1])
        else:
            mid = (0 + (n - 1)) // 2
            left_node = 2 * (1)
            right_node = 2 * (1) + 1

            min1 = query(tree, left_node, 0, mid, x, y)
            min2 = query(tree, right_node, mid + 1, n - 1, x, y)

            print(min(min1, min2))
    elif q == 2:
        a[x - 1] = y
        op2(tree, 1, 0, n - 1, x - 1, y)

