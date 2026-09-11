# Problem 1: Preserve Order Unique Elements Without `set()`

## Problem Statement
Given a list of integers, write a function to return only the unique elements while preserving their original insertion order without using `set()`.

---

## Solution

```python
def making_unique_list(numbers: list[int]) -> list[int]:
    """
    Returns unique elements from a list while preserving original insertion order
    without utilizing set().
    """
    return list(dict.fromkeys(numbers))


if __name__ == "__main__":
    not_unique_list = [int(i) for i in input("enter numbers with space : ").split()]
    unique_list_of_numbers = making_unique_list(not_unique_list)
    print(unique_list_of_numbers)
```
