class Empty(Exception):
    pass

class MyStack:
    """
    An implementation of A stack Data Type

    :_data -> which is private and stores the elements
    :push() -> that adds an element to the end of a list
    :pop() -> returns the last element  added to the stack
    :is_empty() -> returns true if the stack is empty
    :len() -> returns the length of the stack
    :e -> is an element to be inserted or removed from the stack
    """
    def __init__(self):
        self._data = []
    
    def is_empty(self):
        return len(self._data) == 0
    
    def length(self):
        return len(self._data)
    
    def push(self, e):
        self._data.append(e)
    
    def pop(self):
        if self.is_empty():
            raise Empty('Empty Stack')
        return self._data.pop()

    def top(self, e):
        if self.is_empty():
            raise Empty('No Element in Stack')
        return self._data[-1]

    def __repr(self):
        return f"{self._data}"

if __name__ == "__main__":
    MyStack()


