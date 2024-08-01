# .h5   =====>>>>    .obj



import h5py
import pandas as pd
import numpy as np
from google.colab import files

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

    # ù ��° ��ü�� ���������������� ��ȯ
    first_object = pd.DataFrame(data[0], columns=['X', 'Y', 'Z'])
    first_object['label'] = labels[0]

    # ������ ���
    print(first_object.head())

# .obj ���Ϸ� �����ϴ� �Լ�
def save_to_obj(points, label, filename):
    with open(filename, 'w') as f:
        for i in range(points.shape[0]):
            x, y, z = points[i]
            f.write(f'v {x} {y} {z}\n')

        # ������ ���� ���� (label ���� ���� ���� ����)
        color = (label * 50 % 256, label * 85 % 256, label * 120 % 256)
        f.write(f'usemtl {color[0]/255} {color[1]/255} {color[2]/255}\n')

# ù ��° ��ü�� .obj ���Ϸ� ����
output_obj_file = 'first_object_converted.obj'
save_to_obj(data[0], labels[0], output_obj_file)

# ��ȯ�� ���� �ٿ�ε� ��ũ ����
files.download(output_obj_file)
