from interface import *
from PIL import Image, ImageFilter

WIDTH, HEIGHT = photo_label.geometry().width(), photo_label.geometry().height()

def error(message):
    mb = QMessageBox()
    mb.setText(message)
    mb.exec_()

def filter(all_object):
    expansion = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]
    result = list()

    for fliename in all_object:
        for exp in expansion:
            if filename.endswith(exp):
                result.append(filename)

    return result

def choose_workdir():
    global work_dir
    work_dir = QFileDialog.getExistingDirectory()
    try:
        file_names = filter(os.listdir(work_dir))
        photo_list_widget.addItems(file_names)
    except:
        error("Спочатку виберіть папку з зображеннями")

def show_photo():
    global name_photo
    name_photo = photo_list_widget.currentItem().text()
    photo.load(os.path.join(work_dir, name_photo))
    photo_label.setPixmap(photo.scaled(WIDTH, HEIGHT, aspectRatioMode= Qt.KeepAspectRatio))

def make_left():
    try:
        abs_path = os.path.abspath(__file__ + "/..")
        new_name_photo = os.path.join(abs_path, "image", "rotate_left" + name_photo)
        with Image.open(os.path.join(work_dir, name_photo)) as obj_photo:
            photo_rotate = obj_photo.transpose(Image.ROTATE_90)
            photo_rotate.save(new_name_photo)
        photo.load(os.path.join(new_name_photo))
        photo_label.setPixmap(photo.scaled(WIDTH, HEIGHT, aspectRatioMode= Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію")

def make_right():
    try:
        abs_path = os.path.abspath(__file__ + "/..")
        new_name_photo = os.path.join(abs_path, "image", "rotate_right" + name_photo)
        with Image.open(os.path.join(work_dir, name_photo)) as obj_photo:
            photo_rotate = obj_photo.transpose(Image.ROTATE_270)
            photo_rotate.save(new_name_photo)
        photo.load(os.path.join(new_name_photo))
        photo_label.setPixmap(photo.scaled(WIDTH, HEIGHT, aspectRatioMode= Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію")

def make_mirror():
    try:
        abs_path = os.path.abspath(__file__ + "/..")
        new_name_photo = os.path.join(abs_path, "image", "flip_mirror" + name_photo)
        with Image.open(os.path.join(work_dir, name_photo)) as obj_photo:
            photo_flip = obj_photo.transpose(Image.FLIP_LEFT_RIGHT)
            photo_flip.save(new_name_photo)
        photo.load(os.path.join(new_name_photo))
        photo_label.setPixmap(photo.scaled(WIDTH, HEIGHT, aspectRatioMode= Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію")

def make_blur():
    try:
        abs_path = os.path.abspath(__file__ + "/..")
        new_name_photo = os.path.join(abs_path, "image", "blur_" + name_photo)
        with Image.open(os.path.join(work_dir, name_photo)) as obj_photo:
            photo_blur = obj_photo.filter(ImageFilter.GaussianBlur(int(slider.value())))
            photo_blur.save(new_name_photo)
        photo.load(os.path.join(new_name_photo))
        photo_label.setPixmap(photo.scaled(WIDTH, HEIGHT, aspectRatioMode= Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію")

def make_b_w():
    try:
        abs_path = os.path.abspath(__file__ + "/..")
        new_name_photo = os.path.join(abs_path, "image", "BW_" + name_photo)
        with Image.open(os.path.join(work_dir, name_photo)) as obj_photo:
            photo_bw = obj_photo.convert("L")
            photo_bw.save(new_name_photo)
        photo.load(os.path.join(new_name_photo))
        photo_label.setPixmap(photo.scaled(WIDTH, HEIGHT, aspectRatioMode= Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію")


folder.clicked.connect(choose_workdir)
left.clicked.connect(make_left)
right.clicked.connect(make_right)
mirror.clicked.connect(make_mirror)
blur.clicked.connect(make_blur)
wb.clicked.connect(make_b_w)
photo_list_widget.clicked.connect(show_photo)

window.show()
app.exec_()
