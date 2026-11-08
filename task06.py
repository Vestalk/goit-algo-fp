items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(),
                          key=lambda kv: kv[1]["calories"] / kv[1]["cost"],
                          reverse=True)
    chosen, total_cost, total_calories = [], 0, 0
    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            chosen.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]
    return chosen, total_cost, total_calories


def dynamic_programming(items, budget):
    names = list(items)
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        cal = items[names[i - 1]]["calories"]
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if cost <= b and dp[i - 1][b - cost] + cal > dp[i][b]:
                dp[i][b] = dp[i - 1][b - cost] + cal

    chosen, b = [], budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = names[i - 1]
            chosen.append(name)
            b -= items[name]["cost"]
    chosen.reverse()
    total_cost = sum(items[name]["cost"] for name in chosen)
    return chosen, total_cost, dp[n][budget]


if __name__ == "__main__":
    for budget in (50, 100, 120):
        g = greedy_algorithm(items, budget)
        d = dynamic_programming(items, budget)
        print(f"Бюджет: {budget}")
        print(f"  Жадібний:   {g[0]}  вартість={g[1]}, калорії={g[2]}")
        print(f"  Динамічний: {d[0]}  вартість={d[1]}, калорії={d[2]}")
        print()
