import cv2
import glob
import skimage.io as io

# ======================================================================================================================
# ======================================================================================================================

def leason_1():

    img = cv2.imread(filename="./image.jpg", flags=cv2.IMREAD_COLOR)
    """
    imread (filename, flags) :read an image from a file.
    inputs :
        filename : Name of the file.
        flags : Flag for image color space. 
            {cv2.IMREAD_COLOR : Loads a color image.
            cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode.
            cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel.}

    outputs :
        img : image read from the file.

    """

    cv2.imshow("Image", img)
    """
    imshow (winname, img) :show an image in a window.
    inputs :
        winname : Name of the window.
        img : image to be shown.

    outputs :
        None

    """

    cv2.waitKey()
    """
    waitKey () :wait for a key to be pressed.
    inputs :
        delay : Time in milliseconds.

    outputs :
        key : Key pressed.

    """

    cv2.destroyAllWindows()
    """
    destroyAllWindows () :destroy all the windows.
    inputs :
        None

    outputs :
        None

    """

# ======================================================================================================================
# ======================================================================================================================

def leason_2():

    img = cv2.imread(filename="./image.jpg", flags=cv2.IMREAD_COLOR)
    cv2.imshow("Image", img)
    key = cv2.waitKey()
    if key == ord('q'):
        """
        check if the key pressed is 'q'
        ord(character) : return the ASCII value of the character.
        """
        cv2.waitKey(500)
        cv2.destroyAllWindows()
        cv2.imwrite(filename="./image_copy.jpg", img=img)
        """
        imwrite (filename, img) :write an image to a file.
        inputs :
            filename : Name of the file.
            img : image to be written.

        outputs :
            None
        """
    elif key == 27:
        """
        check if the key pressed is 'esc'
        27 : ASCII value of 'esc'
        """
        cv2.destroyAllWindows()

# ======================================================================================================================
# ======================================================================================================================

def leason_3():

    img = cv2.imread(filename="./image.jpg", flags=cv2.IMREAD_COLOR)
    cv2.namedWindow(winname="Image", flags=cv2.WINDOW_NORMAL)
    """
    namedWindow (winname, flags) :create a window with the given name.
    inputs :
        winname : Name of the window.
        flags : Flag for window creation.
            {cv2.WINDOW_NORMAL : Window size is adjusted by user.
            cv2.WINDOW_AUTOSIZE : Window size is adjusted automatically and can't change by user.}

    outputs :
    None
    """
    cv2.imshow("Image", img)
    key = cv2.waitKey(0)
    if key == ord('c'):
        cv2.setWindowTitle(winname="Image", title="Image2")
        """
        setWindowTitle (winname, title) :set the title of the window.
        inputs :
            winname : Name of the window.
            title : New title of the window.

        outputs :
            None
        """
        cv2.resizeWindow(winname="Image", width=500, height=500)
        """
        resizeWindow (winname, width, height) :resize the window.
        inputs :
            winname : Name of the window.
            width : New width of the window.
            height : New height of the window.

        outputs :
            None
        """
        cv2.moveWindow(winname="Image", x=100, y=100)
        """
        moveWindow (winname, x, y) :move the window.
        inputs :
            winname : Name of the window.
            x : New x-coordinate of the window.
            y : New y-coordinate of the window.

        outputs :
            None    
        """
        cv2.waitKey(2000)

    cv2.destroyAllWindows()

# ======================================================================================================================
# ======================================================================================================================

def leason_4():
    """
    Read many images .
    """
    img_paths = glob.glob("./*.jpg")
    for img_path in img_paths:
        img = cv2.imread(filename=img_path, flags=cv2.IMREAD_COLOR)
        cv2.imshow("Image", img)
        key = cv2.waitKey(2000)
    cv2.destroyAllWindows()

# ======================================================================================================================
# ======================================================================================================================        
    
def leason_5():
    """
    Read many images with sklearn.io .
    """
    imgs = io.imread_collection("./*.jpg")
    """
    imread_collection (filenames, **kwargs) :read a collection of images.
    inputs :
        filenames : List of image filenames.
        kwargs : Keyword arguments passed to imread.

    outputs :
        imgs : List of images.
    """
    for img in imgs:
        cv2.imshow("Image", img)
        key = cv2.waitKey(2000)
    cv2.destroyAllWindows()


