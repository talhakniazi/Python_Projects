import numpy as np
import matplotlib.pyplot as plt

# Parameters
size = 1000  # size of the simulation grid
black_hole_mass = 1.0  # mass of the black hole (can adjust for different effects)
event_horizon_radius = 50  # radius of the black hole's event horizon in pixels

# Create a mesh grid for simulating spacetime around the black hole
x = np.linspace(-size // 2, size // 2, size)
y = np.linspace(-size // 2, size // 2, size)
X, Y = np.meshgrid(x, y)

# Distance from the center (black hole)
distance = np.sqrt(X**2 + Y**2)

# Simulate the gravitational lensing effect by altering light paths around the black hole
def gravitational_lensing(distance, mass):
    # Simple lensing effect based on inverse distance
    lensing_effect = 1 / (distance / event_horizon_radius + 0.1) * mass
    return lensing_effect

# Calculate the lensing effect (this will increase near the event horizon)
lensing_effect = gravitational_lensing(distance, black_hole_mass)

# Create a radial gradient for the black hole's appearance
gradient = 1 - np.exp(-lensing_effect)

# Plot the simulation
plt.figure(figsize=(8, 8))
plt.imshow(gradient, cmap="inferno", extent=(-size // 2, size // 2, -size // 2, size // 2))
plt.colorbar(label="Lensing effect strength")
plt.title("Black Hole Gravitational Lensing Simulation")
plt.xlabel("Distance from Black Hole Center (arbitrary units)")
plt.ylabel("Distance from Black Hole Center (arbitrary units)")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
