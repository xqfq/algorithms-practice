from PIL import Image
import numpy as np
def energy(im,h,w):
    '''
    Takes a picture
    Returns the engergy of each pixel
    '''
    size=h*w
    # Get RGB values of all pixels
    RGB=list([np.array(i) for i in im.getdata()])

    # Initialize the engergy array as a row vector
    energy=np.zeros(size)

    # Calculate the energy
    for i in range(size):
        first_c=(i % w == 0); last_c=((i+1) % w == 0); last_r=(i+w >= size)
        if not first_c and not last_c:
            xg=sum((RGB[i+1]-RGB[i-1])**2)
        elif first_c:
            try:
                xg=sum((RGB[i+1]-RGB[i+w-1])**2)
            except IndexError:
                xg=sum((RGB[0]-RGB[i+w-1])**2)
        else:
            xg=sum((RGB[i-1]-RGB[i-w+1])**2)

        if not last_r:
            yg=sum((RGB[i+w]-RGB[i-w])**2)
        else:
            yg=sum((RGB[i-size+w]-RGB[i-w])**2)
        energy[i]=xg+yg
    return energy

def test_energy():
    '''
    test the functionality of the energy function
    '''
    im=Image.new('RGB',(3,4))
    im.putpixel((0,0),(255,101,51))
    im.putpixel((1,0),(255,101,153))
    im.putpixel((2,0),(255,101,255))
    im.putpixel((0,1),(255,153,51))
    im.putpixel((1,1),(255,153,153))
    im.putpixel((2,1),(255,153,255))
    im.putpixel((0,2),(255,203,51))
    im.putpixel((1,2),(255,204,153))
    im.putpixel((2,2),(255,205,255))
    im.putpixel((0,3),(255,255,51))
    im.putpixel((1,3),(255,255,153))
    im.putpixel((2,3),(255,255,255))
    result=np.array([20808,52020,20808,20808,52225,21220,20809,52024,20809,\
    20808,52225,21220])

    assert np.all(energy(im,4,3)==result)
    print('Energy function works')
test_energy()

def seam_finder(im,h,w):
    '''
    Takes an image
    Returns the seam_finder
    '''
    size=h*w
    # get the energy matrix using the energy helper function
    energy_m=energy(im,h,w)
    # initialize the costs matrix, a 2D array holding the total importance of
    # the lowest cost seam
    costs=np.zeros(size)
    # initialize the dirs matrix, a 2D array holding the direction of the lowest
    # cost seam
    dirs=np.zeros(size)
    # initialize the column index representation of the seam
    result=[0]*h
    # perform DP to fill the costs and dirs matrices
    j=size-w-1
    while j>0:
        j=j-1
        if j % w !=0 and (j+1) % w !=0:
            costs[j]=min(energy_m[j+w-1],energy_m[j+w],energy_m[j+w+1])+\
            energy_m[j]
            dirs[j]=np.argmin(np.array([energy_m[j+w-1],energy_m[j+w],energy_m[j+w+1]]))-1
        elif j % w ==0:
            costs[j]=min(energy_m[j+w],energy_m[j+w+1])+\
            energy_m[j]
            dirs[j]=np.argmin(np.array([energy_m[j+w],energy_m[j+w+1]]))
        elif (j+1) % w ==0:
            costs[j]=min(energy_m[j+w-1],energy_m[j+w])+\
            energy_m[j]
            dirs[j]=np.argmin(np.array([energy_m[j+w-1],energy_m[j+w]]))-1
    costs=costs.reshape((h,w))
    dirs=dirs.reshape((h,w))
    # find the uppermost pixel of the seam
    for i in range(len(result)):
        if i==0:
            start=np.argmin(costs[0])
            result[i]=np.argmin(costs[0])
        else:
            result[i]=result[i-1]+dirs[i-1][int(result[i-1])]
    return result

