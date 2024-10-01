from PIL import Image, ImageChops, ImageOps

class image_compare():
    
    def comparison(self, baseline_data, actual_image, threshold):
        baseline = Image.open(baseline_data)
        actual = Image.open(actual_image)
        
        diff = ImageChops.difference(baseline, actual)
        num_different_pixels = sum(1 for pixel in diff.getdata() if pixel != (0, 0, 0))
        total_pixels = baseline.size[0] * baseline.size[1]
        
        if total_pixels > 0:
            difference_percentage = 100 - ((num_different_pixels / (total_pixels) *100)) 
        else:
            difference_percentage = 100.0

        print(f"Percent difference: {difference_percentage:.2f}%")

        if difference_percentage < threshold:  
            diff_gray = diff.convert("L")
            diff_highlighted = ImageOps.colorize(diff_gray, black="black", white="white")
            return diff_highlighted, difference_percentage
        else:
            return None
