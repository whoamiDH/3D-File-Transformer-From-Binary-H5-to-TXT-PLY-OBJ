# .h5   =====>>>>    .ply


import h5py
import pandas as pd
import numpy as np
from google.colab import files

#몇번째 객체 가져올지.
order_dh = 75
# 파일 업로드
uploaded = files.upload()

# 업로드된 파일 이름 가져오기
for file_name in uploaded.keys():
    input_file_path = file_name

# HDF5 파일 열기
with h5py.File(input_file_path, 'r') as file:
    # 파일 내의 데이터셋 리스트 출력
    print("Datasets in the file:", list(file.keys()))

    # 데이터셋 읽기
    data = file['data'][:]
    labels = file['label'][:]

    # 데이터셋 차원 확인
    print(f"Data shape: {data.shape}")
    print(f"Labels shape: {labels.shape}")

    # 261번째 객체의 데이터프레임으로 변환
    first_object = pd.DataFrame(data[order_dh], columns=['X', 'Y', 'Z'])
    first_object['label'] = labels[order_dh]

    # 데이터 출력
    print(first_object.head())

# .ply 파일로 저장하는 함수
def save_to_ply(points, label, filename):
    with open(filename, 'w') as f:
        f.write('ply\nformat ascii 1.0\n')
        f.write(f'element vertex {points.shape[0]}\n')
        f.write('property float x\nproperty float y\nproperty float z\nproperty uchar red\nproperty uchar green\nproperty uchar blue\n')
        f.write('end_header\n')
        # 임의의 색상 매핑 (label 값에 따라 색상 변경)
        color = (label * 50 % 256, label * 85 % 256, label * 120 % 256)
        for i in range(points.shape[0]):
            x, y, z = points[i]
            f.write(f'{x} {y} {z} {color[0]} {color[1]} {color[2]}\n')

# order_dh번째 객체를 .ply 파일로 저장
output_ply_file = str(order_dh)+'st_object_converted.ply'
save_to_ply(data[order_dh], labels[order_dh], output_ply_file)

# 변환된 파일 다운로드 링크 제공
files.download(output_ply_file)
