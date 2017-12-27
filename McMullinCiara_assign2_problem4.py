# Problem #4: Data Size Converter
# Ciara McMullin
# 9/19/16
# Section 002

# get filze size from user in KB
file_size = int(input("Enter a file size, in kilobytes (KB): "))
print ()
print (file_size, "KB ...")
# convert file_size to floats and convert file_size to bits, bytes, megabytes, and gigabytes
bits = (float(file_size) * (8 * 1024))
byte = (float(file_size) * 1024)
megabytes = (float(file_size)) / 1024
gigabytes = megabytes / 1024
print ()
# convert values to two decimal places and insert commas where neccessary 
bits_ = format (bits, ",.2f")
byte_ = format (byte, ",.2f")
mega_ = format (megabytes, ",.2f")
giga_ = format (gigabytes, ",.2f")

# output results
print ("... in bits", "\t", bits_, "bits")
print ("... in bytes", "\t", byte_, "bytes")
print ("... in megabytes", "\t", mega_, "MG")
print ("... in gigabytes", "\t", giga_, " GB")

# 5 ways to crash the program:
# 1. I made a print statement and didnt match my delimiters.
# It said print ("... in gigabytes'). This was a syntax error.
# 2. I forgot to close my print statement at the end with parathenseis.
# This is a syntax error and my program crashed.
# 3. I accidently entered file size instead of an actual number which caused 
# my program to run but it crashed; this was a runntime error.
# 4. I accidently put 3 in for 2 in (bits, ",.2f") which let my program run
# but, it was a logic error because I wanted only two decimal places.
# 5. I didnt put my file size in as kilobytes so my program converted
# it to the wrong numbers. This was a logic error because it my program ran
# but, gave me the wrong answer.
