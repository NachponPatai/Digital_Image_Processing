im = imread('images\cross.pgm');
oriShift = fftshift(fft2(im));
x = -100:99;
y = -100:99;
[x,y] = meshgrid(x,y);
ComplexNumber = exp(-2i*pi*(((20*x)./200) + ((30*y)./200)));
PhaseiFFT = ifft2(ifftshift(ComplexNumber.*oriShift));
imshow([im,PhaseiFFT]);