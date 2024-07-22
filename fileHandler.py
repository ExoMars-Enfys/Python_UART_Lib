from datetime import datetime 
timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

def fileWriter(filename, output) : 
    with open(filename + ".txt",'a') as file:
                file.write(output)


# def write_to_file(response,port,filename,i_Range,speed):
#     with alive_bar(i_Range) as bar:   # default setting
#         for i in range(i_Range):
#             with open(filename + ".txt",'a') as file:
#                 file.write(output)
#             Housekeeping_stream(uart_Packager(response,port,hk = False,cmdInput= "00000000000000"),filename)
#             sleep(speed)
#             bar()