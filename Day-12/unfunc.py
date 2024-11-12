'''This program is mainly made by AI'''
import numpy as np

def cylinder_volume(radius, height):
    return np.pi * radius**2 * height

def cone_volume(radius, height):
    return (1/3) * np.pi * radius**2 * height

def sphere_volume(radius):
    return (4/3) * np.pi * radius**3

volume_ufunc_cylinder = np.frompyfunc(cylinder_volume, 2, 1)
volume_ufunc_cone = np.frompyfunc(cone_volume, 2, 1)
volume_ufunc_sphere = np.frompyfunc(sphere_volume, 1, 1)

radii = np.array([1, 2, 3, 4, 5])
heights = np.array([5, 10, 15, 20, 25])

cylinder_volumes = volume_ufunc_cylinder(radii, heights)
cone_volumes = volume_ufunc_cone(radii, heights)
sphere_volumes = volume_ufunc_sphere(radii)

print("Cylinder Volumes:", cylinder_volumes)
print("Cone Volumes:", cone_volumes)
print("Sphere Volumes:", sphere_volumes)

combined_volumes = np.array([cylinder_volumes, cone_volumes, sphere_volumes])
mean_volumes = np.mean(combined_volumes, axis=0)
volume_difference = cylinder_volumes - sphere_volumes

print("Mean Volumes Across Shapes:", mean_volumes)
print("Difference between Cylinder and Sphere Volumes:", volume_difference)
