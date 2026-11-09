"""Classical multi-scale Retinex with colour restoration (MSRCR)."""

import argparse

import cv2
import numpy as np


def ssr(channel: np.ndarray, sigma: float) -> np.ndarray:
    blur = cv2.GaussianBlur(channel, (0, 0), sigma)
    return np.log10(channel + 1.0) - np.log10(blur + 1.0)


def msrcr(image: np.ndarray, sigmas=(15, 80, 250), gain=5.0, offset=25.0) -> np.ndarray:
    img = image.astype(np.float32) + 1.0
    msr = np.zeros_like(img)
    for sigma in sigmas:
        msr += ssr(img, sigma) / len(sigmas)
    restored = gain * msr + offset
    restored = np.clip(restored, 0, 255)
    return restored.astype(np.uint8)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--out", default="msrcr.png")
    args = parser.parse_args()
    image = cv2.imread(args.image)
    result = msrcr(image)
    cv2.imwrite(args.out, result)


if __name__ == "__main__":
    main()
