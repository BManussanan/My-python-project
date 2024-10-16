def namelist(names):
    if not names:
        return ''

    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return ' & '.join(names)
    else :
        return ', '.join(names[:-1]) + f' & {names[-1]}'
print( namelist(['Bart', 'Viola', 'Peter', 'Nostel']) )
print( namelist(['Bart', 'Viola']) )
print( namelist(['Peter']) )
print( namelist([]) == '' )