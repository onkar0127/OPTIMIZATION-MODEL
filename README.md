# OPTIMIZATION-MODEL

**COMPANY:CODTECH IT SOLUTIONS

NAME:ONKAR GITE

INTERN ID:CT08TMP

DOMAIN:DATA SCIENCE

DURATION:4 WEEK

MENTOR:NEELA SANTOSH**

# Manufacturing Resource Optimization

## Project Overview

This project implements a linear programming solution for optimizing manufacturing resource allocation in a furniture production business. Using Python's PuLP library, the application determines the optimal production mix of tables and chairs to maximize profit while respecting resource constraints.

## Business Problem

A furniture manufacturing company needs to determine how many tables and chairs to produce to maximize profits. The company faces several constraints:

- **Limited Resources**: 
  - 400 available labor hours
  - 800 board feet of wood
  - 150 machine hours

- **Production Requirements**:
  - Tables: Each requires 8 labor hours, 30 board feet of wood, 4 machine hours, and generates $220 profit
  - Chairs: Each requires 5 labor hours, 10 board feet of wood, 2 machine hours, and generates $80 profit
  - Minimum production quantities: 10 tables and 20 chairs

## Solution Features

- **Mathematical Optimization**: Implements linear programming to find the exact optimal solution
- **Resource Utilization Analysis**: Calculates and visualizes how efficiently each resource is being used
- **Constraint Analysis**: Identifies binding constraints (bottlenecks) in the production process
- **Sensitivity Analysis**: Calculates shadow prices to determine the value of additional resources
- **Data Visualization**: Provides clear charts of production quantities and resource utilization

## Technical Implementation

- **Language**: Python 3.x
- **Core Libraries**:
  - PuLP: For formulating and solving the linear programming model
  - Pandas: For data manipulation and preparation
  - Matplotlib: For creating visualizations

## Getting Started

### Prerequisites
- Python 3.x
- PuLP, pandas, and matplotlib libraries

### Installation
```bash
pip install pulp pandas matplotlib
```

### Running the Application
```bash
python manufacturing_optimization.py
```

## Usage Example

The application outputs:
- Optimal number of tables and chairs to produce
- Maximum achievable profit
- Resource usage details and utilization percentages
- Identification of production bottlenecks
- Visual representation of results

## Business Benefits

- **Maximized Profitability**: Ensures the most profitable production mix
- **Efficient Resource Allocation**: Eliminates waste by optimizing resource usage
- **Bottleneck Identification**: Highlights which resources are limiting production
- **Investment Guidance**: Provides data-driven insights for capacity expansion decisions
- **Production Planning**: Supports evidence-based production scheduling

## Future Enhancements

- Integration with real-time inventory management systems
- Multi-period planning capabilities
- Additional product types and constraints
- Interactive dashboard for scenario analysis
- Stochastic modeling to account for uncertainty in demand and supply

##output
![Image](https://github.com/user-attachments/assets/663926a9-461b-4ff0-bd7f-e5dbd18d418c)
