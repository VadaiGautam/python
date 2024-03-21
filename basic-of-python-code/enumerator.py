marks = [10,20,30,40,50,60,70,80,90,100]
 

# for i in marks:

#     if i==100:
#       print("congratulations vadai !")
#     else:
#        print(i)

index =0
for i in marks:
    
    if index ==9:
        print("congratualations vadai")
    else:
        print("well done")
    
    index+=1
# ------------------------------------------------------------------------------------------
    
    #  enumerate --> it can return index vale and value

    for index , i in enumerate(marks,start=1):     #in this , first object get indexvale and second object can contain in the bracket value   ----> start =1 means index start from 1 not  from 0
        if index==9:
            print("congrats")
        else:
            print("next time do well")