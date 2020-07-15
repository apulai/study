input_file=open('/Users/andras.pulai/Downloads/locsol/program.html','r')
output_file=open('/Users/andras.pulai/Downloads/locsol/message.txt','w+')



print('String message = "', file=output_file)



for line in input_file:
    line=line.rstrip()
    line=line.replace('\"','\\\"')
    print("\\n", line, file=output_file, end='')
    print("\\", file=output_file)


print('";', file=output_file)

output_file.close()
input_file.close()

