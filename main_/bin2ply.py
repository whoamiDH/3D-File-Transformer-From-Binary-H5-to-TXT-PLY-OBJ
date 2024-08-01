# .bin  ======>>>>  .ply


import struct
import numpy as np
from google.colab import files

# 파일 업로드
uploaded = files.upload()

# 업로드된 파일 이름 가져오기
for file_name in uploaded.keys():
    input_file_path = file_name

# 바이너리 파일 읽기
with open(input_file_path, 'rb') as f:
    data = f.read()

# 첫 번째 float 값은 총 포인트 수
num_points = struct.unpack('f', data[:4])[0]

# 나머지 데이터는 각 포인트의 속성 (각 포인트당 11개의 float 값)
point_data = data[4:]

# 모든 포인트 데이터를 언팩하여 배열로 변환
points = struct.unpack('f' * int(num_points) * 11, point_data)

# numpy 배열로 변환
points = np.array(points).reshape(-1, 11)

# PLY 파일로 저장
output_ply_file = input_file_path.replace('.bin', '.ply')

with open(output_ply_file, 'w') as file:
    # 헤더 작성
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
    # 데이터 작성
    for point in points:
        x, y, z, nx, ny, nz, r, g, b, instance_label, semantic_label = point
        file.write(f"{x} {y} {z} {nx} {ny} {nz} {int(r)} {int(g)} {int(b)} {int(instance_label)} {int(semantic_label)}\n")

# 변환된 PLY 파일 다운로드 링크 제공
files.download(output_ply_file)
