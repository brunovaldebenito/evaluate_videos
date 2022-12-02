import cv2
import numpy as np
import os
import shutil


def main():
    directory = '/data1/bruno.valdebenito/evaluate_videos/videos_example/'
    output_dir = '/data1/bruno.valdebenito/evaluate_videos/videos_example_ev/'
    videos_list = os.listdir(directory)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("INFO \n\tKey G: select the good videos and save them",
          "\n\tKey B: select the bad videos and discard them",
          "\n\tKey P: Pause the process",
          "\n\tKey q: quit the process")
    print("\n\nSTARTING CLASSIFICATION\n\n")

    quit = False

    i = 0
    while i <= len(videos_list):

        video = videos_list[i]

        print(os.path.join(directory, video))
        print(i)

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
                    cv2.imshow('Video', frame)

                    # Press Q on keyboard to exit
                    key = cv2.waitKey(25) & 0xFF
                    if key == ord('g'):  # good
                        print("its a good video")
                        shutil.copy(directory + video, output_dir + video)
                        choose = True
                        i = i + 1
                        print("good",i)

                        break
                    if key == ord('b'):  # bad
                        print("its a bad video")
                        i = i + 1
                        print("bad", i)
                        choose = True
                        # do nothing

                        break

                    if key == ord('u'):  # undo
                        print("undo...")
                        # always deletes the previous file
                        if os.path.exists(output_dir + videos_list[i-1]):
                            os.remove(output_dir + videos_list[i-1])
                        choose = True
                        if i != 0:
                            i = i - 1
                        print("undo", i)

                        # TODO

                        break

                    if key == ord('p'):  # pause
                        print("Process paused")
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
            print("close", i)
            cap.release()

            # Closes all the frames
            cv2.destroyAllWindows()
        if quit:
            break


if __name__ == '__main__':
    main()
