class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Додати вузол в кінець списку
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    # Розділити список на дві половини
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    # Рекурсивно сортуємо дві половини
    left_half = merge_sort_linked_list(head)
    right_half = merge_sort_linked_list(next_to_middle)

    # Злиття двох відсортованих списків
    sorted_list = merge(left_half, right_half)
    return sorted_list

# Допоміжні функції
def get_middle(head):
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left.data < right.data:
        left.next = merge(left.next, right)
        return left
    else:
        right.next = merge(left, right.next)
        return right

def merge_linked_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.data < list2.data:
        list1.next = merge_linked_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_linked_lists(list1, list2.next)
        return list2

# Створення однозв'язного списку для тестування
def create_linked_list(values):
    linked_list = LinkedList()
    for value in values:
        linked_list.append(value)
    return linked_list

# Перевірка функції реверсування списку
def test_reverse_linked_list():
    values = [1, 2, 3, 4, 5]
    linked_list = create_linked_list(values)
    reversed_list_head = reverse_linked_list(linked_list.head)
    reversed_values = []
    while reversed_list_head:
        reversed_values.append(reversed_list_head.data)
        reversed_list_head = reversed_list_head.next
    assert reversed_values == list(reversed(values)), "Функція реверсування не працює правильно"

# Перевірка функції сортування списку
def test_merge_sort_linked_list():
    values = [5, 3, 1, 4, 2]
    linked_list = create_linked_list(values)
    sorted_list_head = merge_sort_linked_list(linked_list.head)
    sorted_values = []
    while sorted_list_head:
        sorted_values.append(sorted_list_head.data)
        sorted_list_head = sorted_list_head.next
    assert sorted_values == sorted(values), "Функція сортування не працює правильно"

# Перевірка функції об'єднання двох списків
def test_merge_linked_lists():
    list1_values = [1, 3, 5]
    list2_values = [2, 4, 6]
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    merged_list_head = merge_linked_lists(list1.head, list2.head)
    merged_values = []
    while merged_list_head:
        merged_values.append(merged_list_head.data)
        merged_list_head = merged_list_head.next
    assert merged_values == sorted(list1_values + list2_values), "Функція об'єднання списків не працює правильно"

# Запуск тестів
test_reverse_linked_list()
test_merge_sort_linked_list()
test_merge_linked_lists()
print("Всі тести пройдені успішно.")
