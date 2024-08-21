# DMOJ problem - ccc15j2
# https://dmoj.ca/problem/ccc15j2

line = input()

if line.count(':-)') > 0 and line.count(':-(') and line.count(':-)') == line.count(':-('):
    print('unsure')
elif line.count(':-)') > line.count(':-('):
    print('happy')
elif line.count(':-)') < line.count(':-('):
    print('sad')
else:
    print('none')