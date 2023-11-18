def tpl_sort(tpl):
    for i in tpl:
        if i * 10 % 10 > 0.0:
            return tpl

    tpl = sorted(tpl)
    return tpl
