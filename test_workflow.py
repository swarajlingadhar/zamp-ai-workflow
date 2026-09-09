from workflow import (
    find_category,
    find_priority,
    assign_team
)


message = "My payment failed and money was deducted"

category = find_category(message)
priority = find_priority(message)
team = assign_team(category)


assert category == "Payment Issue"
assert priority == "Medium"
assert team == "Payments Team"


print("All tests passed successfully!")