import numpy as np
import open3d as o3d

# print(o3d.__version__)
# """current: 0.16.0"""

# # Visualize point cloud
# # The first part of the tutorial reads a point cloud and visualizes it.

print("Load a ply point cloud, print it, and render it")
ply_point_cloud = o3d.data.PLYPointCloud()
pcd = o3d.io.read_point_cloud(ply_point_cloud.path)
print(pcd, '\n')
print(np.asarray(pcd.points), '\n')



o3d.visualization.draw_geometries([pcd])
# """ additional arguments
# zoom=0.3412,
# front=[0.4257, -0.2125, -0.8795],
# lookat=[2.6172, 2.0475, 1.532],
# up=[-0.0694, -0.9768, 0.2024]
# """




# Python API
# mesh = o3d.geometry.TriangleMesh.create_sphere()
# mesh.compute_vertex_normals()
# o3d.visualization.draw(mesh, raw_mode=True)