im = imread('images\lenna_noise.pgm');
im2 = imread('images\lenna.pgm');
origin = im2double(im2);
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

ideal20_error = origin - ideal20;
ideal50_error = origin - ideal50;
ideal100_error = origin - ideal100;
RMS20 = sqrt(sum(sum(ideal20_error.^2))/(x*y));
RMS50 = sqrt(sum(sum(ideal50_error.^2))/(x*y));
RMS100 = sqrt(sum(sum(ideal100_error.^2))/(x*y));

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

guass20_error = origin - guass20;
guass50_error = origin - guass50;
guass100_error = origin - guass100;
GRMS20 = sqrt(sum(sum(guass20_error.^2))/(x*y));
GRMS50 = sqrt(sum(sum(guass50_error.^2))/(x*y));
GRMS100 = sqrt(sum(sum(guass100_error.^2))/(x*y));


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

btw20_error = origin - btw20;
btw50_error = origin - btw50;
btw100_error = origin - btw100;
BRMS20 = sqrt(sum(sum(btw20_error.^2))/(x*y));
BRMS50 = sqrt(sum(sum(btw50_error.^2))/(x*y));
BRMS100 = sqrt(sum(sum(btw100_error.^2))/(x*y));

figure('Name','Butterword');
subplot(2,2,1);
imshow(im);
subplot(2,2,2);
imshow(real(btw20),[]);
subplot(2,2,3);
imshow(real(btw50),[]);
subplot(2,2,4);
imshow(real(btw100),[]);


%median
noise = padarray(im,[1 1],'both');
[x,y] = size(im);

for i = 1:x
    for j = 1:y
        result = zeros(9,1);
        count = 1;
        for m = 1:3
            for n = 1:3
                result(count) = noise(m+i-1,n+j-1);
                count = count + 1;
            end
        end
        result = sort(result);
        medIm(i,j) = result(5);
    end
end
medIm = uint8(medIm);
figure; imshow(medIm);
mednew = double(medIm);
Mederror = origin - mednew;
MRMS = sqrt(sum(sum(Mederror.^2))/(x*y));






