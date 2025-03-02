import pulp
import pandas as pd
import matplotlib.pyplot as plt

def optimize_manufacturing_resources():
    """
    Solves a manufacturing resource allocation problem using linear programming.
    A furniture company needs to determine the optimal production mix of tables and chairs
    to maximize profit, subject to constraints on labor hours, material, and machine time.
    """
    # Create the optimization problem (maximize profit)
    prob = pulp.LpProblem("Furniture_Manufacturing_Optimization", pulp.LpMaximize)

    # Decision variables: number of tables and chairs to produce
    tables = pulp.LpVariable("Tables", lowBound=0, cat='Integer')
    chairs = pulp.LpVariable("Chairs", lowBound=0, cat='Integer')

    # Resources and constraints
    # Resource requirements per unit
    table_data = {
        'labor_hours': 8,     # hours per table
        'wood': 30,           # board feet per table
        'machine_time': 4,    # hours per table
        'profit': 220         # profit per table
    }

    chair_data = {
        'labor_hours': 5,     # hours per chair
        'wood': 10,           # board feet per chair
        'machine_time': 2,    # hours per chair
        'profit': 80          # profit per chair
    }

    # Available resources
    available_resources = {
        'labor_hours': 400,   # total available labor hours
        'wood': 800,          # total available wood (board feet)
        'machine_time': 150   # total available machine time (hours)
    }

    # Minimum production requirements
    min_tables = 10
    min_chairs = 20

    # Objective function: Maximize profit
    prob += table_data['profit'] * tables + chair_data['profit'] * chairs, "Total_Profit"

    # Add constraints
    # Resource constraints
    prob += table_data['labor_hours'] * tables + chair_data['labor_hours'] * chairs <= available_resources['labor_hours'], "Labor_Constraint"
    prob += table_data['wood'] * tables + chair_data['wood'] * chairs <= available_resources['wood'], "Wood_Constraint"
    prob += table_data['machine_time'] * tables + chair_data['machine_time'] * chairs <= available_resources['machine_time'], "Machine_Time_Constraint"

    # Minimum production constraints
    prob += tables >= min_tables, "Minimum_Tables"
    prob += chairs >= min_chairs, "Minimum_Chairs"

    # Solve the problem
    prob.solve()

    # Check if the problem was solved successfully
    if pulp.LpStatus[prob.status] != 'Optimal':
        return "No optimal solution found."

    # Extract results
    optimal_tables = int(tables.value())
    optimal_chairs = int(chairs.value())
    optimal_profit = pulp.value(prob.objective)

    # Extract resource usage
    labor_used = table_data['labor_hours'] * optimal_tables + chair_data['labor_hours'] * optimal_chairs
    wood_used = table_data['wood'] * optimal_tables + chair_data['wood'] * optimal_chairs
    machine_time_used = table_data['machine_time'] * optimal_tables + chair_data['machine_time'] * optimal_chairs

    # Calculate resource utilization percentages
    resource_utilization = {
        'labor_hours': (labor_used / available_resources['labor_hours']) * 100,
        'wood': (wood_used / available_resources['wood']) * 100,
        'machine_time': (machine_time_used / available_resources['machine_time']) * 100
    }

    # Determine the binding constraints
    binding_constraints = []
    for resource, utilized_pct in resource_utilization.items():
        if abs(utilized_pct - 100) < 0.01:  # If utilization is approximately 100%
            binding_constraints.append(resource)

    # Sensitivity analysis: Shadow prices
    shadow_prices = {}
    for name, constraint in prob.constraints.items():
        shadow_prices[name] = constraint.pi

    # Prepare results
    results = {
        'optimal_production': {'tables': optimal_tables, 'chairs': optimal_chairs},
        'optimal_profit': optimal_profit,
        'resource_usage': {
            'labor_hours': labor_used,
            'wood': wood_used,
            'machine_time': machine_time_used
        },
        'resource_utilization': resource_utilization,
        'binding_constraints': binding_constraints,
        'shadow_prices': shadow_prices
    }

    return results

def visualize_results(results):
    """
    Create visualizations of the optimization results.
    """
    # Production mix
    production = pd.Series(results['optimal_production'])
    plt.figure(figsize=(10, 5))

    # Plot production numbers
    ax1 = plt.subplot(1, 2, 1)
    production.plot(kind='bar', ax=ax1, color=['#1f77b4', '#ff7f0e'])
    plt.title('Optimal Production Mix')
    plt.ylabel('Units to Produce')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Resource utilization
    ax2 = plt.subplot(1, 2, 2)
    utilization = pd.Series(results['resource_utilization'])
    utilization.plot(kind='bar', ax=ax2, color=['#2ca02c', '#d62728', '#9467bd'])
    plt.title('Resource Utilization')
    plt.ylabel('Utilization (%)')
    plt.axhline(y=100, color='r', linestyle='-', alpha=0.3)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

    return

# Run the optimization
results = optimize_manufacturing_resources()

# Print the results
print("Optimization Results:")
print(f"Optimal Production: {results['optimal_production']['tables']} tables and {results['optimal_production']['chairs']} chairs")
print(f"Optimal Profit: ${results['optimal_profit']:.2f}")
print("\nResource Usage:")
for resource, usage in results['resource_usage'].items():
    print(f"  {resource.replace('_', ' ').title()}: {usage:.2f} units ({results['resource_utilization'][resource]:.2f}%)")
print("\nBinding Constraints:")
if results['binding_constraints']:
    for constraint in results['binding_constraints']:
        print(f"  {constraint.replace('_', ' ').title()}")
else:
    print("  None")

# Visualize the results
visualize_results(results)
