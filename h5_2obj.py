# .h5   =====>>>>    .obj



import h5py
import pandas as pd
import numpy as np
from google.colab import files

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

    # 첫 번째 객체의 데이터프레임으로 변환
    first_object = pd.DataFrame(data[0], columns=['X', 'Y', 'Z'])
    first_object['label'] = labels[0]

    # 데이터 출력
    print(first_object.head())

# .obj 파일로 저장하는 함수
def save_to_obj(points, label, filename):
    with open(filename, 'w') as f:
        for i in range(points.shape[0]):
            x, y, z = points[i]
            f.write(f'v {x} {y} {z}\n')

        # 임의의 색상 매핑 (label 값에 따라 색상 변경)
        color = (label * 50 % 256, label * 85 % 256, label * 120 % 256)
        f.write(f'usemtl {color[0]/255} {color[1]/255} {color[2]/255}\n')

# 첫 번째 객체를 .obj 파일로 저장
output_obj_file = 'first_object_converted.obj'
save_to_obj(data[0], labels[0], output_obj_file)

# 변환된 파일 다운로드 링크 제공
files.download(output_obj_file)
