# 最终训练好的文件使用方法
可以看这个仓库，使用opencv直接调用caffemodel的项目，C++实现
https://github.com/BlainWu/cat_or_dog_opencv-test

# 数据集准备
## 1.下载使用微软的没有被打乱的dataset 
https://www.microsoft.com/en-us/download/confirmation.aspx?id=54765 

## 2.数据集打标签
按照我的个人习惯，把手动猫和狗都挑出了20%的图片作为测试集  
最后的文件夹组成结构是这样  
|--dataset  
|----test   
|------cat_test   
|------dog_test   
|----train   
|------cat_train  
|------dog_train  

图片的标签比较容易打，这写了一个python文件auto_list.py ,可以在终端通过命令 python auto_list.py test或者train即可得到标签。  
## 3.数据转换
因为caffe支持lmdb类型的数据库，用打包好的数据库训练更快。转换的脚本为文件为create_lmdb.sh
## 4.得到均值文件
脚本文件dataset_mean.sh

# 网络的设置
## 1.纯网络结构文件，训练的时候不会使用到  
deploy.prototxt
## 2.训练配置参数文件  
solver.prototxt
## 3.训练实际使用的网络文件
train_val.prototxt
