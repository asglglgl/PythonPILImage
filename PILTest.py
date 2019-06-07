from PIL import Image
import numpy as np


def ImageCovedrtHandDraw(a):
    '''
    将图片转换为手绘图片
    :param a: ndarray 原图片的ndarray
    :return:
    '''
    depth = 10
    grad = np.gradient(a)               #取图像灰度的梯度值
    grad_x ,grad_y = grad               #分别取横纵图像梯度值
    grad_x = grad_x*depth/100
    grad_y = grad_y*depth/100
    A = np.sqrt(grad_x**2+grad_y**2+1.)
    uni_x = grad_x /A
    uni_y = grad_y/A
    uni_z = 1. / A

    vec_el = np.pi/2.2                  #光源的俯视角度 弧度值
    vec_az = np.pi/4.                   #光源的方位角度，弧度值
    dx = np.cos(vec_el)*np.cos(vec_az)  #光源对X轴的影响
    dy = np.cos(vec_el)*np.cos(vec_az)  #光源对Y轴的影响
    dz = np.sin(vec_el)                 #光源对Z轴的影响

    b = 255*(dx*uni_x+dy*uni_y+dz*uni_z)
    b = b.clip(b)

    im = Image.fromarray(b.astype('uint8'))
    im.save("z1.jpg")
'''
用PIL的Image  通过修改图片的rgb值 实现图片的变化
'''
img = np.array(Image.open("x.jpg").convert('L')).astype('float')
ImageCovedrtHandDraw(img)

