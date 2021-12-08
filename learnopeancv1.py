import cv2
import numpy as np

def leason_1():
    paper = np.ones((480, 640, 3), np.uint8) 
    paper[:,20:100] = 255
    paper[200:280,280:360] = [0,255,0]
    paper[:,540:620] = 255

    cv2.imshow('paper', paper)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# =============================================================================
# =============================================================================

def leason_2():
    x = np.array([1,4,65,345,246,7856,135,768,-12])
    minval , maxval , minloc , maxloc = cv2.minMaxLoc(x)
    """
    cv2.minMaxLoc(array): returns the minimum and maximum and the location of the minimum and maximum values in the array x.
    input:
        array: input array.

    output:
        minval: minimum value in the array.
        maxval: maximum value in the array.
        minloc: location of the minimum value in the array.
        maxloc: location of the maximum value in the array.
    """
    print(minval, maxval, minloc, maxloc)

# =============================================================================
# =============================================================================

def leason_3():
    """
    attach two image horizontally and vertically
    """
    img1 = cv2.imread("./image.jpg")
    img2 = cv2.imread("./image_copy.jpg")

    attach = np.hstack((img1, img2))
    """
    np.hstack(tup): horizontally stack arrays in sequence.
    input:
        tup: tuple of input arrays.
    
    output:
        out: horizontally stacked array.
    """
    cv2.imshow('horizontally', attach)

    attach = np.vstack((img1, img2))
    """
    np.vstack(tup): vertically stack arrays in sequence.
    input:
        tup: tuple of input arrays.

    output:
        out: vertically stacked array.
    """
    cv2.imshow('vertically', attach)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# =============================================================================
# =============================================================================

def leason_4():
    
    img = cv2.imread("./image.jpg")
    B, G, R = cv2.split(img)
    """
    cv2.split(src): splits an image into three single channel images.
    input:
        src: input image.
    
    output:
        B: blue channel.
        G: green channel.
        R: red channel.
    """
    cv2.imshow('blue', B)
    cv2.imshow('green', G)
    cv2.imshow('red', R)
    newimg = cv2.merge((B, G, R))
    """
    cv2.merge(tup): merges three single channel images into a single multi-channel image.
    input:
        tup: tuple of input arrays.
    
    output:
        out: merged image.
    """
    cv2.imshow('merged', newimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# =============================================================================
# =============================================================================

def leason_5():
    img = cv2.imread("./image.jpg")
    fliped = cv2.flip(img, 1)
    """
    cv2.flip(src, flipCode): flips an image vertically or horizontally.
    input:
        src: input image.
        flipCode: 0: flip horizontally, 1: flip vertically, -1: flip both.
    
    output:
        out: flipped image.
    """
    cv2.imshow('fliped1', fliped)
    fliped = cv2.flip(img, 0)
    cv2.imshow('fliped2', fliped)
    fliped = cv2.flip(img, -1)
    cv2.imshow('fliped3', fliped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# =============================================================================
# =============================================================================

def leason_6():
    img1 = cv2.imread("./image.jpg")
    img2 = cv2.imread("./bat.jpg")
    img1 = cv2.resize(img1, (448*2,448))
    img2 = cv2.resize(img2, (448*2,448))

    mixed = cv2.addWeighted(img1, 0.7, img2, 0.3, 0.1)
    """
    cv2.addWeighted(src1, alpha, src2, beta, gamma): adds two images with specific weight.
    input:
        src1: first input image.
        alpha: weight of the first image.
        src2: second input image.
        beta: weight of the second image.
        gamma: added value.

    output:
        out: added image.
    """
    cv2.imshow('mixed', mixed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# =============================================================================
# =============================================================================

def leason_7():
    a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    inranage = cv2.inRange(a, 2, 6)
    """
    cv2.inRange(src, lowerb, upperb): computes a binary image which is set to 255 (white) in case of the pixel value is in the range [lowerb, upperb] and 0 (black) otherwise.
    input:
        src: input array.
        lowerb: lower boundary of the range.
        upperb: upper boundary of the range.
    
    output:
        out: binary image.
    """
    print(inranage)

# =============================================================================
# =============================================================================

def leason_8():
    a = np.array([0,1,0,1])
    b = np.array([0,0,1,1])

    AND = cv2.bitwise_and(a, b)
    """
    cv2.bitwise_and(src1, src2): computes AND operator of two arrays or images.
    input:
        src1: first input array or image.
        src2: second input array or image.

    output:
        out: AND of two arrays or images.
    """
    OR = cv2.bitwise_or(a, b)
    """
    cv2.bitwise_or(src1, src2): computes OR operator of two arrays or images.
    input: 
        src1: first input array or image.
        src2: second input array or image.
    
    output:
        out: OR of two arrays or images.
    """
    XOR = cv2.bitwise_xor(a, b)
    """
    cv2.bitwise_xor(src1, src2): computes XOR operator of two arrays or images.
    input:
        src1: first input array or image.
        src2: second input array or image.
    
    output:
        out: XOR of two arrays or images.
    """
    NOT = cv2.bitwise_not(a)
    """
    cv2.bitwise_not(src): inverts each bit of array.
    input:
        src: input array.
    
    output:
        out: inverted array.
    """
    print(AND)
    print(OR)
    print(XOR)
    print(NOT)


if __name__ == '__main__':
    leason_8()