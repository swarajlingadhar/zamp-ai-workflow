import csv

from workflow import (
    find_category,
    find_priority,
    assign_team,
    generate_response
)


total_tickets = 0
high_priority = 0
payment_issues = 0


with open("sample_tickets.csv", "r") as file:
    tickets = csv.DictReader(file)

    for ticket in tickets:
        total_tickets += 1

        message = ticket["message"]

        category = find_category(message)
        priority = find_priority(message)
        team = assign_team(category)
        response = generate_response(category)

        if priority == "High":
            high_priority += 1

        if category == "Payment Issue":
            payment_issues += 1

        print("\n--- Ticket", ticket["id"], "---")
        print("Message:", message)
        print("Category:", category)
        print("Priority:", priority)
        print("Team:", team)
        print("Response:", response)


print("\n========== WORKFLOW KPIs ==========")
print("Total Tickets:", total_tickets)
print("High Priority Tickets:", high_priority)
print("Payment Issues:", payment_issues)
print("Automation Rate: 100%")