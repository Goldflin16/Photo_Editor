from PIL import Image, ImageFilter, ImageEnhance


with Image.open("original.jpg") as photo:
    print(photo.size)
    print(photo.format)
    print(photo.mode)


    photo_rotate = photo.transpose(Image.ROTATE_90)
    photo_rotate.save("original_rotate.jpg")
    photo_rotate_any = photo.rotate(90)
    photo_rotate_any.save("original_rotate_any.jpg")
    photo_rotate = photo.transpose(Image.ROTATE_270)
    photo_rotate.save("original_rotate_270.jpg")
    photo_rotate = photo.transpose(Image.FLIP_LEFT_RIGHT)
    photo_rotate.save("original_rorate_flip.jpg")
    photo_blur = photo.filter(ImageFilter.BLUR)
    photo_blur.save("original_blur.jpg")
    photo_blur_box = photo.filter(ImageFilter.BoxBlur(3))
    photo_blur_box.save("original_blur_box.jpg")
    photo_blur_gaus = photo.filter(ImageFilter.GaussianBlur(3))
    photo_blur_gaus.save("original_blur_gaus.jpg")
    photo_crop = photo.crop((0,0,500,500))
    photo_crop.save("photo_crop.jpg")
    photo_resize = photo.resize((2400, 1600))
    photo_resize.save("photo_resize.jpg")