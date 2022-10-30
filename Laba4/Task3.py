def delete(list_, index=None):
    if index is None:
        list_ = list_[:-1]
        return list_
    list1 = list_[:index]
    list2 = list_[index+1:]
    list_ = list1 + list2
    return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
