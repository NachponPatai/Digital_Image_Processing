im = imread('images\lenna.pgm');
oriShift = fftshift(fft2(im));
PhaseSpec = angle(oriShift);
PhaseiFFT = abs(ifft2(ifftshift(PhaseSpec)));
GrayPhase = mat2gray(PhaseiFFT);
amplitude = abs(oriShift);
AmpiFFT = ifft2(ifftshift(amplitude));
GrayAmp = mat2gray(AmpiFFT);
imshow([GrayAmp,GrayPhase]);