def greedy_algorithm(items, budget):
    # Створюємо список кортежів (назва_страви, співвідношення_калорій_до_вартості)
    item_ratios = [(item, items[item]["calories"] / items[item]["cost"]) for item in items]
    # Сортуємо список за спаданням співвідношення
    item_ratios.sort(key=lambda x: x[1], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, ratio in item_ratios:
        if total_cost + items[item]["cost"] <= budget:
            selected_items.append(item)
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]
    
    return selected_items, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    # Створюємо матрицю для збереження результатів підзадач
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            # Якщо вартість страви менше або дорівнює бюджету
            if items[i - 1]["cost"] <= j:
                # Порівнюємо вибір між включенням і виключенням страви
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1]["cost"]] + items[i - 1]["calories"])
            else:
                # Якщо вартість страви перевищує бюджет, просто копіюємо результат з попередньої підзадачі
                dp[i][j] = dp[i - 1][j]

    # Відновлюємо оптимальний набір страв
    selected_items = []
    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items[i - 1])
            j -= items[i - 1]["cost"]
        i -= 1

    return selected_items, dp[n][budget]


# Задані дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Викликаємо функції для обох алгоритмів
greedy_items, greedy_calories = greedy_algorithm(items, budget)
# Виклик функції dynamic_programming
dp_items, dp_calories = dynamic_programming(list(items.values()), budget)


print("Greedy Algorithm:")
print("Selected Items:", greedy_items)
print("Total Calories:", greedy_calories)

print("\nDynamic Programming:")
print("Selected Items:", dp_items)
print("Total Calories:", dp_calories)
