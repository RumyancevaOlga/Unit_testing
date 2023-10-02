def find_average(lst: list[int]) -> float:
    if not isinstance(lst, list):
        raise TypeError('Argument must be a list type')
    for item in lst:
        if not isinstance(item, (int, float)):
            raise ValueError(f'Element {item} not int or float')
    if len(lst):
        return sum(lst) / len(lst)
    return 0.0
