# TODAY I LEARNED

## Use map() to type cast
He uses map() as a way to cast a lists of values into different types.  I don't know why I never thought to do this, its very clever.  I've only ever passed custom functions into map, I never thought to use common ones like int() or str() to cast a list of values into a different type.  I would always setup an accumulator, iterate and cast each item.  His method is much easier. 

<br>

## Destructering 
He uses a lot of destructering, example:
```py
list1, list2 = list(map(list, zip(*lines)))
```
When you know the result of an expression will be a list, destructering it right in the return like this saves time.

<br>

## For loops have an else clause
The else clause in a Python for loop is executed only when the loop completes all its iterations without encountering a break statement.
 This means the else block runs after the loop has naturally exhausted the iterable, providing a way to execute code specifically when no break was triggered during the loop's execution.
 It is particularly useful for scenarios like searching for an item in a collection, where the else block can handle the "not found" case after the loop finishes without breaking.
 The else clause is not executed if the loop is exited early by a break, return, or an exception.

```py
  for i, char in enumerate("MAS", 1):
            if (r + (dr * i), c + (dc * i)) not in char_map[char]:
                break
        else:
            part1 += 1
```

<br>

## Zip() function to stitch two lists together
The zip() function in Python is a built-in utility that aggregates elements from multiple iterables—such as lists, tuples, strings, or dictionaries—into an iterator of tuples, where each tuple contains elements from the input iterables at the same index.
 It is commonly used for parallel iteration, creating dictionaries from paired lists, and combining data from multiple sources in a structured way.
 The function stops when the shortest input iterable is exhausted, meaning any excess elements in longer iterables are ignored.
 It returns a lazy iterator, so the tuples are generated on-demand during iteration, which is memory efficient for large datasets.

The syntax is zip(*iterables, strict=False), where *iterables can be any number of iterable objects, and strict=True (available in Python 3.10+) will raise a ValueError if the input iterables have unequal lengths.
When used with two lists, zip() pairs corresponding elements: list(zip([1, 2], ['a', 'b'])) returns [(1, 'a'), (2, 'b')].
The function works with various iterables, including strings (pairing characters by position) and tuples.
To convert the iterator to a list or use it in a loop, wrap it with list() or use it directly in a for loop.
An advanced use case is "unzipping" data by using the unpacking operator *, such as numbers, letters = zip(*[(1, 'a'), (2, 'b')]).
A common pitfall is that the iterator can only be consumed once; attempting to iterate over it again will yield no results.


<br>

## List comprehensions
I need to get better at these, wow are they powerful. Less 'for loops', more comprehensions.
```py
diffs = [abs(x1 - x2) for x1, x2 in zip(nums, nums[1:])]
len([r for r in lines if check_report(r)])
part2 = len([r for r in lines if check_report(r, part1=False)])
squares = [x**2 for x in range(10)]   
```
Note the last one iterating over range(10). I've had problems iterating things like a list or object and the answer was to get the range(val) and iterate that.

<br>

## Range() function instead of for loops
The Python range() function generates an immutable sequence of integers starting from a specified start value, up to (but not including) a specified stop value, with an optional step increment.
 It is commonly used in for loops to iterate a specific number of times or to access elements in sequences like lists or strings by index.
 The function accepts up to three arguments: start, stop, and step, where start defaults to 0 and step defaults to 1 if not provided.
 For example, range(5) produces numbers from 0 to 4, while range(2, 10, 2) generates 2, 4, 6, and 8.
 The function returns a range object, which is memory-efficient as it generates values on-demand during iteration rather than storing the entire sequence in memory.

## defaultdict
The defaultdict in Python is a subclass of the built-in dict class from the collections module, designed to automatically provide a default value for missing keys, thereby preventing KeyError exceptions.
 When a key is accessed that does not exist in the defaultdict, it calls a specified default_factory function (a callable) to generate a default value, which is then assigned to the key.
 This default_factory is passed as the first argument during initialization and can be any callable, such as int, list, set, or a custom function.
 For example, using defaultdict(int) initializes missing keys with a value of 0, making it ideal for counting occurrences
 , while defaultdict(list) initializes missing keys with an empty list, which is useful for grouping items.
 The defaultdict simplifies code by eliminating the need for repetitive checks like if key not in dict, and it is particularly effective for tasks such as histogram creation, graph building, and data aggregation.

<br>

 ## Using the colon to slice lists
 In Python, the colon (:) is used in indexing to perform slicing, which allows you to extract a subset of elements from a list or array. When used alone, : means "all elements" in that dimension.
 For example, list[:] returns a copy of the entire list.

The colon can be used in various combinations to specify ranges:

list[start:] returns all elements from index start to the end of the list.
list[:stop] returns all elements from the beginning of the list up to (but not including) index stop.
list[start:stop] returns elements from index start to stop - 1.
list[start:stop:step] includes a step parameter, allowing you to skip elements; for instance, list[::2] returns every second element starting from the beginning.

When multiple colons are used, such as in list[::2], the first colon represents the start (defaulting to 0 if omitted), the second represents the stop (defaulting to the end if omitted), and the third represents the step size.
 This is equivalent to list[None:None:2] internally.

In multi-dimensional structures like NumPy arrays, the colon is used to select all elements along a specific axis, and commas separate the indices for different dimensions.
 For example, array[:, 1] selects all rows (:) and the element at index 1 in the second dimension (columns).
 This slicing behavior extends to strings and other sequences as well.

The colon is also used in other contexts, such as defining code blocks (e.g., in if, for, or def statements), where it indicates the start of an indented block.

## Get the element at the center of a list
By dividing the length in half.  Simple, brilliant.
```py
return job[len(job) // 2]
```

<br>

## Sort lists using cmp_to_key
The functools.cmp_to_key function in Python converts an old-style comparison function into a key function that can be used with sorting and ordering functions like sorted(), min(), and max().
 A comparison function takes two arguments and returns a negative value if the first is considered smaller, a positive value if it is larger, and zero if they are equal.
 This function is particularly useful for migrating code from Python 2, which supported comparison functions, to Python 3, where only key functions are used for sorting.

Internally, cmp_to_key creates a new callable class, K, which wraps each object and implements comparison methods (__lt__, __gt__, __eq__, etc.) that use the original comparison function to determine the order.
 When sorting, the built-in sorting algorithms compare these wrapped objects, and the comparison methods invoke the original function to decide the relative order.
 For example, when K(a).__lt__(K(b)) is called, it evaluates mycmp(a, b) < 0 to determine if a should come before b.

This mechanism allows developers to reuse existing comparison logic without rewriting it as a key function, making it convenient when working with complex sorting criteria.
 The resulting key function is a callable object that can be passed directly to sorting functions, enabling custom sorting based on the provided comparison logic.
