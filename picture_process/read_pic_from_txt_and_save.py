clc;
clear;
main_Path='H:/project/NUAA/Detectedface/';
savePath='I:/Face_Liveness_Data/CNN_NUAA/test/fake/';
path1=[main_Path 'client_train.txt'];
path2=[main_Path 'imposter_train.txt'];
path3=[main_Path 'client_test.txt'];
path4=[main_Path 'imposter_test.txt'];

path={path1,path2,path3,path4};
i=0;
for pathIdx=1:length(path)
    fid=fopen(path{pathIdx},'r');
    while feof(fid) ~= 1;#只要不到文件结束
            name = fgetl(fid); #从文件中读取一行
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
