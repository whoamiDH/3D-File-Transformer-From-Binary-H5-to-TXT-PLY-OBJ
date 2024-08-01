# .h5  =======> .txt

import h5py
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
    datasets = list(file.keys())
    print("Datasets in the file:", datasets)

    # 데이터셋 읽기
    data = file['data'][:]
    labels = file['label'][:]

    # 데이터셋 차원 확인
    print(f"Data shape: {data.shape}")
    print(f"Labels shape: {labels.shape}")

# 텍스트 파일로 저장
output_txt_file = input_file_path.replace('.h5', '.txt')

with open(output_txt_file, 'w') as f:
    f.write("Datasets in the file:\n")
    f.write(f"{datasets}\n\n")

    f.write("Data shape:\n")
    f.write(f"{data.shape}\n\n")

    f.write("Labels shape:\n")
    f.write(f"{labels.shape}\n\n")

    f.write("Data:\n")
    np.savetxt(f, data.reshape(-1, data.shape[-1]), fmt='%f')

    f.write("\nLabels:\n")
    np.savetxt(f, labels.reshape(-1, 1), fmt='%d')

# 변환된 파일 다운로드 링크 제공
files.download(output_txt_file)
