import numpy as np
import matplotlib.pyplot as plt
def reproject_3d_to_2d_batch(coordinates_3d, ogm, grid_resolution, floor_z,point_cloud_data):
    """
    Reproject a list of 3D coordinates to 2D coordinates on an occupancy grid map.

    Args:
    - coordinates_3d (numpy.ndarray): Array of 3D coordinates (Nx3).
    - ogm (numpy.ndarray): 2D occupancy grid map (0 for black, 255 for white).
    - grid_resolution (float): Resolution of the grid in meters.
    - floor_z (float): Z-coordinate of the floor in the TLS coordinate system.

    Returns:
    - list of tuples: List of (x, y) coordinates in 2D corresponding to the input 3D coordinates.
    """
    # Initialize an empty list to store the 2D coordinates
    coordinates_2d_list = []

    for coord_3d in coordinates_3d:
        x_3d, y_3d, z_3d = coord_3d

        # Ensure the 3D coordinate is above the floor 值得思考的是floorz是最低的高度
        if z_3d >= floor_z:         # +0.47?
            # Calculate grid coordinates, RELATED COORDINATES(ORIGINAL POINT)
            grid_x = int(np.clip((x_3d - np.min(point_cloud_data[:, 0]))/ grid_resolution, 0, ogm.shape[0] - 1))
            grid_y = int(np.clip((y_3d -np.min(point_cloud_data[:, 1])) / grid_resolution, 0, ogm.shape[1] - 1))

            # Check if the grid coordinates are within the OGM bounds
            if 0 <= grid_x < ogm.shape[0] and 0 <= grid_y < ogm.shape[1]:
                # Check if the corresponding pixel in the OGM is white (floor)
                if (ogm[grid_x, grid_y]).all() == 1:
                    coordinates_2d_list.append((x_3d, y_3d))

    return coordinates_2d_list

# Example usage:
# ogm = plt.imread("../occupancy_grid.png")[:,:,0]  # Load the occupancy grid map one chanel from the saved image
# grid_resolution = 0.35  # Resolution of the grid in meters (should match the value used earlier)
# floor_z = 9.71  # Z-coordinate of the floor in the TLS coordinate system (should match the value used earlier)
# # List of 3D coordinates to reproject to 2D
# coordinates_3d = [(110, 85, 10.18), (117, 107, 10.18), (165, 90, 10.18)]  # Replace with your desired 3D coordinates
# # Reproject the 3D coordinates to 2D
# coordinates_2d = reproject_3d_to_2d_batch(coordinates_3d, ogm, grid_resolution, floor_z)
# #print(coordinates_2d)
