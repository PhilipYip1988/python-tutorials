import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def create_image(row, col, index):
    image_data = np.array([[(0, 0, 0), (0, 0, 0)],
                           [(0, 0, 0), (0, 0, 0)]], dtype=np.uint8)
    
    image_data[:, :, 0][row, col] = 255
    image = Image.fromarray(image_data)
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.set_xticks(np.arange(2), [str(i) for i in range(2)])
    ax.set_yticks(np.arange(2), [str(i) for i in range(2)])
    ax.set_xlabel('column')
    ax.set_ylabel('row')
    ax.set_title(f'row{row:01d} col{col:01d}')
    fig.savefig(f'img_{index:03d}.png')

create_image(0, 0, 1)
create_image(0, 1, 2)
create_image(1, 0, 3)
create_image(1, 1, 4)