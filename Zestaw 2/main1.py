def add_to_nested_list(nested_list):
    max_depth = [0]
    def helper(lst, depth=1):
        print("first")
        print()
        if isinstance(lst, dict):
            for key in lst:
                helper(lst[key], depth + 1)
        elif isinstance(lst, list):
            if depth > max_depth[0]:
                max_depth[0] = depth
            for i in lst:
                helper(i, depth + 1)
        elif isinstance (lst, tuple):
            for i in lst:
                helper(i, depth+1)
    helper(nested_list)
    def helper(lst, depth=1):
        print("second")
        if isinstance(lst, dict):
            for key in lst:
                helper(lst[key], depth + 1)
        elif isinstance(lst, list):
            if depth == max_depth[0]:
                lst.append(max(lst) + 1)
            for i in lst:
                helper(i, depth + 1)
        elif isinstance (lst, tuple):
            for i in lst:
                helper(i, depth+1)
    helper(nested_list)
    return nested_list

list1 = [1, 2, [3, 4, [5, {'klucz': [5, 6], 'tekst': [1, 2]}], 5], 'hello', 3, [4, 5], (5, (6, (1, [7, 8])))]
print(add_to_nested_list(list1))




