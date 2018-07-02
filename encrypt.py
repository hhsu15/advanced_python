import os
from Crypto.Cipher import AES # Advanced Encrypt Standard
from Crypto.Hash import SHA256 # produces a 16 byte output
                               # hash users password to produce 
							   # same length everytime
from Crypto import Random

"""
PyCrypto 
Cryptography - encryption of plaintext into chphertext (unreadable) 
               and reverse, decryption of chphertext into plaintext

Cipher is used with a key which produces what looks like random output

"""

def encrypt(key, filename):
	# set the chunk size
	chunksize  = 64 * 1024
	
	outputFile= "(encrypted)" + filename
	filesize = str(os.path.getsize(filename)).zfill(16) #fill with zeros
	
	IV = Random.new().read(16) # Initialization Vector and read 16 bytes
    
	# create encryptor
	encryptor = AES.new(key, AES.MODE_CBC, IV)
    
	# read the file
	with open(filename, 'rb') as infile:
		with open(outputFile, 'wb') as outfile:
			# write the size into the output file
			outfile.write(filesize.encode('utf-8')) # file size is string
			# write the IV into the output file
			outfile.write(IV) 
            
			# infinite loop to encript
			while True:
			    # read each chunk provided the size
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				elif len(chunk) % 16 != 0: #mudulus adding padding
					chunk += b' ' * (16 - len(chunk) % 16 )

                    # encrpt the output file
					outfile.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
	"""decrypt file"""
	chunksize = 64 * 1024
	outputFile = filename[11:] # for "(encrypted)"

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)
				
				if len(chunk) == 0:
					break
				
				outfile.write(decryptor.decrypt(chunk))

            # turn it into the original size
			outfile.truncate(filesize) 

def getKey(password):
	hasher = SHA256.new(password.encode('utf-8')) # make the password same length 
	return hasher.digest()

def main():
	choice = input("Would you like to Encrypt or Decrypt? ")
	if choice == 'E':
		filename = input("File to encrypt: ")
		password = input("Password: ")
		encrypt(getKey(password), filename)
		print("Done")

	elif choice == 'D':
		filename = input("File to decrypt: ")
		password = input("Password: ")
		decrypt(getKey(password), filename)
		print("Done")

	else:
		print("No option selected. Closing..")

if __name__ == "__main__":
	main()
 
