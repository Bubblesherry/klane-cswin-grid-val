import cv2
import open3d as o3d
import numpy as np
import configs.config_vis as cnf
import matplotlib.pyplot as plt

# from baseline.utils.vis_utils import *

def visualizer(pc_path, infer_lane):
    # point cloud: env
    pcd = o3d.io.read_point_cloud(pc_path[0])

    # read intensity
    xyzi = o3d.t.io.read_point_cloud(pc_path[0])
    intensity = xyzi.point['intensity']
    intensity = intensity.numpy()

    # normaliyze intensity
    intensity_nor = (intensity - intensity.min()) / (intensity.max() - intensity.min())

    # map intensity value to colormap
    colormap = plt.get_cmap('gist_stern') # https://matplotlib.org/stable/tutorials/colors/colormaps.html
    colors_rgba = colormap(intensity_nor)
    colors_rgb = colors_rgba[:, :, :3]
    colors_flattened = colors_rgb.reshape(-1, 3)

    pcd.colors = o3d.utility.Vector3dVector(colors_flattened)

    # point cloud: lane class
    pcd_cls = o3d.geometry.PointCloud()
    pc_xyz, pc_cls = get_point_cloud_from_bev_tensor_label(infer_lane, with_cls=True)
    pcd_cls.points = o3d.utility.Vector3dVector(pc_xyz)

    list_cls_idx = []
    for idx in pc_cls.tolist():
        list_cls_idx.append(cnf.pc_rgb_cls[idx])
    list_cls_idx_array = np.array(list_cls_idx)
    pcd_cls.colors = o3d.utility.Vector3dVector(np.array(list_cls_idx))

    o3d.visualization.draw_geometries([pcd, pcd_cls])
    # o3d.visualization.draw_geometries([pcd])
    return


def get_point_cloud_from_bev_tensor_label(bev_label, with_cls=False, z_fix=cnf.z_fix):
    '''
    * return
    *   n x 3 (x,y,z) [m] in np.array, with_cls == False
    *   n x 3 (x,y,z) [m], n x 1 (cls_idx) in np.array, with_cls == True
    '''
    bev_label_144 = bev_label[:, :144]

    points_arr = []
    cls_arr = []
    for i in range(6):
        points_in_pixel = np.where(bev_label_144 == i)
        _, num_points = np.shape(points_in_pixel)
        for j in range(num_points):
            x_point, y_point = get_point_from_pixel_in_m(points_in_pixel[1][j], points_in_pixel[0][j])
            points_arr.append([x_point, y_point, z_fix])
            if with_cls:
                cls_arr.append(i)  # cls

    if with_cls:
        return np.array(points_arr), np.array(cls_arr)
    else:
        return np.array(points_arr)

def get_point_from_pixel_in_m(x_pix, y_pix):
        x_lidar = 144 - (y_pix + 0.5)
        y_lidar = 72 - (x_pix + 0.5)

        return cnf.x_grid * x_lidar, cnf.y_grid * y_lidar