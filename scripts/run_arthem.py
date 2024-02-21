#!/usr/bin/env python3
import os
import subprocess
import shutil

def run_cmd(cmd: str):
	"""Run a command in the terminal."""
	print("cmd:", cmd)
	print("output:")
	subprocess.Popen(cmd, shell=True).wait()

data_dir = "/scratch/project/open-29-7/varun_ws/train_ngps/data"


if __name__ == '__main__':
	for object in range(1, 45):
		dir = f"object_{object}"
		dir_path = os.path.join(data_dir, dir)
		snap_path = os.path.join(dir_path, "snapshots.ingp")
		if os.path.exists(snap_path):
			#shutil.rmtree(dir_path)
			print("skipping", dir)
			continue
		snap_path1 = os.path.join(dir_path, "snapshots")
		if os.path.exists(snap_path1):
			shutil.rmtree(dir_path)

		scene = "--scene " + os.path.join(data_dir, dir)
		save_snap = " --save_snapshot " + os.path.join(data_dir, dir, "snapshots.ingp")
		steps = " --n_steps 35000"
		run_cmd(f"python run.py {scene} {save_snap} {steps}")
