#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(img):
    img_cp = img.copy()
    r_coeff = 0.2126
    g_coeff = 0.7152
    b_coeff = 0.0722

    gray = np.dot(img_cp[..., :3], [r_coeff, g_coeff, b_coeff])
    return gray


def to_red(img):
    img_cp = img.copy()
    col_size = img[:, 0:, 1].shape
    img_cp[:, 0:, 1] = np.zeros(col_size)
    img_cp[:, 0:, 2] = np.zeros(col_size)
    return img_cp


def to_green(img):
    img_cp = img.copy()
    col_size = img[:, 0:, 1].shape
    img_cp[:, 0:, 0] = np.zeros(col_size)
    img_cp[:, 0:, 2] = np.zeros(col_size)
    return img_cp


def to_blue(img):
    img_cp = img.copy()
    col_size = img[:, 0:, 1].shape
    img_cp[:, 0:, 0] = np.zeros(col_size)
    img_cp[:, 0:, 1] = np.zeros(col_size)
    return img_cp


def main():
    img = plt.imread("painting.png")
    gs_img = to_grayscale(img)
    plt.gray()
    plt.imshow(gs_img)
    plt.show()

    # Test RGB figures
    fig, axes = plt.subplots(3, 1)
    axes[0].imshow(to_red(img))
    axes[1].imshow(to_green(img))
    axes[2].imshow(to_blue(img))
    plt.show()


if __name__ == "__main__":
    main()
