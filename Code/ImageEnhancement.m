function Enhanced_img = ImageEnhancement(Normalized_img)
%     [row_number,col_number] = size(Normalized_img)
% 
%     column_split = []
%     for i = 1:32
%         value = i*16
%         column_split = [column_split,value]
%     end
%     column_split2 = column_split +1
%     column_split2 = [1,column_split2]
%     column_split2 = column_split2(:,1:end-1)
% 
%     row_split = []
%     for i = 1:4
%         value = i*16
%         row_split = [row_split,value]
%     end 
%     row_split2 = row_split + 1 
%     row_split2 = [1,row_split2]
%     row_split2 = row_split2(:,1:end-1)
% 
%     background_illumination = zeros(4,32)
%     for i = 1:4
%         for j = 1:32
%             background_illumination(i,j) = mean2(Normalized_img(row_split2(i):row_split(i),column_split2(j):column_split(j)))
%         end
%     end
% 
%     
%     %figure(3),subplot(5,1,1),imshow(Normalized_img),axis on;
%     
%     background_illumination = uint8(background_illumination)
% %     figure(3),subplot(5,1,2),imshow(background_illumination),axis on;
% 
% 
%     background_illumination_resize = imresize(background_illumination,16,'bicubic')
%     %figure(3),subplot(5,1,3),imshow(background_illumination_resize),axis on;
% 
%     preprocessing = Normalized_img - background_illumination_resize
%    % figure(3),subplot(5,1,4),imshow(preprocessing),axis on;

    Enhanced_img = adapthisteq(Normalized_img,'NumTiles',[2 16],'ClipLimit',0.1);
    %figure(3),subplot(5,1,5),imshow(Enhanced_img),axis on;

    

end