import random

def throw_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(iterations):
    sums_count = {i: 0 for i in range(2, 13)}
    for _ in range(iterations):
        dice1 = throw_dice()
        dice2 = throw_dice()
        total = dice1 + dice2
        sums_count[total] += 1
    
    probabilities = {k: v / iterations * 100 for k, v in sums_count.items()}
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for total, probability in probabilities.items():
        print(f"{total}\t{probability:.2f}% ({probability/100:.2f})")

def analytical_probabilities():
    analytical = {
        2: 1/36 * 100,
        3: 2/36 * 100,
        4: 3/36 * 100,
        5: 4/36 * 100,
        6: 5/36 * 100,
        7: 6/36 * 100,
        8: 5/36 * 100,
        9: 4/36 * 100,
        10: 3/36 * 100,
        11: 2/36 * 100,
        12: 1/36 * 100
    }
    return analytical

# Задана кількість ітерацій для симуляції
iterations = 1000000

# Запуск симуляції та виведення результатів
print("Метод Монте-Карло:")
monte_carlo_probabilities = monte_carlo_simulation(iterations)
print_probabilities(monte_carlo_probabilities)

print("\nАналітичні результати:")
analytical = analytical_probabilities()
print_probabilities(analytical)
