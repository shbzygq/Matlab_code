clc;
clear;
main_Path='H:/project/NUAA/Detectedface/';
savePath='I:/Face_Liveness_Data/CNN_NUAA/test/fake/';
% path1=[main_Path 'train/train_pos.txt'];
% path2=[main_Path 'train/train_neg.txt'];
% path3=[main_Path 'test/test_pos.txt'];
% path4=[main_Path 'test/test_neg.txt'];
path1=[main_Path 'client_train.txt'];
path2=[main_Path 'imposter_train.txt'];
path3=[main_Path 'client_test.txt'];
path4=[main_Path 'imposter_test.txt'];

path={path1,path2,path3,path4};
i=0;
for pathIdx=4:4%length(path)
    fid=fopen(path{pathIdx},'r');
    while feof(fid) ~= 1;
            name = fgetl(fid);
            %name = fscanf(fid, '%s',i);
            if isempty(name)
                break;
            end
            picturePath=['H:/project/NUAA/Detectedface/' name];
            img= imread(picturePath);  
            i=i+1;
            Img1=imresize(img,[256,256]);
            Img2=imrotate(Img1,0);
            imwrite(Img2,[savePath,sprintf('%05d',i),'.jpg']);
    end
end  
