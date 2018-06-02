im = imread('images\cross.pgm');
im_pad = padarray(im,[28 28],'both');
oriShift = fftshift(fft2(im_pad));
PhaseSpec = angle(oriShift);
amplitude = abs(oriShift)+1;
logAmp = log(amplitude);
GrayAmp = mat2gray(logAmp);
imshow([GrayAmp PhaseSpec]);