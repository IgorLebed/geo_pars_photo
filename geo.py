import pexif


RUN = True
global img_counter 
z_counter = "0"
z2_counter = "00"
z3_counter = "000"
z4_counter = "0000"
#t1 = raw_input("Enter photo name like this DSC")
input_folder = "photo/DSC"
output_folder = "photo/photo_with_geo/DSC"

array = []
ax = []
ay = []
az = []

with open("photo/track.txt", 'r') as file:
    data = file.readlines()
    for line in data:
        array.append([float(x) for x in line.split()])
    num = sum(1 for line in data)
    
    for i in range(0, num):
        ax.append(array[i][1]) # lon
        ay.append(array[i][2]) # lat
        az.append(array[i][3]) # alt


def pars_photo():
	print "How much photo?"
	photo_counter = int(raw_input())
	print ("Enter start photo name, after DSC without first zero:") 
	buf = int(raw_input())
	img_counter = buf
	new_buf = buf
	RUN = True

	while RUN:
		if img_counter == buf+photo_counter:
			break
		for i in range(0, num):

			if len(str(new_buf)) == 1:
				print "DSC" + str(z4_counter) +  str(img_counter) + ".JPG"
				if img_counter == buf+photo_counter:
					break
				img_set = pexif.JpegFile.fromFile(str(input_folder) + str(z4_counter) +  str(img_counter) + ".JPG")
				img_set.set_geo((array[i][2]), (array[i][1]), (array[i][3]))

				print("the array 1", (array[i][2]))
				print("the array 2", (array[i][1]))
				print("the array 3", (array[i][3]))

				img_set.writeFile(str(output_folder) + str(z4_counter) + str(img_counter) + "_with_geo" + ".JPG")
				img_counter += 1
				new_buf = img_counter		
			if len(str(new_buf)) == 2:
				print "DSC" + str(z3_counter) +  str(img_counter) + ".JPG"
				if img_counter == buf+photo_counter:
					break
				img_set = pexif.JpegFile.fromFile(str(input_folder) + str(z3_counter) +  str(img_counter) + ".JPG")
				img_set.set_geo((array[i][2]), (array[i][1]), (array[i][3]))

				print("the array 1", (array[i][2]))
				print("the array 2", (array[i][1]))
				print("the array 3", (array[i][3]))

				img_set.writeFile(str(output_folder) + str(z3_counter) + str(img_counter) + "_with_geo" + ".JPG")
				img_counter += 1
				new_buf = img_counter		
			if len(str(new_buf)) == 3:
				print "DSC" + str(z2_counter) +  str(img_counter) + ".JPG"
				if img_counter == buf+photo_counter:
					break
				img_set = pexif.JpegFile.fromFile(str(input_folder) + str(z2_counter) +  str(img_counter) + ".JPG")
				img_set.set_geo((array[i][2]), (array[i][1]), (array[i][3]))

				print("the array 1", (array[i][2]))
				print("the array 2", (array[i][1]))
				print("the array 3", (array[i][3]))

				img_set.writeFile(str(output_folder) + str(z2_counter) + str(img_counter) + "_with_geo" + ".JPG")
				img_counter += 1
				new_buf = img_counter
			if len(str(new_buf)) == 4:
				print "DSC" + str(z_counter) +  str(img_counter) + ".JPG"
				if img_counter == buf+photo_counter:
					break
				img_set = pexif.JpegFile.fromFile(str(input_folder) + str(z_counter) +  str(img_counter) + ".JPG")
				img_set.set_geo((array[i][2]), (array[i][1]), (array[i][3]))

				print("the array 1", (array[i][2]))
				print("the array 2", (array[i][1]))
				print("the array 3", (array[i][3]))

				img_set.writeFile(str(output_folder) + str(z_counter) + str(img_counter) + "_with_geo" + ".JPG")
				img_counter += 1
				new_buf = img_counter
			if len(str(new_buf)) == 5:
				print "DSC" + str(img_counter) + ".JPG"
				if img_counter == buf+photo_counter:
					break
				img_set = pexif.JpegFile.fromFile(str(input_folder) +  str(img_counter) + ".JPG")
				img_set.set_geo((array[i][2]), (array[i][1]), (array[i][3]))

				print("the array 1", (array[i][2]))
				print("the array 2", (array[i][1]))
				print("the array 3", (array[i][3]))

				img_set.writeFile(str(output_folder) + str(img_counter) + "_with_geo" + ".JPG")
				img_counter += 1
				new_buf = img_counter



pars_photo()