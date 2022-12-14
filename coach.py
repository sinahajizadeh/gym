import mediapipe as mp
import cv2
import numpy as np




dr=mp.solutions.drawing_utils

pos=mp.solutions.pose

bodypose=pos.Pose()

ca=cv2.VideoCapture(0)

u=0
d=0


ch=0

my_holist=mp.solutions.holistic


with my_holist.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:



    while True:
        _,fr=ca.read()
        topimg=cv2.cvtColor(fr,cv2.COLOR_BGR2RGB)
        result=holistic.process(topimg)

        topimg=cv2.cvtColor(topimg,cv2.COLOR_RGB2BGR)
        

        

        #dr.draw_landmarks(topimg,result.face_landmarks,my_holist.FACEMESH_CONTOURS)


        


        if result.pose_landmarks:
            landbodylist=[]
            for index,point in enumerate(result.pose_landmarks.landmark):
                p1, p2, z = fr.shape
                a,b=int(point.x*p2),int(point.y*p1)
                landbodylist.append([index,a,b])


            if cv2.waitKey(20) & 0xFF == ord('a'):
                ch=1
                u=0
                d=0


            if ch==1:

                if landbodylist[20] and landbodylist[14] and landbodylist[19] and landbodylist[15]:    

                    if landbodylist[20][2]>landbodylist[14][2] and landbodylist[19][2]>landbodylist[13][2] and u==d:
                        d=d+1
                    


                    if landbodylist[20][2]<landbodylist[14][2] and landbodylist[19][2]<landbodylist[13][2] and d>u:
                        u=u+1
                    
                    
                    
            cv2.putText(topimg,str(u),(50,150),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),5)


            if cv2.waitKey(20) & 0xFF == ord('s'):
                ch=2
                u=0
                d=0
            
            if ch==2:
                if landbodylist[14] and landbodylist[12] and landbodylist[13] and landbodylist[11] and landbodylist[7] and landbodylist[8]:    

                    if landbodylist[13][2]>landbodylist[11][2] and landbodylist[14][2]>landbodylist[12][2] and u==d:
                        d=d+1
                    


                    if landbodylist[13][2]<landbodylist[11][2] and landbodylist[14][2]<landbodylist[12][2] and landbodylist[13][2]<=landbodylist[3][2] and landbodylist[14][2]<=landbodylist[6][2] and  d>u:
                        u=u+1


            
            
                    





     



        

        


        
        
        cv2.imshow('NJ', topimg)
        cv2.waitKey(1)

        if cv2.waitKey(20) & 0xFF == ord('d'):
            break
         




'''
while True:
    _,fr=ca.read()
    framergb=cv2.cvtColor(fr,cv2.COLOR_BGR2RGB)
    result=bodypose.process(framergb)
    #print(result.pose_landmarks)


    #for list of bodypose
    landbodylist=[]

    if result.pose_landmarks:
        for index, point in enumerate(result.pose_landmarks.landmark):
            p1, p2, z = fr.shape

            a,b=int(point.x*p2),int(point.y*p1)

            landbodylist.append([index,a,b])

            

            



            print(landbodylist[1])



    

           

            
    


        dr.draw_landmarks(fr,result.pose_landmarks,pos.POSE_CONNECTIONS)



    cv2.imshow('NJ', fr)
    cv2.waitKey(1)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break




print(np.shape(landbodylist))



if landbodylist[16][2] > landbodylist[14][2]:
                print("yes") 
                cv2.puText(fr,'ok',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

            else:
                print("not")
'''