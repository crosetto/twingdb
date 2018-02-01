def diff(string1, string2) :
    import difflib
    string1=str(string1).splitlines(1)
    string2=str(string2).splitlines(1)
    diff=difflib.unified_diff(string1, string2)
    return ''.join(diff)

# def continue_if_not(str3) :
#     import gdb
#     if str3 == "" :
#         gdb.execute("continue")
#     else :
#         print str3
#     return
