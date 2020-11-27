height = input("Enter height in m ===> ")
width = input("Enter width in m===> ")
try:
    area = int(height) * int(width)
    print("Area ===>" , area, "meters")
except ValueError:
    print("Please enter number only")

#in linux scripts
#echo -n "Enter height in m ===> "
#read height
#echo -n "Enter width in m ===> "
#read width
#echo "area is `expr $height * $width` meter"