from PIL import Image, ImageChops, ImageDraw

class ImageCompare:
    def comparison(self, baseline_data, actual_image):
        baseline = Image.open(baseline_data).convert('RGB')
        actual = Image.open(actual_image).convert('RGB')
        diff = ImageChops.difference(baseline, actual)
        diff = diff.point(lambda i: i * 4)

        diff_pixels = sum(1 for pixel in diff.getdata() if pixel != (0, 0, 0))
        total_pixels = baseline.size[0] * baseline.size[1]
        difference_percentage = (diff_pixels / total_pixels) * 100

        return diff, difference_percentage
