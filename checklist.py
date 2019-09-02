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
