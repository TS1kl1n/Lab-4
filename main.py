
items = [
    {"name": "r", "size": 3, "survival_points": 25},
    {"name": "m", "size": 2, "survival_points": 20},
    {"name": "a", "size": 1, "survival_points": 10},
    {"name": "t", "size": 1, "survival_points": 25},
    {"name": "ax", "size": 3, "survival_points": 20},
    {"name": "p", "size": 2, "survival_points": 15},
    {"name": "am", "size": 2, "survival_points": 15},
    {"name": "k", "size": 1, "survival_points": 15},
    {"name": "s", "size": 2, "survival_points": 20},
    {"name": "f", "size": 1, "survival_points": 15},
    {"name": "c", "size": 2, "survival_points": 20},
]


sorted_items = sorted(items, key=lambda x: x["survival_points"], reverse=True)


backpack_width = 2
backpack_height = 4


packed_items = []
remaining_space = backpack_width * backpack_height


for item in sorted_items:
    if item["size"] <= remaining_space:
        packed_items.append(item["name"])
        remaining_space -= item["size"]


print("Упакованные предметы:", packed_items)
total_survival_points = sum(item["survival_points"] for item in sorted_items if item["name"] in packed_items)
print("Итоговые очки выживания:", total_survival_points)
