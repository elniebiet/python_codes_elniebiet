import subprocess

output = subprocess.check_output(['netstat', '-a'])
output_text = output.decode('utf-8')
print(output_text)
 
output = subprocess.check_output(['shutdown', '-i'])
# output_text = output.decode('utf-8')
# print(output_text)

#exception hndling
try:
    out_bytes = subprocess.check_output(['cmd','arg1','arg2'])
    print(out_bytes.decode('utf-8'))
except subprocess.CalledProcessError as e:
    out_bytes = e.output # Output generated before error
    print(out_bytes.decode('utf-8'))
    code = e.returncode # Return code
    print(code)