# def hp(amount, heap=dict()):
#     if not heap:
#         heap[amount] = []
#     else:
#         if
#         heap[max(heap)].append(amount)
#         heap[amount] = []
#     print(heap)


# hp(10)
# hp(15)
# hp(20)
# hp(30)

# h = {}
# p = dict()
#
# print(h == p)
# print(h)
# print(p)
# if not h:
#     print(True)
# if not p:
#     print(True)

number_of_requests = int(input())
heap = []
graph = dict()
parent = []
counter = 0


def hp(request):
    req = request.split()
    global counter
    if req[0] == 'Insert':  # Если запрос Insert
        heap.append(int(req[1]))  # Добавляем значение Insert в конец списка heap
        n = counter  # максимальный индекс heap (кучи)
        # if n % 2 == 0:  # если n четное или равно 0
        #     parent = n // 2 - 1  # порядковый номер родителя в heap
        # else:
        #     parent = n // 2  # иначе: порядковый номер родителя в heap
        parent = (n - 1) // 2
        while heap[n] > heap[parent]:  # пока значение элемента меньше, чем значение родителя
            heap[parent], heap[n] = heap[n], heap[parent]  # меняем местами родителя и элемент
            n = parent
            # if n % 2 == 0 and n // 2 - 1 >= 0:
            #     parent = n // 2 - 1
            # else:
            #     parent = n // 2
            if n - 1 // 2 >= 0:
                parent = (n - 1) // 2

        # print(heap, counter)
        counter += 1
        print(heap)
    else:
        n = heap.index(max(heap))  # a_list.remove('new')
        counter -= 1
        return print(heap.pop(n))


for element in range(number_of_requests):
    request = input()
    hp(request)
