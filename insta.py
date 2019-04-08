import cv2
import numpy as np

#helpers
def truncate(n):
    return 0 if (n<0) else 255 if (n>255) else n

def max(a,b,c):
    return a if (a >= b and a >= c) else c if (c >= b and c>= a) else b

def min(a,b,c):
    return a if (a <= b and a <= c) else c if (c <= b and c<= a) else b

#filters
def inkwell(img):
    #brighter than default grey
    img_size = img.shape
    new_img = np.zeros(img_size, img.dtype)
    r,c = 0,0
    while(r<img_size[0]):
        while(c<img_size[1]):
            bl = img[r][c][0]
            gr = img[r][c][1]
            rd = img[r][c][2]
            max_v = max(bl,gr,rd)
            new_img[r][c]=[max_v,max_v,max_v]
            # 
            c=c+1
        # 
        r = r+1
        c =0
    # print(new_img)
    return new_img

def gotham(img):
    #brighter than default grey
    img_size = img.shape
    new_img = np.zeros(img_size, img.dtype)
    r,c = 0,0
    while(r<img_size[0]):
        while(c<img_size[1]):
            bl = img[r][c][0]
            gr = img[r][c][1]
            rd = img[r][c][2]
            min_v = min(bl,gr,rd)
            new_img[r][c]=[min_v,min_v,min_v]
            # 
            c=c+1
        # 
        r = r+1
        c =0
    # print(new_img)
    new_img = lo_fi(new_img)
    return new_img

def lo_fi(img):
    #high contrast
    img_size = img.shape
    new_img = np.zeros(img_size, img.dtype)
    r,c = 0,0
    while(r<img_size[0]):
        while(c<img_size[1]):
            bl = img[r][c][0]
            gr = img[r][c][1]
            rd = img[r][c][2]
            alpha = 1.5
            new_bl = truncate(alpha*(bl-128)+128)
            new_gr = truncate(alpha*(gr-128)+128)
            new_rd = truncate(alpha*(rd-128)+128)
            new_img[r][c]=[new_bl,new_gr,new_rd]
            # 
            c=c+1
        # 
        r = r+1
        c =0
    # print(new_img)
    return new_img

def lilly(img):
    new_img = np.zeros(img.shape, img.dtype)
    new_img[:,:,1] = 220
    new_img[:,:,2] = 170
    new_img[:,:,0] = 10 #blue
    new_img = cv2.addWeighted(img,0.8,new_img,0.2,0)
    brown = np.zeros(img.shape, img.dtype)
    brown[:,:,2] = 255
    brown[:,:,1] = 170
    brown[:,:,0] = 0
    new_img = cv2.addWeighted(brown,0.2,new_img,0.8,0)
    return new_img

def pro_procket(img):
    new_img = np.zeros(img.shape, img.dtype)
    new_img[:,:,1] = 0 #g
    new_img[:,:,2] = 255 #r
    new_img[:,:,0] = 0 #blue
    new_img = cv2.addWeighted(img,0.9,new_img,0.4,0)
    # brown = np.zeros(img.shape, img.dtype)
    # brown[:,:,2] = 255
    # brown[:,:,1] = 170
    # brown[:,:,0] = 0
    # new_img = cv2.addWeighted(brown,0.2,new_img,0.8,0)
    return new_img


def main():
    print ("Hello to my insta_like filters :D")
    print ("photo should be named <insta_test.jpg>")
    img = cv2.imread("insta_test.jpg")
    filters = "[lilly | gotham | lo-fi | proprocket | inkwell]"
    # print ("I support "+filters)
    while (1):
        print ("\nwrite a filter name or <q> to close")
        print ("filters supported: "+filters)
        filter = input()
        if (filter == "lilly"):
            out = lilly(img)
        elif(filter == "gotham"):
            out = gotham(img)
        elif(filter == "lo-fi"):
            out = lo_fi(img)
        elif(filter == "proprocket"):
            out = pro_procket(img)
        elif(filter == "inkwell"):
            out = inkwell(img)
        elif(filter == 'q'):
            return
        else:
            print("wrong input!!")
            continue
        cv2.imshow("orig",img)
        cv2.imshow(filter,out)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

main()