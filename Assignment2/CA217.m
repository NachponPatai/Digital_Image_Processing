im = imread('images\Chess.pgm');
[x, y] = size(im);
kernel = [1 1 1;1 1 1;1 1 1];
kernel = kernel/9;
[l, o] = size(kernel);
pad = padarray(im,[1 1],'both');
new_kernel = padarray(kernel,[253 253],'post');
oriKernel = fftshift(fft2(new_kernel));

for i = 1:x
    for j = 1:y
        result = 0;
        for m = 1:l
            for n = 1:o
                con = double(kernel(m,n)).*double(pad(m+i-1,n+j-1));
                result = result + con; 
            end
        end
        im(i,j) = double(result);
    end
end

oriim = fftshift(fft2(im));
result = oriKernel.*oriim;
inIm = ifft2(ifftshift(result));
freqIm = uint8(abs(inIm));
imshow([im freqIm]);
