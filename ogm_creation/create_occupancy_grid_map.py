import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def create_occupancy_grid_map_and_save_image(pcd_path, floor_z, grid_resolution, output_image_path):
    # Load the PCD file
    pcd = o3d.io.read_point_cloud(pcd_path)

    # Convert the PCD data to a NumPy array
    point_cloud_data = np.asarray(pcd.points)

    # Define parameters for the occupancy grid map
    grid_size_x = int(np.ceil((np.max(point_cloud_data[:, 0]) - np.min(point_cloud_data[:, 0])) / grid_resolution))
    grid_size_y = int(np.ceil((np.max(point_cloud_data[:, 1]) - np.min(point_cloud_data[:, 1])) / grid_resolution))

    # Create an empty occupancy grid map filled with gray
    occupancy_grid = np.full((grid_size_x, grid_size_y), 128, dtype=np.uint8)

    # Convert point cloud data to grid coordinates
    grid_x = np.floor((point_cloud_data[:, 0] - np.min(point_cloud_data[:, 0])) / grid_resolution).astype(int)
    grid_y = np.floor((point_cloud_data[:, 1] - np.min(point_cloud_data[:, 1])) / grid_resolution).astype(int)

    # Set white pixels for points on the floor (Z value close to the floor_z)
    floor_points = np.abs(point_cloud_data[:, 2] - floor_z) < 0.47  # Adjust the threshold (thickness of floor)as needed
    occupancy_grid[grid_x[floor_points], grid_y[floor_points]] = 255  # White

    # Set black pixels for points on the walls (you may need more sophisticated wall detection)
    # For simplicity, let's assume that all points 30 cm above the floor, and in a range of 20 cm are walls
    wall_points = np.abs(point_cloud_data[:, 2] - (floor_z+2.0)) < 0.1  # Adjust the threshold as needed
    occupancy_grid[grid_x[wall_points], grid_y[wall_points]] = 0  # Black

    # Save the occupancy grid map as a PNG image
    plt.imsave(output_image_path, occupancy_grid, cmap='gray')
    return occupancy_grid

# Example usage:
pcd_path = "../Con_SLAM_0_05.pcd"  # Replace with the path to your PCD file
floor_z = 9.71  # Adjust as needed according to the floor coordinate
grid_resolution = 0.35 # Specify the grid resolution in meters
output_image_path = "../occupancy_grid.png"  # Specify the output image path
create_occupancy_grid_map_and_save_image(pcd_path, floor_z, grid_resolution, output_image_path)
