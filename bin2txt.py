# .bin  ======>>>>  .txt


import struct
import numpy as np
from google.colab import files

# ���� ���ε�
uploaded = files.upload()

# ���ε�� ���� �̸� ��������
for file_name in uploaded.keys():
    input_file_path = file_name

# ���̳ʸ� ���� �б�
with open(input_file_path, 'rb') as f:
    data = f.read()

# ù ��° float ���� �� ����Ʈ ��
num_points = struct.unpack('f', data[:4])[0]

# ������ �����ʹ� �� ����Ʈ�� �Ӽ� (�� ����Ʈ�� 11���� float ��)
point_data = data[4:]

# ��� ����Ʈ �����͸� �����Ͽ� �迭�� ��ȯ
points = struct.unpack('f' * int(num_points) * 11, point_data)

# numpy �迭�� ��ȯ
points = np.array(points).reshape(-1, 11)

# �ؽ�Ʈ ���Ϸ� ����
output_txt_file = input_file_path.replace('.bin', '.txt')

with open(output_txt_file, 'w') as file:
    file.write("x y z nx ny nz r g b instance_label semantic_label\n")
    for point in points:
        file.write(" ".join(map(str, point)) + "\n")

# ��ȯ�� �ؽ�Ʈ ���� �ٿ�ε� ��ũ ����
files.download(output_txt_file)
