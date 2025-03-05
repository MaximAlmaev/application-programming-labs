import cv2
import matplotlib.pyplot as plt
import numpy as np

def fetch_image(file_name: str) -> np.ndarray:
    """
    Retrieves the image from the specified path, raises an error if the image file cannot be found.
    :param file_name: The path to the image.
    :return: The image as np.ndarray
    """
    image = cv2.imread(file_name)
    if image is None:
        raise FileNotFoundError("Image not found!")
    return image

def show_image_dimensions(image: np.ndarray) -> None:
    """
    Prints the dimensions of the image in pixels.
    :param image: The image as np.ndarray
    :return: None
    """
    print(f"Height: {image.shape[0]}, Width: {image.shape[1]}")

def compute_histogram(image: np.ndarray) -> dict:
    """
    Computes the histogram for a grayscale image, or
    computes brightness and color histograms for a color image.
    :param image: The image in the form of np.ndarray
    :return: A dictionary with brightness and color histograms.
    """
    histogram_dict = {}
    if len(image.shape) == 2:  # Grayscale image
        histogram_dict['gray'] = cv2.calcHist([image], [0], None, [256], [0, 256])
    else:  # Color image
        channel_colors = ('b', 'g', 'r')
        for index, color in enumerate(channel_colors):
            histogram_dict[color] = cv2.calcHist([image], [index], None, [256], [0, 256])
    return histogram_dict

def draw_histograms(histogram_dict: dict) -> None:
    """
    Displays the brightness histogram and the color histograms.
    :param histogram_dict: A dictionary with brightness and color histograms.
    :return: None
    """
    if any(color in histogram_dict for color in ('b', 'g', 'r')):  # Color histograms
        for color in ('b', 'g', 'r'):
            if color in histogram_dict:
                plt.plot(histogram_dict[color], color=color, label=f'Channel {color.upper()}')
        plt.title('Color Histogram')
        plt.xlim([0, 256])
        plt.xlabel('Intensity')
        plt.ylabel('Pixel Count')
        plt.legend()
    plt.tight_layout()
    plt.show()

def adjust_size(image: np.ndarray, new_width: int, new_height: int) -> np.ndarray:
    """
    Adjusts the size of the image.
    :param image: The original image as np.ndarray
    :param new_width: The width of the image in pixels
    :param new_height: The height of the image in pixels
    :return: np.ndarray of the resized image.
    """
    dimensions = (new_width, new_height)
    resized_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_CUBIC)
    return resized_image

def show_side_by_side(original: np.ndarray, modified: np.ndarray) -> None:
    """
    Displays two images in two separate windows simultaneously.
    :param original: np.ndarray of the first image.
    :param modified: np.ndarray of the second image.
    :return: None
    """
    if original is None:
        raise ValueError("Error: Original image not found.")
    elif modified is None:
        raise ValueError("Error: Modified image not found.")
    else:
        cv2.imshow("Original", original)
        cv2.imshow("Modified", modified)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def save_image(image: np.ndarray, output_path: str) -> None:
    """
    Saves the provided image, raises an error if the image could not be saved.
    :param image: np.ndarray of the image to be saved.
    :param output_path: The path where the image will be saved.
    :return: None
    """
    result = cv2.imwrite(output_path, image)
    if not result:
        raise IOError(f"Could not save image to {output_path}.")