def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    ticket_cost_adult=no_of_adults*37550.0
    ticket_cost_child=(no_of_children*37550.0)/3
    service_tax=((ticket_cost_child+ticket_cost_adult)*7)/100
    total=service_tax+ticket_cost_adult+ticket_cost_child
    total_ticket_cost=total-((total*10)/100)
    return total_ticket_cost

total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)
