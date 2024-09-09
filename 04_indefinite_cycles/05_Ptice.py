def solve_ptice(n, correct_answers):
    adrian_pattern = "ABC"
    bruno_pattern = "BABC"
    goran_pattern = "CCAABB"

    adrian_score = 0
    bruno_score = 0
    goran_score = 0

    for i in range(n):
        if correct_answers[i] == adrian_pattern[i % len(adrian_pattern)]:
            adrian_score += 1
        if correct_answers[i] == bruno_pattern[i % len(bruno_pattern)]:
            bruno_score += 1
        if correct_answers[i] == goran_pattern[i % len(goran_pattern)]:
            goran_score += 1

    max_score = max(adrian_score, bruno_score, goran_score)

    results = []
    if adrian_score == max_score:
        results.append("Adrian")
    if bruno_score == max_score:
        results.append("Bruno")
    if goran_score == max_score:
        results.append("Goran")

    print(max_score)
    for name in results:
        print(name)

n = int(input())
correct_answers = input()
solve_ptice(n, correct_answers)