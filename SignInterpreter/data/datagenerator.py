import cv2
import numpy as np
import os
from data.keypoints import mediapipe_detection, mp_holistic, draw_styled_landmarks
from data.datarecord import actions, no_sequences, sequence_length, datadate, DATA_PATH, create_folder
from data.values import extract_keypoints



def generador():
    print("Generating dataset")
    create_folder()
    cap = cv2.VideoCapture(0)
    # Set mediapipe model 
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        
        # NEW LOOP
        # Loop through actions
        for action in actions:
            # Loop through sequences aka videos
            for sequence in range(no_sequences):
                # Loop through video length aka sequence length
                for frame_num in range(sequence_length):

                    # Read feed
                    ret, frame = cap.read()

                    # Make detections
                    image, results = mediapipe_detection(frame, holistic)
                    #print(results)

                    # Draw landmarks
                    draw_styled_landmarks(image, results)
                    
                    # NEW Apply wait logic
                    if frame_num == 0: 
                        cv2.putText(image, "STARTING COLLECTION", (120,200), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 4, cv2.LINE_AA)
                        cv2.putText(image, f"Collecting frames for {action} Video Number {sequence}", (15,12), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        # Show to screen
                        cv2.imshow("OpenCV", image)
                        cv2.waitKey(2000)
                    else: 
                        cv2.putText(image, f"Collecting frames for {action} Video Number {sequence}", (15,12), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        # Show to screen
                        cv2.imshow("OpenCV", image)
                    
                    # NEW Export keypoints
                    keypoints = extract_keypoints(results)
                    
                    npy_path = os.path.join(DATA_PATH, action, datadate, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)

                    # Break gracefully
                    if cv2.waitKey(10) & 0xFF == ord("q"):
                        break
                        
        cap.release()
        cv2.destroyAllWindows()
