function Normalized_img = IrisNormalization(localized_img,pupil_center_x,pipul_center_y,pipul_radius,iris_center_x,iris_center_y,iris_radius)
    

    M = 64
    N = 512


    for n=1:N
        theta = 2*pi*n/N
    %%%%%%%%%%%%
    %%%%%%%%%%%%   Need to think about it here. Whether need to change
    %%%%%%%%%%%%   centers_pupil_crop(1),centers_pupil_crop(1),centers_pupil_crop(2)
    %%%%%%%%%%%%
        Xp(1,n)=pupil_center_x + pipul_radius*cos(theta); 
        Yp(1,n)=pipul_center_y + pipul_radius*sin(theta); 
        Xi(1,n)=iris_center_x + iris_radius*cos(theta);
        Yi(1,n)=iris_center_y + iris_radius*sin(theta); 
    end

    x = zeros(M, N)
    y = zeros(M, N)

    for m = 1:M
        x(m,:)=round(Xp(1,:) + (Xi(1,:) - Xp(1,:))*m/M) ;
        y(m,:)=round(Yp(1,:) + (Yi(1,:) - Yp(1,:))*m/M) ; 
    end
% % 
% 

    x=max(1,x);
    y=max(1,y);
%   
    [size_value1, size_value2] = size(localized_img)
    %map
    for i=1:M
        for j=1:N
            Normalized_img(i,j)=localized_img(min(x(i,j),size_value1),min(y(i,j),size_value2));
        end
    end

    % figure(2),subplot(1,1,1),imshow(Normalized_img),axis on;
end




