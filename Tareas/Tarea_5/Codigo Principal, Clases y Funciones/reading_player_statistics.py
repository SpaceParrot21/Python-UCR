def reading_statistics():

    file_name = "Estadisticas.txt"

    try:
        # opening and reading the file 
        file_read = open(file_name, "r")
  
        # search for String Luis
        text = "Luis"
  
        # reading file content line by line.
        lines = file_read.readlines()
  
        new_list = []
        idx = 0
  
        # looping through each line in the file
        for line in lines:
            # if line have the input string, get the index 
            # of that line and put the
            # line into newly created list 
            if text in line:
                new_list.insert(idx, line)
                idx += 1
  
        # closing file after reading
        file_read.close()
  
        # if length of new list is 0 that means 
        # the input string doesn't
        # found in the text file
        if len(new_list)==0:
            print("\n\"" +text+ "\" is not found in \"" +file_name+ "\"!")
        else:
            # displaying the lines 
            # containing given string
            lineLen = len(new_list)
            print("\n**** Estas son la estadisticas de \"" +text+ "\" ****\n")
            for i in range(lineLen):
                print(end=new_list[i])
            print()
  
    # entering except block
    # if input file doesn't exist 
    except :
        print("\nThe file doesn't exist!")

reading_statistics()