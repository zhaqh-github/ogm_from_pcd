import numpy as np
import matplotlib.pyplot as plt

def reproject_2d_to_3d_batch(coordinates_2d, ogm, grid_resolution, floor_z, point_cloud_data):
    """ # change coordinates_2d to coordinates_2d_list
    Reproject a list of 2D coordinates to 3D coordinates in the TLS coordinate system based on an occupancy grid map.    
    Args:
    - coordinates_2d (list of tuples): List of (x, y) coordinates in 2D.
    - ogm (numpy.ndarray): 2D occupancy grid map (0 for black, 255 for white).
    - grid_resolution (float): Resolution of the grid in meters.
    - floor_z (float): Z-coordinate of the floor in the TLS coordinate system.    
    Returns:
    - numpy.ndarray: 3D coordinates in the TLS coordinate system corresponding to the input 2D coordinates.
    """
    # Initialize an empty list to store the 3D coordinates
    coordinates_3d = []

    for x_2d, y_2d in coordinates_2d:
        # change coordinates_2d to coordinates_2d_list
        # Convert 2D coordinates to grid indices
        grid_x = int(np.clip((x_2d-np.min(point_cloud_data[:, 0])) / grid_resolution, 0, ogm.shape[0] - 1))
        grid_y = int(np.clip((y_2d-np.min(point_cloud_data[:, 1])) / grid_resolution, 0, ogm.shape[1] - 1))

        # Check if the grid coordinates are valid and correspond to a white pixel (floor)
        if 0 <= grid_x < ogm.shape[0] and 0 <= grid_y < ogm.shape[1]:
            #if ogm[grid_x, grid_y] == 255:## !!!The map uses grayscale values[0,1](print(np.min(ogm))print(np.max(ogm)))to represent occupancy status, rather than pure black and white.
            if (ogm[grid_x, grid_y]).all() == 1:
            #If requirement is for all white pixels to match, continue to use .all(). Otherwise, keep .any(), depending on application scenario.
            # Calculate 3D coordinates
                x_3d = x_2d
                y_3d = y_2d
                z_3d = floor_z+0.47
                coordinates_3d.append([x_3d, y_3d, z_3d])
    return np.array(coordinates_3d)

# Example usage:
#ogm = plt.imread("../occupancy_grid.png")[:,:,0] # Load the occupancy grid map from the saved image
#grid_resolution = 0.35  # Resolution of the grid in meters (should match the value used earlier)
#floor_z = 9.71  # Z-coordinate of the floor in the TLS coordinate system (should match the value used earlier)
# List of 2D coordinates to reproject to 3D
#coordinates_2d_list = [(110, 85), (117, 107), (165, 90)]  # Replace with your desired 2D coordinates /floor只能选择地板
# Reproject the 2D coordinates to 3D
#coordinates_3d = reproject_2d_to_3d_batch(coordinates_2d_list, ogm, grid_resolution, floor_z,point_cloud_data)

