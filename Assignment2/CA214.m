im = imread('images\cross.pgm');
resize = imresize(im,0.5);
oriShift = fftshift(fft2(im));
PhaseSpec = angle(oriShift);
amplitude = abs(oriShift)+1;
logAmp = log(amplitude);
GrayAmp = mat2gray(logAmp);
imshow([GrayAmp,PhaseSpec]);