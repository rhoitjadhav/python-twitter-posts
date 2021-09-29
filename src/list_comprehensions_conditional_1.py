categories = {
    "clothing": 1,
    "beauty": 0,
    "watches": 1
}

filtered_categories = []

# Bad
for cat in categories:
    if categories[cat] != 1:
        filtered_categories.append(cat)

print(filtered_categories)


# Improved
filtered_categories = [cat for cat in categories if categories[cat] != 1]

print(filtered_categories)

'''
Output:
['beauty']
['beauty']
'''
