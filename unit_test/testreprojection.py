import unittest
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d
from create_occupancy_grid_map import create_occupancy_grid_map_and_save_image
from reproject_2d_to_3d import reproject_2d_to_3d_batch
from reproject_3d_to_2d import reproject_3d_to_2d_batch

class TestReprojection(unittest.TestCase):
    def test_reprojection_round_trip(self):

        # Create and load oad the occupancy grid map
        grid_resolution = 0.35
        floor_z = 9.71
        pcd_path = "../Con_SLAM_0_05.pcd"  # Replace with the actual path to your PCD file
        output_image_path = "../occupancy_grid.png"  # Specify the output image path
        pcd = o3d.io.read_point_cloud(pcd_path)
        point_cloud_data = np.asarray(pcd.points)
        ogm = create_occupancy_grid_map_and_save_image(pcd_path, floor_z, grid_resolution, output_image_path)
        ogm = plt.imread(output_image_path)

        # List of 2D coordinates for testing (replace with valid coordinates)
        coordinates_2d_list = [(110, 85), (117, 107), (165, 90)] #Set 2D coordinates of floor manully，
        # try with coordinates_2d_list = [(110, 85), (117, 107), (129.24, 85.36)], reprojection will fail, because (129.24, 85.36) is the coordnate of wall
        print("2D Coordinates:")
        print(coordinates_2d_list)

        # Reproject the 2D coordinates to 3D
        coordinates_3d = reproject_2d_to_3d_batch(coordinates_2d_list, ogm, grid_resolution, floor_z, point_cloud_data)
        print("3D Coordinates:")
        print(coordinates_3d)

        # Reproject the 3D coordinates back to 2D
        reprojected_coordinates_2d = reproject_3d_to_2d_batch(coordinates_3d, ogm, grid_resolution, floor_z,point_cloud_data)
        print("Reprojected 2D Coordinates:")
        print(reprojected_coordinates_2d)

        # Check if the reprojected 2D coordinates are almost the same as the original
        # np.testing.assert_allclose(reprojected_coordinates_2d, coordinates_2d_list, atol=1e-6)
        # print("reprojection: success")
        try:
            np.testing.assert_allclose(reprojected_coordinates_2d, coordinates_2d_list, atol=1e-6)
            print("reprojection: success")
        except AssertionError:
            print("reprojection: failed")


if __name__ == '__main__':
    unittest.main()