def leason_6():
    
    img = cv2.imread(filename="./image.jpg", flags=cv2.IMREAD_COLOR)
    color_spaces = [cv2.COLOR_BGR2RGB,
                    cv2.COLOR_BGR2GRAY,
                    cv2.COLOR_BGR2HSV,
                    cv2.COLOR_BGR2HLS,
                    cv2.COLOR_BGR2YUV,
                    cv2.COLOR_BGR2YCrCb,
                    cv2.COLOR_BGR2Lab,
                    cv2.COLOR_BGR2Luv,
                    cv2.COLOR_BGR2XYZ, 
                    ]
    titles = ["RGB",
            "GRAY",
            "HSV",
            "HLS",
            "YUV",
            "YCrCb",
            "Lab",
            "Luv",
            "XYZ",
            ]
   
    for i in range(len(color_spaces)+1):
        if i == 0:
            cv2.imshow("Image", img)
            cv2.waitKey(2000)
        else:
            cv2.setWindowTitle("Image", titles[i-1])
            img_color_space = cv2.cvtColor(src=img, code=color_spaces[i-1])
            """
            cvtColor (src, code) :convert an image from one color space to another.
            inputs :
                src : Source image.
                code : Color space conversion code.
                    {cv2.COLOR_BGR2RGB : Convert a BGR image to RGB.
                    cv2.COLOR_BGR2GRAY : Convert a BGR image to grayscale.
                    cv2.COLOR_BGR2HSV : Convert a BGR image to HSV.
                    cv2.COLOR_BGR2HLS : Convert a BGR image to HLS.
                    cv2.COLOR_BGR2YUV : Convert a BGR image to YUV.
                    cv2.COLOR_BGR2YCrCb : Convert a BGR image to YCrCb.
                    cv2.COLOR_BGR2Lab : Convert a BGR image to Lab.
                    cv2.COLOR_BGR2Luv : Convert a BGR image to Luv.
                    cv2.COLOR_BGR2XYZ : Convert a BGR image to XYZ.}

            outputs :
                dst : Destination image.
            """
            cv2.imshow("Image", img_color_space)
            key = cv2.waitKey(2000)
    cv2.destroyAllWindows()

# ======================================================================================================================
# ======================================================================================================================

