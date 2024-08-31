""" To train: 

!git clone https://github.com/NanoCode012/OIDv6_ToolKit_Download_Open_Images_Support_Yolo_Format.git

!pip3 install -r /content/OIDv6_ToolKit_Download_Open_Images_Support_Yolo_Format/requirements.txt

!mkdir OID
!mkdir OID/Dataset

classes = 'Book'
samples = 5000

!python /content/OIDv6_ToolKit_Download_Open_Images_Support_Yolo_Format/main.py downloader --classes {classes} --type_csv train --limit {samples}

!zip -r /content/data.zip  /content/OID/Dataset/train/

"""