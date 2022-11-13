from pprint import pprint


def make_dict(n):
    dict_ = {'bin': bin(n), 'dec': n, 'oct': oct(n), 'hex': hex(n)}
    return dict_


amount_of_numb = 15
list_ = [make_dict(i) for i in range(amount_of_numb+1)]

pprint(list_)