# 12DTC: 2D Lists

## 🧠 Learning intentions

In this lesson, you will learn:

1. What a 2D list is
2. How to create a 2D list
3. How to access inner items in a 2D list
4. How to manage inner lists within an outer list

## 📖 Lesson

A powerful feature of lists in Python is that they can store anything, including other lists. This is called **2D lists**.

Normal lists are 1D, or one-dimensional, because the items can be represented in a single line.

| | Index 0 | Index 1 | Index 2 |
| --: | :-: | :-: | :-: |
| **List 1** | Hubert | Dewford | Llewellyn |

See how the items move only across from left to right?

2D lists can be represented across and up-down.

| | Index 0 | Index 1 | Index 2 |
| --: | :-: | :-: | :-: |
| **List 1** | Hubert | Dewford | Llewellyn |
| **List 2** | Webbigail | Lena | Violet |
| **List 3** | Scrooge | Donald | Della |

### Creating a 2D list

To put a list inside another list, simply write the lists like normal but with each list embedded in a list that wraps the rest.

```python
duck_groups = [["Hubert", "Dewford", "Llewellyn"], ["Webbigail", "Lena", "Violet"], ["Scrooge", "Donald", "Della"]]
```

See how each indivdual list is contained within another set of ``[`` and ``]``? This is a list of lists!

### Accessing a list

You access list within a 2D list the same as accessing items within a 1D list.

For example, to get the first list containing ``Hubert``, ``Dewford``, and ``Llewellyn``:

```python
print(duck_groups[0]) # ['Hubert', 'Dewford', 'Llewellyn']
```

To access the items *within* a 2D list, you first access the inner list, and then access the item as usual.

For example, to access ``Llewellyn`` from ``duck_groups``:

```python
# 0 for the first list
# 2 for the third item in the first list
print(duck_groups[0][2]) # Llewellyn
```

### List functions in 2D

All of the functions you learnt in [List Functions](lists-03-functions.md) work exactly the same, both for modifying lists within lists **and** for modifying items.

#### Appending and removing a list

```python
# Appending a list
duck_groups.append(["Magica", "Flintheart", "John"])

# Removing the list
duck_groups.pop(-1)
```

#### Appending and removing items in inner lists

```python
# Appending to the first inner list
duck_groups[0].append("Gene")

# Removing the item from the first inner list
duck_groups[0].pop(0)
```

#### Merging lists

```python
# Note that the added list is also a 2D list
duck_groups = duck_groups + [["Magica", "Flintheart", "John"]]
```

#### Merging items into inner lists

```python
# Add items to the last inner list
duck_groups = duck_groups[-1] + ["Ma Beagle", "Mark Beaks"]
```

## 📝 Instructions

Create a Python program in ``main.py`` and complete the tasks described in the comments. Write your code **below** the comments.

> Add your own comment above each function you create, describing what it does.

### Saving and committing

1. For each program, save the file (press Ctrl-S or ⌘S).
2. Click on the ▶️ Run Code button at the top-right to see if your code works. If not, fix the code and run it again.
3. When the code works, you will need to commit and push your code so that it is saved:
    - Click on the Source Control tab at the left
    - In the Message box, type a brief message that explains what you have done (e.g. "Finished the program")
    - Click on the Commit button
    - Click on the Sync button
4. When you have finished, let your kaiako know.