def leason_7():
    """
    Access to pixel and chhange it.
    """
    img = cv2.imread(filename="./image.jpg", flags=cv2.IMREAD_COLOR)
    px = img[100, 100]
    """
    px = img[y, x] :access to pixel.
    inputs :
        img : Source image.
        y : y-coordinate of pixel.
        x : x-coordinate of pixel.

    outputs :
        px : Pixel value.
    """
    print(px)
    img[100:150, 100:150] = [255, 255, 255]
    """
    img[y, x] = [b, g, r] :change pixel.
    inputs :
        b : Blue value of pixel.
        g : Green value of pixel.
        r : Red value of pixel.

    outputs :
        None
    """
    cv2.imshow("Image", img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

# ======================================================================================================================
# ======================================================================================================================

def leason_8():
    """
    Get image details.
    """
    img = cv2.imread(filename="./image.jpg", flags=cv2.IMREAD_COLOR)
    print("Image Dimensions : ", img.shape)
    print("Image Channels : ", img.shape[2])
    print("Image Resolution : ", (img.shape[0], img.shape[1]))
    print("Total sub_pixels : ", img.size)
    print("Total pixels : ", img.size / 3)
    print("Image Data Type : ", img.dtype)

# ======================================================================================================================
# ======================================================================================================================

def leason_9():
    """
    Use Webcam.
    """
    cam = cv2.VideoCapture(0)
    """
    VideoCapture (device_id) :create a VideoCapture object.
    inputs :
        device_id : Device ID of the camera.

    outputs :
        cap : VideoCapture object.
    """
    while True:
        ret, frame = cam.read()
        """
        cam.read (self) :read a single frame.
            inputs :
            self : VideoCapture object.

        outputs :
            ret : True if frame is read correctly (Boolean).
            frame : frame read from the camera.
        """
        if ret:
            cv2.imshow("frame", frame)
            key = cv2.waitKey(2000)
        if key == 27:
            break
    cam.release()
    """
    cam.release (self) :release the VideoCapture object.
    inputs :
        self : VideoCapture object.
    
    outputs :
        None
    """
    cv2.destroyAllWindows()

# ======================================================================================================================
# ======================================================================================================================

def leason_10():
    cam = cv2.VideoCapture(0)

    fourCC = cv2.VideoWriter_fourcc(*'XVID')
    """
    VideoWriter_fourcc (codec) :create a VideoWriter_fourcc object.
    inputs :
        codec : Codec of the video.
            {'DIVX' : DivX codec.
            'XVID' : Xvid codec.
            'MJPG' : Motion JPEG codec.
            'X264' : H.264 codec.
            'WMV1' : Windows Media Video 7.
            'WMV2' : Windows Media Video 8.
            'DV' : DV codec.
            'MPEG' : MPEG-1 codec.
            'MPEG2' : MPEG-2 codec.
            'MPEG4' : MPEG-4 codec.
            'H264' : H.264 codec.
            'H263' : H.263 codec.
            'H261' : H.261 codec.}

    outputs :
        fourCC : VideoWriter_fourcc object.
    """
    save = cv2.VideoWriter(filename="./video.avi", fourcc=fourCC, fps=30, frameSize=(640, 480))
    """
    VideoWriter (filename, fourcc, fps, frameSize) :create a VideoWriter object.
    inputs :
        filename : Name of the output video file.
        fourcc : Codec of the video.
        fps : Frames per second (int).
        frameSize : Size of the video frames.

    outputs :
        save : VideoWriter object.
    """
    recorde = False
    
    if cam.isOpened() == False:
        """
         cam.isOpened (self) :check if the VideoCapture object is opened.
        inputs :
            self : VideoCapture object.

        outputs :
            True if the VideoCapture object is opened (Bolean).
        """
        print("Camera is not opened.")
        cam.open(0)
        """
        cam.open (self, device_id) :open a VideoCapture object.
        inputs :
            self : VideoCapture object.
            device_id : Device ID of the camera.

        outputs :
            None
        """
    else:
        while cam.isOpened():
            key = cv2.waitKey(0)
            if key == 27:
                break
            elif key == ord('r'):
                recorde = not recorde
                _, frame = cam.read()
                cv2.imshow("frame", frame)

                if recorde:
                    save.write(frame)
                    """
                    save.write (self, frame) :write a frame to the video file.
                    inputs :
                        self : VideoWriter object.
                        frame : frame to write.

                    outputs :
                        None
                    """
    cam.release()
    save.release()
    cv2.destroyAllWindows()

# ======================================================================================================================
# ======================================================================================================================

def leason_11():
    """
    Get movie details.
    """
    cam = cv2.VideoCapture(0)
    print("Resolution : ", cam.get(cv2.CAP_PROP_FRAME_WIDTH), cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    """
    cam.get (self, propId) :get the specified property of video capturing.
    inputs :
        self : VideoCapture object.
        propId : Property ID.
            {'CAP_PROP_POS_MSEC' : Current position of the video file in milliseconds (ID = 0).
            'CAP_PROP_POS_FRAMES' : 0-based index of the frame to be decoded/captured next (ID = 1).
            'CAP_PROP_POS_AVI_RATIO' : Relative position of the video file (ID = 2).
            'CAP_PROP_FRAME_WIDTH' : Width of the frames in the video stream (ID = 3).
            'CAP_PROP_FRAME_HEIGHT' : Height of the frames in the video stream (ID = 4).
            'CAP_PROP_FPS' : Frame rate (ID = 5).
            'CAP_PROP_FOURCC' : 4-character code of codec (ID = 6).
            'CAP_PROP_FRAME_COUNT' : Number of frames in the video file (ID = 7).
            'CAP_PROP_FORMAT' : Format of the Mat objects returned by retrieve() (ID = 8).
            'CAP_PROP_MODE' : Backend-specific value indicating the current capture mode (ID = 9).
            'CAP_PROP_BRIGHTNESS' : Brightness of the image (ID = 10).
            'CAP_PROP_CONTRAST' : Contrast of the image (ID = 11).
    
    outputs :
        value : Value of the property.
    """
    print("FPS : ", cam.get(cv2.CAP_PROP_FPS))
    cam.release()

# ======================================================================================================================
# ======================================================================================================================




if __name__ == '__main__':
    leason_8()
    