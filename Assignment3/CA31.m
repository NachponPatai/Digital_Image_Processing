im = imread('images\WormHole_1H.tif');
[x,y] = size(im);
kernel = [1 1 1;1 1 1;1 1 1];
kernel = kernel/9;
[l, o] = size(kernel);
pad = padarray(im,[1 1],'both');

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

GrayScale = rgb2gray(im);
bw1 = imbinarize(GrayScale,'adaptive','ForegroundPolarity','dark','Sensitivity',0.0);
canny = edge(bw1,'canny');
imshow(canny);
[centers, radii] = imfindcircles(canny,[5 12]);
viscircles(centers, radii,'Color','b');