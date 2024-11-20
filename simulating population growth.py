import matplotlib.pyplot as plt

# Parameters for the simulation
initial_population = 50  # Starting population
growth_rate = 0.1        # Growth rate (r)
carrying_capacity = 1000 # Carrying capacity (K)
time_steps = 100         # Number of time steps to simulate

# Initialize population list with the initial population
population = [initial_population]

# Run the simulation
for t in range(1, time_steps + 1):
    current_population = population[-1]
    new_population = current_population + growth_rate * current_population * (1 - current_population / carrying_capacity)
    population.append(new_population)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(population, label="Population")
plt.axhline(y=carrying_capacity, color='r', linestyle='--', label="Carrying Capacity")
plt.xlabel("Time Steps")
plt.ylabel("Population")
plt.title("Population Growth Simulation")
plt.legend()
plt.show()
