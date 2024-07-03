def fileWriter(filename, output) : 
    with open(filename + ".txt",'a') as file:
                file.write(output)