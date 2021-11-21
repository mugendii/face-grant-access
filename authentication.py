import getpass
import cv2
import face_recognition
import sys






#registration
database ={}

user_name = input("register with user_name: ")
password = input("Enter password: ")


database = {user_name:password}

def take_users_photo():
    print('Registration face scan in progress....')

    video_capture = cv2.VideoCapture(0)

    # Capture frame
    ret, frame = video_capture.read()

    # Write frame in file
    cv2.imwrite('image.jpg', frame)

    # When everything is done, release the capture
    video_capture.release()
    print('scan is complete')


take_users_photo()




#login
login_username = input("Enter Your Username to log in : ")
login_password = input("Enter Your Password : ")
# for i in database.keys():
#     if username == i:
#          while password != database.get(i):
#             password = getpass.getpass("Enter Your Password Again : ")
#          break
if login_username == user_name:

  if login_password== password:
        print("Welcome",user_name)



        print('face scan in progress....')


        video_capture = cv2.VideoCapture(0)

        # Capture frame
        ret, frame = video_capture.read()

        # Write frame in file
        cv2.imwrite('new_image.jpg', frame)

        # When everything is done, release the capture
        video_capture.release()
        print('scan is complete')

        def analyze_user():
            print('analyzing face..')
            #users picture comparision
            baseimg = face_recognition.load_image_file('image.jpg')
            baseimg = cv2.cvtcolor(baseimg,cv2.color_BGR2RGB)

            myface = face_recognition.face_locations(baseimg)[0]
            encodemyface = face_recognition.face_encodings(baseimg)[0]
            cv2.rectangle(baseimg,(myface[3],myface[0]),(myface[1],myface[2]),(255,0,255),2)

            cv2.imshow("test",baseimg)
            cv2.waitkey(0)


            #sample image of face picture
            sampleimage = face_recognition.load.image_file("new_image.jpg")
            sampleimage = cv2.cvtcolor(baseimg, cv2.color_BGR2RGB)


            try:
                samplefacetest = face_recognition.face_locations(sampleimage)[0]
                encodesamplefacetest = face_recognition.face_encodings(sampleimage)[0]
            except IndexError:
                print('authentification error')
                sys.exit()

            cv2.rectangle(sampleimage, (myface[3], myface[0]), (myface[1], myface[2]), (255, 0, 255), 2)

            cv2.imshow("test", sampleimage)
            cv2.waitkey(0)

            result = face_recognition.compare_faces([encodemyface],encodesamplefacetest)
            resultstring = str(result)



            if resultstring == "[True]":
                print('login was successful...Welcome ')

            else:
                print('login failed ...try again')


        analyze_user()
  else:
                     print("User not recognised")

else:
    print("user not recognised")








