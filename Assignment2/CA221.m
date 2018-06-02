im = imread('images\Cross.pgm');
[x,y] = size(im);
centerx = (x-1)/2;
centery = (y-1)/2;
[u,v] = meshgrid(-centerx:centerx,-centery:centery);
oriShift = fftshift(fft2(im));
D = sqrt(u.^2 + v.^2);

freqcutoff1 = 20;
freqcutoff2 = 50;
freqcutoff3 = 100;

ideal20 = ifft2(ifftshift(double(D <= freqcutoff1).*oriShift));
ideal50 = ifft2(ifftshift(double(D <= freqcutoff2).*oriShift));
ideal100 = ifft2(ifftshift(double(D <= freqcutoff3).*oriShift));

figure('Name','Ideal');
subplot(2,2,1);
imshow(im);
subplot(2,2,2);
imshow(real(ideal20),[]);
subplot(2,2,3);
imshow(real(ideal50),[]);
subplot(2,2,4);
imshow(real(ideal100),[]);

guass20 = ifft2(ifftshift(double(exp(-(D.^2./(2.*freqcutoff1.^2)))).*oriShift));
guass50 = ifft2(ifftshift(double(exp(-(D.^2./(2.*freqcutoff2.^2)))).*oriShift));
guass100 = ifft2(ifftshift(double(exp(-(D.^2./(2.*freqcutoff3.^2)))).*oriShift));

figure('Name','Guass');
subplot(2,2,1);
imshow(im);
subplot(2,2,2);
imshow(real(guass20),[]);
subplot(2,2,3);
imshow(real(guass50),[]);
subplot(2,2,4);
imshow(real(guass100),[]);


n = 2;
btw20 = ifft2(ifftshift(double(1./(1+(D./freqcutoff1).^2*n)).*oriShift));
btw50 = ifft2(ifftshift(double(1./(1+(D./freqcutoff2).^2*n)).*oriShift));
btw100 = ifft2(ifftshift(double(1./(1+(D./freqcutoff3).^2*n)).*oriShift));

figure('Name','Butterword');
subplot(2,2,1);
imshow(im);
subplot(2,2,2);
imshow(real(btw20),[]);
subplot(2,2,3);
imshow(real(btw50),[]);
subplot(2,2,4);
imshow(real(btw100),[]);

