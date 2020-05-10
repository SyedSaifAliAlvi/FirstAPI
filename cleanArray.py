def Label_Correction(x):
    correct_Array=x
    if (correct_Array[6]==1):
        correct_Array[6]=0
        correct_Array[7]=1
    elif (correct_Array[6]==2):
        correct_Array[6]=0
        correct_Array[7]=0
        correct_Array[8]=1

    if(correct_Array[10]==2):
        correct_Array[10]=0
        correct_Array[11]=1
    elif(correct_Array[10]==3):
        correct_Array[10] = 0
        correct_Array[11] = 0
        correct_Array[12] = 1

    if(correct_Array[14]==2):
        correct_Array[14]=0
        correct_Array[15]=1

    if(correct_Array[17]==0):
        correct_Array[17]=1
    elif(correct_Array[17]==1):
        correct_Array[17]=0
        correct_Array[18]=1
    elif(correct_Array[17]==2):
        correct_Array[17] = 0
        correct_Array[18] = 0
        correct_Array[19] = 1



    return correct_Array
