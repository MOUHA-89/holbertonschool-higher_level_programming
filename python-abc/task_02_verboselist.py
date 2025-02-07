#!/usr/bin/python3
"""
python code
"""


class VerboseList(list):
    """
    class
    """
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        original_length = len(self)
        super().extend(iterable)
        items_added = len(self) - original_length
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        if self:
            item = self[index]
            print(f"Popped [{item}] from the list.")
            return super().pop(index)
        else:
            print("Cannot pop from an empty list.")
            raise IndexError("pop from empty list")


if __name__ == "__main__":

    vl = VerboseList()

    vl.append(4)

    vl.extend([5, 6])

    vl.remove(2)

    vl.append(2)
    vl.remove(2)

    vl.pop()
    vl.pop(0)
