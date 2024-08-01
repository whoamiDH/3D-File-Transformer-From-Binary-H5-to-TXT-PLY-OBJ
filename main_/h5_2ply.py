# .h5   =====>>>>    .ply


import h5py
import pandas as pd
import numpy as np
from google.colab import files

#���° ��ü ��������.
order_dh = 75
# ���� ���ε�
uploaded = files.upload()

# ���ε�� ���� �̸� ��������
for file_name in uploaded.keys():
    input_file_path = file_name

# HDF5 ���� ����
with h5py.File(input_file_path, 'r') as file:
    # ���� ���� �����ͼ� ����Ʈ ���
    print("Datasets in the file:", list(file.keys()))

    # �����ͼ� �б�
    data = file['data'][:]
    labels = file['label'][:]

    # �����ͼ� ���� Ȯ��
    print(f"Data shape: {data.shape}")
    print(f"Labels shape: {labels.shape}")

    # 261��° ��ü�� ���������������� ��ȯ
    first_object = pd.DataFrame(data[order_dh], columns=['X', 'Y', 'Z'])
    first_object['label'] = labels[order_dh]

    # ������ ���
    print(first_object.head())

# .ply ���Ϸ� �����ϴ� �Լ�
def save_to_ply(points, label, filename):
    with open(filename, 'w') as f:
        f.write('ply\nformat ascii 1.0\n')
        f.write(f'element vertex {points.shape[0]}\n')
        f.write('property float x\nproperty float y\nproperty float z\nproperty uchar red\nproperty uchar green\nproperty uchar blue\n')
        f.write('end_header\n')
        # ������ ���� ���� (label ���� ���� ���� ����)
        color = (label * 50 % 256, label * 85 % 256, label * 120 % 256)
        for i in range(points.shape[0]):
            x, y, z = points[i]
            f.write(f'{x} {y} {z} {color[0]} {color[1]} {color[2]}\n')

# order_dh��° ��ü�� .ply ���Ϸ� ����
output_ply_file = str(order_dh)+'st_object_converted.ply'
save_to_ply(data[order_dh], labels[order_dh], output_ply_file)

# ��ȯ�� ���� �ٿ�ε� ��ũ ����
files.download(output_ply_file)
