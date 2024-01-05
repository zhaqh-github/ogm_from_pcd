# ogm_from_pcd
## Overview
**PC2OGM** is an algorithm developed for generating an Occupancy Grid Map (OGM) from point cloud data, along with associated functions for testing the accuracy of the generated map through re-projection. 
  
## How to use
1.**create_occupancy_grid_map_and_save_image**: Developed the create_occupancy_grid_map_and_save_image function to create an OGM from point cloud data and save it as a PNG image file.  
`pcd_path`: Replace with the actual path to your PCD file  
`floor_z`: Adjust as needed for the actual floor z_coordinate  
`grid_resolution`: Specify the grid resolution in meters  
`output_image_path`: Specify the output image path  
Run the function:
`python3 cd/path/to/create_occupancy_grid_map.py`  

  
2.**testreprojection**: The primary purpose of this test is to compare the reprojection-generated 2D coordinates in the occupancy grid map with the original 2D coordinates to assess the precision of the reprojection and inverse reprojection processes  
  
Run the test: `python3 cd/path/to/testreprojection.py`  

PCD file Link: https://drive.google.com/drive/folders/1jofyz_LqmUCmKQmoMSPKpWAhPikRSRuM?usp=drive_link
