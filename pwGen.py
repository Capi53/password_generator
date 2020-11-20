import string
import random
import sys
import os

def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(12, 15)
  return ''.join(random.choice(chars) for x in range(size))
  
def write_to_clipboard(output):
    import subprocess
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode())
    return output
    
def write_to_file(path, contents):
	with open(path,"a") as f:
		for idx in contents:
			if idx == contents[0]:
				f.write("%s\n" %idx)
			else:
				f.write("\t%s\n" %idx)
		f.write("------------------\n")
			
def main(service_name, service_id, remark):
	pw = []
	for _ in range(10):
		tmp_pw = randompassword()
		pw.append(tmp_pw)
	service_pw = pw[random.randrange(10)]
	contents = [service_name, service_id, service_pw] + [remark]
	pb_pw = write_to_clipboard(service_pw)
	file_path = os.environ['PWD_TXT_PATH']
	write_to_file(file_path, contents)
	return service_pw, pb_pw

if __name__ == "__main__":
	args = sys.argv
	try:
		sp, tp =main(args[1], args[2], args[3:])
		print("SUCCESSED")
	except:
		print("you need to add argument service_name, your_id, remark")
