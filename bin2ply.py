# .bin  ======>>>>  .ply


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

# PLY ���Ϸ� ����
output_ply_file = input_file_path.replace('.bin', '.ply')

with open(output_ply_file, 'w') as file:
    # ��� �ۼ�
    file.write("ply\n")
    file.write("format ascii 1.0\n")
    file.write(f"element vertex {int(num_points)}\n")
    file.write("property float x\n")
    file.write("property float y\n")
    file.write("property float z\n")
    file.write("property float nx\n")
    file.write("property float ny\n")
    file.write("property float nz\n")
    file.write("property uchar red\n")
    file.write("property uchar green\n")
    file.write("property uchar blue\n")
    file.write("property int instance_label\n")
    file.write("property int semantic_label\n")
    file.write("end_header\n")
    # ������ �ۼ�
    for point in points:
        x, y, z, nx, ny, nz, r, g, b, instance_label, semantic_label = point
        file.write(f"{x} {y} {z} {nx} {ny} {nz} {int(r)} {int(g)} {int(b)} {int(instance_label)} {int(semantic_label)}\n")

# ��ȯ�� PLY ���� �ٿ�ε� ��ũ ����
files.download(output_ply_file)
