function V = FeatureExtraction(Enhanced_img)
    feature_extraction_img = Enhanced_img(1:48,:)


    % Channel 1

    % build the kernel
    delta_x1 = 3
    delta_y1 = 1.5

    f1 = 1/delta_y1

    height = 1
    width = 1
    for y = -height:height
        for x = -width:width
            G1(height+y+1,width+x+1) = (1/(2*pi*delta_x1*delta_y1))*(exp((-1/2)*(x^2/delta_x1^2 + y^2/delta_y1^2)))*(cos(2*pi*f1*sqrt(x^2 + y^2)))
        end
    end


    %Channel 2

    delta_x2 = 4.5
    delta_y2 = 1.5

    f2 = 1/delta_y2

    height = 1
    width = 1
    for y = -height:height
        for x = -width:width
            G2(height+y+1,width+x+1) = (1/(2*pi*delta_x2*delta_y2))*(exp((-1/2)*(x^2/delta_x2^2 + y^2/delta_y2^2)))*(cos(2*pi*f2*sqrt(x^2 + y^2)))
        end
    end


    F1_img = conv2(feature_extraction_img,G1,'same')
    F2_img = conv2(feature_extraction_img,G2,'same')

%     figure(4),subplot(3,1,1),imshow(feature_extraction_img),axis on;
%     figure(4),subplot(3,1,2),imshow(F1_img),axis on;
%     figure(4),subplot(3,1,3),imshow(F2_img),axis on;

    % convert both matrix cell value to absolute value

    F1_img_abs = abs(F1_img)
    F2_img_abs = abs(F2_img)



    row_divide = [8,8,8,8,8,8]

    column_divide = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]

    F1_img_small_blocks = mat2cell(F1_img_abs, row_divide, column_divide)
    F2_img_small_blocks = mat2cell(F2_img_abs, row_divide, column_divide)


    % calculate m
    F1_sum_of_everyone = cellfun(@(x) sum(x(:)), F1_img_small_blocks)
    F1_m = F1_sum_of_everyone/64
    
    % calculate sigma
    F1_m_cell = num2cell(F1_m)
    F1_sig = cellfun(@minus,F1_img_small_blocks,F1_m_cell,'UniformOutput',false)
   
    F1_sig_abs = cellfun(@(x) abs(x(:)), F1_sig,'UniformOutput',false)
    
    F1_sig_abs_sum = cellfun(@(x) sum(x(:)), F1_sig_abs)
    F1_sig_value = F1_sig_abs_sum/64
    
    
    F1_m_list = F1_m(:)
    F1_sig_value_list = F1_sig_value(:)
    
        
    F1_final = zeros(1,length(F1_m_list)*2)
    F1_final(1:2:end-1) = F1_m_list
    F1_final(2:2:end) = F1_sig_value_list
    
    
    % same method on F2
    % calculate m
    F2_sum_of_everyone = cellfun(@(x) sum(x(:)), F2_img_small_blocks)
    F2_m = F2_sum_of_everyone/64
    
    
    
     % calculate sigma
    F2_m_cell = num2cell(F2_m)
    F2_sig = cellfun(@minus,F2_img_small_blocks,F2_m_cell,'UniformOutput',false)
   
    F2_sig_abs = cellfun(@(x) abs(x(:)), F2_sig,'UniformOutput',false)
    
    F2_sig_abs_sum = cellfun(@(x) sum(x(:)), F2_sig_abs)
    F2_sig_value = F2_sig_abs_sum/64
    
    
    F2_m_list = F2_m(:)
    F2_sig_value_list = F2_sig_value(:)
    
    F2_final = zeros(1,length(F2_m_list)*2)
    F2_final(1:2:end-1) = F2_m_list
    F2_final(2:2:end) = F2_sig_value_list
    
    
    V = [F1_final,F2_final]
    
    
    
end





