im = imread('images\cross.pgm');
rotate = imrotate(im,30,'bilinear');
im_pad = padarray(rotate,[28 28],'both');
oriShift = fftshift(fft2(im_pad));
PhaseSpec = angle(oriShift);
amplitude = abs(oriShift)+1;
logAmp = log(amplitude);
GrayAmp = mat2gray(logAmp);
imshow([GrayAmp,PhaseSpec]);