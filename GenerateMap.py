from PIL import Image

def getLevelMap(path, colors):
    image = Image.open(path)
    
    imageXW, imageYW = image.size
    
    key = {
        "WALL" : "RED",
        "START" : "BLUE",
        "WIN" : "GREEN"
    }
    
    for y in range(imageYW):
        for x in range(imageXW):
            if(image.getpixel((x,y)) == colors[key["WALL"]]):
                #print("A")
                pass