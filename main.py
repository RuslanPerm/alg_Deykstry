from collections import defaultdict

# Задаем входные значения
input_list = [[1, 2, 1], [1, 7, 9], [2, 3, 2], [3, 4, 1], [4, 7, 2], [4, 5, 2],
              [5, 6, 3], [6, 7, 1], [7, 9, 6], [7, 9, 1], [7, 8, 2], [8, 9, 2]]
number_of_elements = 9
source = 1
target = 9

# Инициализируем граф
graph = defaultdict(list)
# Заполняем граф: вершина -> (стоимость, вершина куда можем прийти)
for a, b, cost in input_list:
    graph[a] += [(cost, b)]

# Инициализируем список вершин для посещения
nodes_to_visit = []
# Добавляем нашу исходную с расстоянием равным нулю
nodes_to_visit.append((0, source))
# Инициализируем список уникальных значений для хранения вершин которые уже посетили
visited = []
# Заполняем расстояния до всех остальных вершие
min_dist = {i: float('inf') for i in range(1, number_of_elements + 1)}
# Заполняем расстояние до текущей вершины
min_dist[source] = 0
# Проходимся по всем вершинам которые нужно посетить
# Проходимся до тех пор, пока такие вершины есть
while len(nodes_to_visit):
    # Берем самую близкую вершину к нам
    # cost - стоимость попадания, node - название вершины
    cost, node = min(nodes_to_visit)
    # Удаляем эту вершину из списка вершин для посещения
    nodes_to_visit.remove((cost, node))
    # Проверяем что мы в нее еще не заходили (если вдруг мы сначала добавили (9,7), а потом (6,7)
    if node in visited:
        continue
    # Добавляем в список посещенных
    visited.append(node)
    # Проходимся по всем соединенным вершинам
    # n_cost - стоимость попадания из текущей вершины, n_node - прикрепленная вершина, в которую хотим попасть
    for n_cost, n_node in graph[node]:
        # Проверяем нашли ли мы оптимальный путь
        if cost + n_cost < min_dist[n_node] and n_node not in visited:
            # Если нашли то обновляем значение расстояния
            min_dist[n_node] = cost + n_cost
            # И добавляем эту вершину в список вершин для посещения
            nodes_to_visit.append((cost + n_cost, n_node))

# Выводим ответ
print("Вес суммарного пути: ", min_dist[target])
print("Вершины были посещены в следующем порядке: ", *visited)