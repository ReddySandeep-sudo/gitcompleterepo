import os
for path,dirs,files in os.walk("C://Users//rdoodima//Downloads//folder1/"):
    for f in files:
        print(f" {f}      ")
        filename = os.path.join(path,f)
        d = ['Execution_env','zip','move','touch','chmod 777']
        with open(filename) as file1:
            fileline1= file1.readlines()
            for i,line in enumerate(fileline1):
                if  "#uncomment this post QA" in line:
                    if line.lstrip().startswith("#"):
                        print(f"At linenum:{i} {line} has:  #uncomment this post QA and starts with #")
            for i,line in enumerate(fileline1):
                if '#uncomment this post QA' in line:
                        line.lstrip()
                        print(f"now the line is uncommented at linenum {i}",":  ",line.replace('#','',1))
            for x in d:
                for i,line in enumerate(fileline1):
                    if (x in line)and (line.startswith('#')):
                        print(f"{x} isfound and commented at linenum:{i}")
            for x in d:
                for line in fileline1:
                    if (x in line):
                        break
                else:
                    print(f"{x} not found")
                