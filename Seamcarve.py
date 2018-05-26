from PIL import Image
import numpy as np
def energy(im,h,w):
    '''
    Takes a picture
    Returns the engergy of each pixel
    '''
    rgb_im=im.convert('RGB')

    # initialize the RGB array
    RGBc=np.zeros((h,w),dtype=[('Red','i'),('Green','i'),('Blue','i')])
    # get RGB values of all pixels
    for i in range(w):
        for j in range(h):
            RGB=rgb_im.getpixel((i,j))
            RGBc[j][i]=RGB
    # initialize the x and y gradients
    xg=np.zeros((h,w),dtype='i')
    yg=np.zeros((h,w),dtype='i')
    # calculate x and y gradients
    for i in range(w):
        for j in range(h):
            # gradients for pixels not in the rightmost column
            r1=j; c1=i+1; r2=j; c2=i-1
            r3=j+1; c3=i; r4=j-1; c4=i
            #gradients for pixels in the rightmost column
            if c1==w:
                c1=0
            if r3==h:
                r3=0
            xg[j][i]=(RGBc[r1][c1]['Red']-RGBc[r2][c2]['Red'])**2\
            +(RGBc[r1][c1]['Blue']-RGBc[r2][c2]['Blue'])**2\
            +(RGBc[r1][c1]['Green']-RGBc[r2][c2]['Green'])**2

            yg[j][i]=(RGBc[r3][c3]['Red']-RGBc[r4][c4]['Red'])**2\
            +(RGBc[r3][c3]['Blue']-RGBc[r4][c4]['Blue'])**2\
            +(RGBc[r3][c3]['Green']-RGBc[r4][c4]['Green'])**2
    # calculate the energy, which is the sum of x- and y- gradients
    energy=xg+yg
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
    result=np.mat([[20808,52020,20808],[20808,52225,21220],[20809,52024,20809],\
    [20808,52225,21220]])
    assert np.all(energy(im,4,3)==result)
    print('Energy function works')
test_energy()


def seam_finder(im,h,w):
    '''
    Takes an image
    Returns the seam_finder
    '''
    # get the energy matrix using the energy helper function
    energy_m=energy(im,h,w)
    # initialize the costs matrix, a 2D array holding the total importance of
    # the lowest cost seam
    costs=np.zeros((h,w))
    # initialize the dirs matrix, a 2D array holding the direction of the lowest
    # cost seam
    dirs=np.zeros((h,w))
    # initialize the column index representation of the seam
    result=[0]*h
    # perform DP to fill the costs and dirs matrices
    j=h-1
    while j>0:
        j=j-1
        for i in range(w):
            if i-1>=0 and i+1<w:
                costs[j][i]=min(energy_m[j][i-1],energy_m[j][i+1],energy_m[j][i])+\
                energy_m[j+1][i]
                dirs[j][i]=np.argmin(np.array([energy_m[j][i-1],energy_m[j][i+1],energy_m[j][i]]))-1
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


def seam_remove(im,seam):
    '''
    takes an image and a list representing the position of the seam
    removes the seam from the picture
    returns the processed picture
    '''
    rgb_im=im.convert('RGB')
    h=rgb_im.size[1]
    w=rgb_im.size[0]
    result=Image.new('RGB',(w-1,h))
    for j in range(h):
        position=0
        for i in range(w):
            if seam[j]!=i:
                result.putpixel((position,j),rgb_im.getpixel((i,j)))
                position+=1
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
    assert np.all(energy(seam_remove(im,[0,0,0,0]),4,2)==energy(im_r,4,2))
    print('Seam_move works')
seam_remove_test()


def seam_carve(im,w_desired):
    '''
    takes an image and a desired width
    returns a carved image
    '''
    rgb_im=im.convert('RGB')
    h=rgb_im.size[1]
    w=rgb_im.size[0]
    while w>w_desired:
        seam=seam_finder(im,h,w)
        im=seam_remove(im,seam)
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

    im_r=Image.new('RGB',(1,4))
    im_r.putpixel((0,0),(255,101,255))
    im_r.putpixel((0,1),(255,153,255))
    im_r.putpixel((0,2),(255,205,255))
    im_r.putpixel((0,3),(255,255,255))
    assert np.all(energy(seam_carve(im,1),4,1)==energy(im_r,4,1))
    print('seam_carve works')
seam_carve_test()
