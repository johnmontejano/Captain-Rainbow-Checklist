checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)


def create(item):
    checklist.append(item)


def read(index):
    return checklist[index]


def update(index, item):
    checklist[index] = item


def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(yellow(index) + blue(list_item)))
        index += 1


def test():
    create("purple sox")

    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)
    list_all_items()
    print(read(0))
    print(read(1))


def mark_completed(index):
    checklist[index] = green('√') + checklist[index]


test()
