import argparse

import imageprocessor as ip

def parse_arguments() -> tuple[str, float, float, str]:
    """
    Parses the image filename, height and width of the image, the name of the directory
    where the modified image will be saved.
    :return: The tuple of parsed data
    """
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('input_name', type=str, help='input_name')
    argument_parser.add_argument('height', type=int, help='height')
    argument_parser.add_argument('width', type=int, help='width')
    argument_parser.add_argument('output_name', type=str, help='output_name')
    args = argument_parser.parse_args()
    return args.input_name, args.height, args.width, args.output_name

def main() -> None:
    try:
        input_file, height, width, output_file = parse_arguments()

        img = ip.fetch_image(input_file)

        ip.show_image_dimensions(img)

        hist = ip.compute_histogram(img)
        ip.draw_histograms(hist)

        resized = ip.adjust_size(img, width, height)

        ip.show_side_by_side(img, resized)

        ip.save_image(resized, output_file)

    except Exception as exc:
        print("Error:", exc)

if __name__ == "__main__":
    main()
