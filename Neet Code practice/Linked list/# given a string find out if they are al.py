# given a string find out if they are all unique characters


# def unique(text):
#     dictionary = {}
    
#     for i in text: 
#         if i in dictionary:
#             return False
#         else:
#             dictionary [i] += 1
        
#     return True



# print(unique("race"))
char_dict = {}
my_srt = "acar"

for character in my_srt:
    if character in char_dict:
       print ("False")
    else:
       char_dict[character] = True
       
    print ("True")