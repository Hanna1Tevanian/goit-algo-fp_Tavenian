import heapq

def dijkstra(graph, start):
    # Ініціалізуємо відстані до всіх вершин як нескінченні
    distances = {vertex: float('infinity') for vertex in graph}
    # Відстань до початкової вершини рівна 0
    distances[start] = 0
    
    # Бінарна купа для оптимізації вибору вершин
    pq = [(0, start)]
    
    while pq:
        # Вибираємо вершину з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Якщо поточна відстань більша, ніж вже знайдена, пропускаємо
        if current_distance > distances[current_vertex]:
            continue
        
        # Оновлюємо відстані до сусідніх вершин через поточну вершину
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Якщо знайдено коротший шлях, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Приклад графа
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print("Найкоротші відстані від вершини", start_vertex + ":")
for vertex, distance in shortest_distances.items():
    print("До вершини", vertex, ":", distance)
