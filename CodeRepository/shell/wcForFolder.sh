#!/bin/sh
#Filename: wcForFolder.sh
# 统计一个文件夹下面的所有文件的行数之和
# usage:
# . wcForFolder.sh -f folderaddress
# 最容易误用的就是将wcForFolder.sh 文件移动到相应的目录下，然后执行; . wcForFolder.sh `pwd` ，这样会计算wcForFolder的行数。
foldername="";
while getopts "f:" arg
do
    case $arg in 
    f)
        foldername=$OPTARG
        ;;      
    ?)
        echo "unknow argument"
        exit -1 
        ;;      
    esac    
done
echo "foldername = "${foldername}
sum=0;
for i in `ls $foldername`
do
    i=${foldername}"/"${i} #字符串连接方法
    echo $i 
    tmp=`wc -l $i | cut -d ' ' -f 1`
    sum=$(($sum + $tmp))
done
echo $sum
