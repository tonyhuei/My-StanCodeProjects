"""
File: stanCodoshop.py
Name: Tony
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2) ** 0.5
    return float(dist)


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    rgb = []
    # total_red = 0 # total_green = 0 # total_blue = 0
    # for i in range(len(pixels)):
    #     total_red += pixels[i].red
    #     total_green += pixels[i].green
    #     total_blue += pixels[i].blue
    total_red = sum(pixel.red for pixel in pixels)
    total_green = sum(pixel.green for pixel in pixels)
    total_blue = sum(pixel.blue for pixel in pixels)
    red_avg = total_red // len(pixels)
    green_avg = total_green // len(pixels)
    blue_avg = total_blue // len(pixels)
    rgb.append(red_avg)
    rgb.append(green_avg)
    rgb.append(blue_avg)
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the
    average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    [red_avg, green_avg, blue_avg] = get_average(pixels)   # get list of average number red、green、blue pixels

    # small_distance = float("inf")
    # best = []
    # for i in range(len(pixels)):
    #     current_distance = get_pixel_dist(pixels[i], red_avg, green_avg, blue_avg)
    #     if current_distance < small_distance:
    #         best = pixels[i]
    #         small_distance = current_distance
    # return best
    # for index pixel enumerate(pixels)  # for data in enumerate(a)    # (index, element)
    #     pass

    # comprehensive     #[(20, pixel1),(30, pixel2),......]
    dist_list = list((get_pixel_dist(pixel, red_avg, green_avg, blue_avg), pixel) for pixel in pixels)
    best = min(dist_list, key=lambda ele: ele[0])   # tuple(distance, pixel)
    return best[1]


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    sp_pixels = []      # list of same position pixels in all images
    for x in range(width):
        for y in range(height):
            for i in range(len(images)):
                sp_pixels.append(images[i].get_pixel(x, y))
            best = get_best_pixel(sp_pixels)
            result.get_pixel(x, y).red = best.red
            result.get_pixel(x, y).green = best.green
            result.get_pixel(x, y).blue = best.blue
            for i in range(len(sp_pixels)):
                sp_pixels.pop()
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
