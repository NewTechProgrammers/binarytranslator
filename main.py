
a = "011000010110111001100100011100100111101001100101011010100010000001110100011011110010000001100011011110100110000101100100"

# Initialize a binary string
input_string=int(a, 2);
 
#Obtain the total number of bytes
Total_bytes= (input_string.bit_length() +7) // 8
 
#Convert these bits to bytes
input_array = input_string.to_bytes(Total_bytes, "big")
 
#Convert the bytes to an ASCII value and display it on the output screen
ASCII_value=input_array.decode()
print(ASCII_value)
