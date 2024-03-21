# try:
#     l=[5,4,3,2,1]
#     i=int(input("enter index number"))
#     print(f"{l[i]}")
# except:
#     print("some error")

# finally:
#     print("i am always executable")


# ----ye to ham ese bhi kr sakte the direct print ka use krke --------------------------------------------------------------------------------------------
# try:
#     l=[5,4,3,2,1]
#     i=int(input("enter index number"))
#     print(f"{l[i]}")
# except:
#     print("some error")

# # finally:
# #     print("i am always executable")
# print("i am always executable")

# --------------------------------------------------------------------------------------------

def func():
    try:
        l=[5,4,3,2,1]
        i=int(input("enter index number"))
        print(f"{l[i]}")
        return 1
    except:
        print("some error")
        return 0
        # finally:
        #     print("i am always executable")
        print("i am always executable")
x=func()
print(x)

def func():
    try:
        l=[5,4,3,2,1]
        i=int(input("enter index number"))
        print(f"{l[i]}")
        return 1
    except:
        print("some error")
        return 0
    finally:
            print("i am always executable")
        # print("i am always executable")
x=func()
print(x)

