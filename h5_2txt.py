# .h5  =======> .txt

import h5py
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
    datasets = list(file.keys())
    print("Datasets in the file:", datasets)

    # �����ͼ� �б�
    data = file['data'][:]
    labels = file['label'][:]

    # �����ͼ� ���� Ȯ��
    print(f"Data shape: {data.shape}")
    print(f"Labels shape: {labels.shape}")

# �ؽ�Ʈ ���Ϸ� ����
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

# ��ȯ�� ���� �ٿ�ε� ��ũ ����
files.download(output_txt_file)
