import cv2
import lensfunpy # See for details https://github.com/letmaik/lensfunpy

cam_maker = 'Generic'
cam_model = 'Crop-factor 1.7'
lens_maker = 'Generic'
lens_model = 'Fisheye 8-20mm f/1.0'
lens_type = 'FISHEYE_ORTHOGRAPHIC'

db = lensfunpy.Database()
cam = db.find_cameras(cam_maker, cam_model)[0]
lens = db.find_lenses(cam, lens_maker, lens_model, lens_type)[0]


focal_length = 5.6
aperture =  1.12
distance = 1000000
scale = 1.1
image_path = 'circle.jpg'
undistorted_image_path = 'square.jpg'

im = cv2.imread(image_path)
height, width = im.shape[0], im.shape[1]

mod = lensfunpy.Modifier(lens, cam.crop_factor, width, height)
mod.initialize(focal_length, aperture, distance, scale)

undist_coords = mod.apply_geometry_distortion()
im_undistorted = cv2.remap(im, undist_coords, None, cv2.INTER_LANCZOS4)
cv2.imwrite(undistorted_image_path, im_undistorted)
