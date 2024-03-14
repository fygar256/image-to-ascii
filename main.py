from PIL import Image
import sys

class Main:
    def __init__(self, path, r=50):
        image = Image.open(path)
        width, height = image.size
        image = image.resize((width//r, height//r))
        self.image = image.convert("L")

    def eval_with_threshold(value,threshold):
        return 0 if value<=threshold else 1

    def pxl_to_ascii(self, pixel_value,pixel_value2,threshold):
        ascii_chars = ' .\':'
        char_index = Main.eval_with_threshold(1 - pixel_value / 255,threshold )
        char_index2 = Main.eval_with_threshold(1 - pixel_value2 / 255,threshold )
        return ascii_chars[(char_index)*2+char_index2]

    def convert(self,threshold=0.5):
        ascii_txt = ""
        width, height = self.image.size
        for h in range(0,height-1,2):
            for w in range(width):
                pxl_value = self.image.getpixel((w, h))
                pxl_value2= self.image.getpixel((w,h+1))
                ascii_txt += self.pxl_to_ascii(pxl_value,pxl_value2,threshold)
            ascii_txt += "\n"
        return ascii_txt

if __name__ == "__main__":
    r=5
    threshold=0.6
    if len(sys.argv)==1:
        print("Usage python3 main.py picturefile [ shrinkscale [ threshold ] ]")
    if len(sys.argv)==3:
        r=int(sys.argv[2])
    if len(sys.argv)==4:
        r=int(sys.argv[2])
        threshold=float(sys.argv[3])

    to_ascii = Main(sys.argv[1], r)
    result = to_ascii.convert(threshold)
    print(result)
