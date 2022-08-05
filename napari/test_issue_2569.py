import numpy as np
import napari

viewer = napari.Viewer()

try:
    viewer.add_image(np.random.rand(64, 64), scale=(0, 1))
except Exception as e:
    print(e)
