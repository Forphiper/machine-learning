# Style GAN

import subprocess
import os
import glob
import shutil


command_line = 'stylegan2_pytorch --data ./faces/faces/ --image-size 64 --batch-size 1 --network-capacity 256 --num-train-steps 30000'
#command_line = 'stylegan2_pytorch --new --data ./faces/faces/ --image-size 64 --batch-size 8 --network-capacity 256 --num-train-steps 30000'
args = command_line.split()
subprocess.run(args)

command_line = 'stylegan2_pytorch --generate --num_generate 1000 --num_image_tiles 1'
args = command_line.split()
subprocess.run(args)



# Rename and Compress files

# 1. create dir if not exist
# 2. move files to dest dir and rename in the process
# 3. compress

src_dir = './results/default/'
dest_dir = './results/rename/'
src_files = glob.glob(src_dir + 'generated*ema.jpg')

if not os.path.isdir(dest_dir):
    os.mkdir(dest_dir)

i = 1
for file in src_files:
    new_name = str(i) + '.jpg'
    new_path = os.path.join(dest_dir, new_name)
    shutil.move(file, new_path)
    i += 1

command_line = 'tar -zcf ../../submission.tgz .'
args = command_line.split()
subprocess.call(args, cwd="./results/rename")


