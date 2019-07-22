#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def center(a):
    return (a.shape[0] - 1) / 2, (a.shape[1] - 1) / 2


def radial_distance(a):
    c = center(a)
    print(f"center y ={c[0]}, center x ={c[1]}")
    x_range = a.shape[1] - c[1]
    dx = []
    for i in np.arange(-x_range + 1, x_range):
        dx.append(abs(i))

    y_range = a.shape[0] - c[0]
    dy = []
    for i in np.arange(-y_range + 1, y_range):
        dy.append(abs(i))

    print(f"dx={dx}")
    print(f"dy={dy}")

    print(f"a_shape={a.shape}")
    dx_arr, dy_arr = np.meshgrid(dx, dy)
    print(f"dx_arr shape={dx_arr.shape}, dy_arr shape={dy_arr.shape}")

    return np.sqrt(dx_arr**2 + dy_arr**2)


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))


def radial_mask(a):
    rd = radial_distance(a)
    print(f"rd={rd}")
    if rd.shape[0] <= 2 or rd.shape[1] <= 2:
        return np.ones(rd.shape)
    m = scale(rd, 0.0, 1.0)
    print(f"r_mask = {1-m}")
    return 1 - m


def radial_fade(a):
    mask = radial_mask(a)[:, :, np.newaxis]
    return a*mask


def main():
    img = plt.imread("painting.png")
    img_cp = img.copy()

    #print(center(img_cp))

    #a = np.zeros((3,3,3))
    #a = np.zeros((2, 2, 3))
    # a = np.zeros((1, 3, 3))

    #print((radial_distance(a)))

    #print(radial_mask(a))

    fig, axes = plt.subplots(3, 1)
    plt.gray()
    axes[0].imshow(img_cp)
    axes[1].imshow(radial_mask(img_cp))
    axes[2].imshow(radial_fade(img_cp))
    plt.show()


if __name__ == "__main__":
    main()
