try:
    file2 = open('output.txt', 'w')
    write_file2 = file2.write(' ')
    file2.close()

    file1=open('output.txt','r+')
    input1=input("Enter text to write to the file: ")
    print("Data successfully written to output.txt.",'\n')
    input2=input("Enter additional text to append: ")
    print("Data successfully appended.",'\n')
    write_file=file1.write(input1)
    append_file=file1.write('\n')
    append_file1=file1.write(input2)
    file1.close()

    file3=open('output.txt','r+')
    read_file=file3.read()
    read_files = file3.readline()
    print('Final content of output.txt:')
    print(read_file)
    print(read_files)
    file1.close()



except FileNotFoundError:
    print("Error: The File 'output.txt' was not found")

