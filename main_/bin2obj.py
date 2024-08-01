# .bin  ======>>>>  .obj


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

# ù �� ���� ����Ʈ ���
print("ù 10���� ����Ʈ:")
print(points[:10])

# OBJ ���Ϸ� ����
output_obj_file = input_file_path.replace('.bin', '.obj')

with open(output_obj_file, 'w') as file:
    file.write("# Converted OBJ file\n")
    for point in points:
        x, y, z, nx, ny, nz, r, g, b, instance_label, semantic_label = point
        file.write(f"v {x} {y} {z} {r/255.0} {g/255.0} {b/255.0}\n")

# ��ȯ�� OBJ ���� �ٿ�ε� ��ũ ����
files.download(output_obj_file)
