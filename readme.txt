1. a.py应用背景：
读取xml和车牌图片，运行程序在车牌周边填充黑色边框，这里扩充w,h的20%。生成的扩充后的图片保存在out中，更新的xml会保存在xml目录中。
运行命令：
python2 a.py --detect_parent_path=/home/gch/AI/w/dataset/



2.  b.py应用背景：
读取原始图片（目录：img_dataset）以及对应的原始图片的车牌位置xml（目录：img_xml），读取车牌位置区域，根据车牌的w和h，分别扩充w和h的20%（相当于w两边各扩充10%,h两边各扩充10%），然后裁剪扩充后的车牌区域，保存在文件夹(目录：img_out),手动将基于车牌基础上标注的字符xml保存在xml目录下（注意此处的xml不是在原始图片上标注的字符），运行命令，程序会将修改后的xml保存在xml目录中。
运行命令：
python2 a.py --detect_parent_path=/home/gch/AI/w/img_dataset/




