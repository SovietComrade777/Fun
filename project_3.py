"""Well this time too credit goes to programming hero ,Jhankar mahbub . 
  Though the imports and most of code is just same but with my little understanding 
  I Improved it little:
    1>Right eye blink means right click
    2>left eye blink means left click
    3>the colors are little bit changed for the eyes like blue is for left one and orange+some color is for right blink that circles of some color i don;t know it;s name hence.
    4>Enjoying a lot and you all should too"""
import cv2
import mediapipe as mp
import pyautogui
cam=cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h=pyautogui.size()
while True:
    _, frame= cam.read()
    frame=cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h,frame_w,_=frame.shape
    if landmark_points:
        landmarks=landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,120,255))
            if id==1:
                screen_x=screen_w/frame_w*x
                screen_y=screen_h/frame_h*y
                pyautogui.moveTo(screen_x,screen_y)
        left=[landmarks[145],landmarks[159]]
        right=[landmarks[475],landmarks[477]]
        for landmark in left:
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(145,97,42))  
        if (left[0].y-left[1].y)<0.008:
            pyautogui.leftClick()
        for landmark in right:
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,97,42)) 
        if (right[1].y-right[0].y)<0.008:
            pyautogui.rightClick() 
        cv2.imshow('I controlled mouse', frame)
    cv2.waitKey(1)
