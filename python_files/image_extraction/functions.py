def load_obj(path, file_type): # this function returned file path
    import glob
    import os
    if file_type == '-': # for loading subfolder
        return glob.glob(os.path.join(path))
    elif file_type == '*' :# means all
        return glob.glob(os.path.join(path, "*"))
    else : # require file type
        return glob.glob(os.path.join(path, "*.{}".format(file_type)))

def show_img(img):
    import matplotlib.pyplot as plt
    plt.imshow(img, cmap="gray")
    plt.colorbar()
    plt.show()

# plot ractangle in image by txt file
# partmeter is path of image and text file
# only 1 image per text
def plot_rectangle(img, txt, format='pixel'):
    import cv2
    import matplotlib.pyplot as plt

    try: # read with path
        name_img = img.split('\\')[-1].split('.')[0]
        name_label = txt.split('\\')[-1].split('.')[0]
        img = cv2.imread(img, 0)
    except: # read with instance
        name_img = False
        name_label = False
        img = img

    if format == 'pixel':
        if name_img ==  name_label:
            with open(txt, 'r') as f:
                for line in f:
                    line = line.split()
                    x = float(line[1])
                    y = float(line[2])
                    w = float(line[3])
                    h = float(line[4])
                    x_min = x - w
                    x_max = x + w
                    y_min = y - h
                    y_max = y + h
                    plt.plot([x_min, x_max], [y_min, y_min], c='r')
                    plt.plot([x_min, x_max], [y_max, y_max], c='r')
                    plt.plot([x_min, x_min], [y_min, y_max], c='r')
                    plt.plot([x_max, x_max], [y_min, y_max], c='r')
        else:
            print('error, name image and name label not match...')
            print('Hint: you should sort path name before use this function')
    
    elif format == 'yolo':
        if name_img == name_label:
            if name_img == False and name_label == False:
                for line in txt:
                    x_center = float(line[0])
                    y_center = float(line[1])
                    width = float(line[2])
                    height = float(line[3])
                    img_w, img_h = img.size # for PIL image
                    x_min = int((x_center - width/2) * img_w)
                    x_max = int((x_center + width/2) * img_w)
                    y_min = int((y_center - height/2) * img_h)
                    y_max = int((y_center + height/2) * img_h)
                    plt.plot([x_min, x_max], [y_min, y_min], c='r')
                    plt.plot([x_min, x_max], [y_max, y_max], c='r')
                    plt.plot([x_min, x_min], [y_min, y_max], c='r')
                    plt.plot([x_max, x_max], [y_min, y_max], c='r')
            else:
                with open(txt, 'r') as f:
                    for line in f:
                        line = line.split()
                        # line 0 = class, line 1 = x_center, line 2 = y_center, line 3 = width, line 4 = height
                        x_center = float(line[1])
                        y_center = float(line[2])
                        width = float(line[3])
                        height = float(line[4])
                        img_w, img_h = img.shape
                        x_min = int((x_center - width/2) * img_w)
                        x_max = int((x_center + width/2) * img_w)
                        y_min = int((y_center - height/2) * img_h)
                        y_max = int((y_center + height/2) * img_h)
                        plt.plot([x_min, x_max], [y_min, y_min], c='r')
                        plt.plot([x_min, x_max], [y_max, y_max], c='r')
                        plt.plot([x_min, x_min], [y_min, y_max], c='r')
                        plt.plot([x_max, x_max], [y_min, y_max], c='r')

        else:
            print('error, name image and name label not match...')
            print('Hint: you should sort path name before use this function')

    return img

def read_np_image(path_img, channel=1):
    import cv2
    if channel == 1:
        return cv2.imread(path_img, 0)
    elif channel == 3:
        return cv2.imread(path_img)


# the image is saved in the same old resolution = len data in numpy array and display the image by flip vertical with inverte y-axis
def save_image(data, cm, fn):
    import matplotlib.pyplot as plt
    import numpy as np
    sizes = np.shape(data)
    height = float(sizes[0])
    width = float(sizes[1])
     
    fig = plt.figure()
    fig.set_size_inches(width/height, 1, forward=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
 
    ax.imshow(data, cmap=cm)
    plt.savefig(fn, dpi = height) 
    plt.close()
