def slicer(tpl, el):
    if el in tpl:
        if tpl.count(el) > 1:
            first = tpl.index(el)
            second = tpl.index(el, first + 1)
            return tpl[first: second]
        else:
            return tpl[tpl.index(el): ]
    else:
        return ()


print(slicer((1, 2, 3), 8))
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