def seam_finder_test():
    im=Image.new('RGB',(3,4))
    im.putpixel((0,0),(255,101,51))
    im.putpixel((1,0),(255,101,153))
    im.putpixel((2,0),(255,101,255))
    im.putpixel((0,1),(255,153,51))
    im.putpixel((1,1),(255,153,153))
    im.putpixel((2,1),(255,153,255))
    im.putpixel((0,2),(255,203,51))
    im.putpixel((1,2),(255,204,153))
    im.putpixel((2,2),(255,205,255))
    im.putpixel((0,3),(255,255,51))
    im.putpixel((1,3),(255,255,153))
    im.putpixel((2,3),(255,255,255))
    result=[0,0,0,0]
    assert seam_finder(im,4,3)==result
    print('Seam_finder works')
seam_finder_test()

def seam_remove(im,seam,h,w):
    '''
    takes an image and a list representing the position of the seam
    removes the seam from the picture
    returns the processed picture
    '''
    # Get the RGB array
    RGB=np.array(im.getdata(),dtype=np.uint8).reshape((h,w,3))
    # Remove the seam by bool indexing
    RGB=RGB[np.array(seam).reshape(h,1)!=np.arange(w)].reshape((h,w-1,3))
    result = Image.fromarray(RGB,'RGB')
    return result

def seam_remove_test():
    im=Image.new('RGB',(3,4))
    im.putpixel((0,0),(255,101,51))
    im.putpixel((1,0),(255,101,153))
    im.putpixel((2,0),(255,101,255))
    im.putpixel((0,1),(255,153,51))
    im.putpixel((1,1),(255,153,153))
    im.putpixel((2,1),(255,153,255))
    im.putpixel((0,2),(255,203,51))
    im.putpixel((1,2),(255,204,153))
    im.putpixel((2,2),(255,205,255))
    im.putpixel((0,3),(255,255,51))
    im.putpixel((1,3),(255,255,153))
    im.putpixel((2,3),(255,255,255))
    im_r=Image.new('RGB',(2,4))
    im_r.putpixel((0,0),(255,101,153))
    im_r.putpixel((1,0),(255,101,255))
    im_r.putpixel((0,1),(255,153,153))
    im_r.putpixel((1,1),(255,153,255))
    im_r.putpixel((0,2),(255,204,153))
    im_r.putpixel((1,2),(255,205,255))
    im_r.putpixel((0,3),(255,255,153))
    im_r.putpixel((1,3),(255,255,255))
    assert np.all(energy(seam_remove(im,[0,0,0,0],4,3),4,2)==energy(im_r,4,2))
    print('Seam_remove works')
seam_remove_test()

def seam_carve(im,w_desired):
    '''
    takes an image and a desired width
    returns a carved image
    '''
    rgb_im=im.convert('RGB')
    h=rgb_im.size[1]
    w=rgb_im.size[0]
    # Remove seams untile the desired width is reached
    while w>w_desired:
        seam=seam_finder(im,h,w)
        im=seam_remove(im,seam,h,w)
        w=w-1
    return im

def seam_carve_test():
    im=Image.new('RGB',(3,4))
    im.putpixel((0,0),(255,101,51))
    im.putpixel((1,0),(255,101,153))
    im.putpixel((2,0),(255,101,255))
    im.putpixel((0,1),(255,153,51))
    im.putpixel((1,1),(255,153,153))
    im.putpixel((2,1),(255,153,255))
    im.putpixel((0,2),(255,203,51))
    im.putpixel((1,2),(255,204,153))
    im.putpixel((2,2),(255,205,255))
    im.putpixel((0,3),(255,255,51))
    im.putpixel((1,3),(255,255,153))
    im.putpixel((2,3),(255,255,255))
    output=seam_carve(im,1)
    im_r=Image.new('RGB',(1,4))
    im_r.putpixel((0,0),(255,101,255))
    im_r.putpixel((0,1),(255,153,255))
    im_r.putpixel((0,2),(255,205,255))
    im_r.putpixel((0,3),(255,255,255))

    assert np.all(energy(output,4,1)==energy(im_r,4,1))
    print('seam_carve works')
seam_carve_test()
