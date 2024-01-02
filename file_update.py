#appending a file 
#update data in an existing file ya kahe appending a file
f =open("update.txt","a")
f.write("hello i am added this text in file \n i am sucessfully updated  \n i am learning Object Array Functions Dom and Events in JS")

#read file
file =open("update.txt","r")
print(file.read())
# how close a file   file.close()
