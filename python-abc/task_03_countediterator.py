#!/usr/bin/python3
"""
python program
"""


class CountedIterator:
    """
    this is a class
    """
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        self.count += 1
        try:
            return next(self.iterator)
        except StopIteration:
            self.count -= 1
            raise

    def __iter__(self):
        return self


if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5]
    counted_iter = CountedIterator(my_list)

    print("Iterating through the list:")
    for item in counted_iter:
        print(f"Item: {item}, Count: {counted_iter.get_count()}")

    print("\nFinal count:", counted_iter.get_count())

    print("\nTesting with manual calls to __next__:")
    string_iter = CountedIterator("Hello")
    try:
        while True:
            char = next(string_iter)
            print(f"Character: {char}, Count: {string_iter.get_count()}")
    except StopIteration:
        print("Iteration complete")

    print("\nFinal count:", string_iter.get_count())
