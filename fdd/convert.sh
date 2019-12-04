#! /bin/bash

OUT_DIR="output"
CNT_FILE="num_frames.txt"

# Find output path
curr_dir=$(dirname $0)
out_path="${curr_dir}/${OUT_DIR}"

# Find image size
size=$(head -n 1 fdd_conf.txt | tr "x" ":")
echo $size

if [ $# -eq 1 ]; then 
	rm -rf ${out_path}/*
	ffmpeg -i $1 -pix_fmt monob -vf "scale=${size}, fps=15" ${out_path}/frame%d.png -hide_banner
	frame_count=$(ls -l ${out_path} | wc -l)
	echo "$((frame_count-1))" > ${out_path}/${CNT_FILE}
fi

