function [localized_img,pupil_center_x,pipul_center_y,pipul_radius,iris_center_x,iris_center_y,iris_radius] = IrisLocalization(img,Min_r_Pupil,Max_r_Pupil,Min_r_Iris,Max_r_Iris,Iris_Sensitivity_value)
    

    pupil_area = img < 50;
    img(pupil_area) = 0;

    Iblur = imgaussfilt(img, 4);
    edge1 = edge(Iblur,'canny');


    % find pupul center

    [centers1, radii1, metric1] = imfindcircles(edge1,[Min_r_Pupil Max_r_Pupil]);

    centers_pupil_org = centers1(:,:); 
    radii_pupil_org = radii1(:);
    % metric_pupil_org = metric1(:);


    % Crop the image
    % % [xmin ymin width height] 
    X1 = centers_pupil_org(1,1)-135
    Y1 = centers_pupil_org(1,2)-135

    edge1_crop = imcrop(edge1,[X1 Y1 270 270])


    % find iris center and radius on the cropped image
    [centers2, radii2, metric2] = imfindcircles(edge1_crop,[Min_r_Iris Max_r_Iris],'Sensitivity',Iris_Sensitivity_value);

    centers_iris_crop = centers2(:,:); 
    radii_iris_crop = radii2(:);
    % metric_iris_crop = metric2(:);
    % viscircles(centers_iris_crop, radii_iris_crop,'EdgeColor','b');


    
    % find pupil center and radius on the cropped image
    [centers3, radii3, metric3] = imfindcircles(edge1_crop,[Min_r_Pupil Max_r_Pupil]);

    centers_pupil_crop = centers3(:,:); 
    radii_pupil_crop = radii3(:);
    % metric_pupil_crop = metric3(:);
    % viscircles(centers_pupil_crop, radii_pupil_crop,'EdgeColor','b');

    
     localized_img = imcrop(img,[X1 Y1 270 270])

%     viscircles(centers_pupil_crop, radii_pupil_crop,'EdgeColor','b');
%     viscircles(centers_iris_crop, radii_iris_crop,'EdgeColor','b');

    
%       draw_circle = localized_img
%      
%       draw_circle= insertShape(draw_circle,'circle',[centers_iris_crop(1) centers_iris_crop(2) radii_iris_crop],'LineWidth',5);
%      
%       draw_circle = insertShape(draw_circle,'circle',[centers_pupil_crop(1) centers_pupil_crop(2) radii_pupil_crop],'LineWidth',5);
%      
     
      
      iris_center_x = centers_iris_crop(1)
      iris_center_y = centers_iris_crop(2)
      iris_radius = radii_iris_crop
    
      pupil_center_x = centers_pupil_crop(1)
      pipul_center_y = centers_pupil_crop(2)
      pipul_radius = radii_pupil_crop
     
    
end

   