import cv2
import numpy as np
import os


def main():
    directory = '/data1/bruno.valdebenito/evaluate_videos/videos_example/'
    videos_list = os.listdir(directory)

    quit = False
    for video in videos_list:

        print(os.path.join(directory, video))

        choose = False
        while not choose:

            cap = cv2.VideoCapture(os.path.join(directory, video))
            if not cap.isOpened():
                print("Error opening video file")

            # Read until video is completed
            while cap.isOpened():

                # Capture frame-by-frame
                ret, frame = cap.read()

                if ret == True:
                    # Display the resulting frame
                    cv2.imshow('Frame', frame)

                    # Press Q on keyboard to exit
                    key = cv2.waitKey(25) & 0xFF
                    if key == ord('g'):  # good
                        print("its a good video")
                        choose = True
                        # TODO: SAVE

                        break
                    if key == ord('b'):  # bad
                        print("its a bad video")
                        choose = True
                        # TODO: DISCARD

                        break

                    if key == ord('p'):  # pause
                        print("Process paused")
                        # TODO: pause
                        while True:
                            if cv2.waitKey(25) & 0xFF == ord('p'):  # unpause
                                print("Process continue")
                                break
                    if key == ord('q'):  # quit
                        choose = True
                        quit = True
                        break
                else:
                    break



                # Break the loop

            # When everything done, release
            # the video capture object
            cap.release()

            # Closes all the frames
            cv2.destroyAllWindows()
        if quit:
            break


if __name__ == '__main__':
    main()
