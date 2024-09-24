# DMOJ problem - ecoo18r1p2
# https://dmoj.ca/problem/ecoo18r1p2


def urban_modeling():
    routes_count = int(input())

    routes = []
    for i in range(routes_count):
        route = list(map(int, input().split()))
        routes.append(route)

    min_diameter = None
    problem_areas = []

    for route in routes:
        min_num = min(route[2:])

        if min_diameter is None:
            min_diameter = min_num

        if min_num == min_diameter:
            problem_areas.append(route[0])
        elif min_num < min_diameter:
            min_diameter = min_num
            problem_areas.clear()
            problem_areas.append(route[0])

    problem_areas.sort()
    print(f'{min_diameter} {{{','.join(map(str, problem_areas))}}}')


for _ in range(10):
    urban_modeling()