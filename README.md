### This is a Python script that performs a series of operations using the CloudCompare application. The operations are:

1. `cloud_compare_merge`: Merges point clouds in a directory and its subdirectories.

2. `cloud_compare_ss`: Sub-samples the merged point clouds.

3. `cloud_compare_final_merge`: Merges the sub-sampled point clouds into a single final point cloud.

The script uses the `subprocess` module to call the CloudCompare application with specified parameters for each operation. The merged and sub-sampled point clouds are saved in separate directories as **.e57 files**.