import pulp

def solve_diet_problem():
    # Define the problem
    problem = pulp.LpProblem("Diet Optimization", pulp.LpMinimize)

    # Define the variables (foods)
    foods = ['Chicken', 'Beef', 'Vegetables']
    cost = {'Chicken': 0.5, 'Beef': 0.8, 'Vegetables': 0.2}
    food_vars = pulp.LpVariable.dicts("Food", foods, 0)

    # Objective function: Minimize the total cost of foods
    problem += pulp.lpSum([cost[i] * food_vars[i] for i in foods]), "Total Cost"

    # Constraints
    # Calories constraint: Total calories should be between 500 and 800
    problem += pulp.lpSum([food_vars['Chicken'] * 200 + 
                           food_vars['Beef'] * 300 + 
                           food_vars['Vegetables'] * 100]) >= 500, "MinCalories"
    problem += pulp.lpSum([food_vars['Chicken'] * 200 + 
                           food_vars['Beef'] * 300 + 
                           food_vars['Vegetables'] * 100]) <= 800, "MaxCalories"

    # Protein constraint: At least 50 grams of protein
    problem += pulp.lpSum([food_vars['Chicken'] * 30 + 
                           food_vars['Beef'] * 25 + 
                           food_vars['Vegetables'] * 10]) >= 50, "Protein"

    # Fat constraint: No more than 20 grams of fat
    problem += pulp.lpSum([food_vars['Chicken'] * 5 + 
                           food_vars['Beef'] * 10 + 
                           food_vars['Vegetables'] * 1]) <= 20, "Fat"

    # Solve the problem
    problem.solve()
    print("Status:", pulp.LpStatus[problem.status])

    # Print the results
    for v in problem.variables():
        print(v.name, "=", v.varValue)
    print("Total Cost of Diet = ", pulp.value(problem.objective))

solve_diet_problem()
