import cv2
import numpy as np
import os
import shutil
import argparse


def main(directory, output_dir, index):
    #directory = '/data1/bruno.valdebenito/evaluate_videos/videos_example/'

    #output_dir = '/data1/bruno.valdebenito/evaluate_videos/videos_example_ev/'




    print("INFO \n\tKey G: select the good videos and save them",
          "\n\tKey B: select the bad videos and discard them",
          "\n\tKey P: Pause the process",
          "\n\tKey Q: quit the process")
    print("\n\nSTARTING CLASSIFICATION\n\n")

    print('Input directory: \n\t', directory)
    print('Output directory: \n\t', output_dir)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    videos_list = os.listdir(directory)

    quit = False

    i = index
    while i <= len(videos_list):

        video = videos_list[i]

        print('Evaluating:',os.path.join(directory, video),'\n')

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
                    cv2.imshow(video, frame)

                    # Press Q on keyboard to exit
                    key = cv2.waitKey(25) & 0xFF
                    if key == ord('g'):  # good
                        print("Its a GOOD video\n")
                        shutil.copy(directory + video, output_dir + video)
                        choose = True
                        i = i + 1
                        print("Saved as:", output_dir + video, '\n')

                        break

                    if key == ord('b'):  # bad
                        print("Its a BAD video\n")
                        i = i + 1
                        choose = True
                        # do nothing

                        break

                    if key == ord('u'):  # undo
                        print("Undo...\n")
                        # always deletes the previous file
                        if os.path.exists(output_dir + videos_list[i - 1]):
                            os.remove(output_dir + videos_list[i - 1])
                            print("Deleting",output_dir + videos_list[i - 1], '\n')
                        choose = True
                        if i != 0:
                            i = i - 1

                        break

                    if key == ord('p'):  # pause
                        print("Process paused\n")
                        while True:
                            if cv2.waitKey(25) & 0xFF == ord('p'):  # unpause
                                print("Process continue\n")
                                break
                    if key == ord('q'):  # quit
                        print("QUIT\n")
                        print('Evaluate until:', videos_list[i - 1], '\n')
                        print('index:', i - 1, '\n')

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
    # Build the command line parser
    parser = argparse.ArgumentParser(
        description="Script for evaluate datasets",
        epilog="Enjoy!")

    parser.add_argument("-ind", "--input_directory", required=True,
                        help="Path to directory with the files to be evaluated.")
    parser.add_argument("-outd", "--output_directory", required=False,
                        help="Path to directory where the files will be "
                             "saved.",
                        default="")
    parser.add_argument("-i", "--index", required=False,
                        help="Index of file to start.",
                        default=0)

    args = parser.parse_args()

    input_dir = args.input_directory

    if input_dir[len(input_dir)-1] != '/':
        input_dir = input_dir + '/'

    output_dir = args.output_directory
    if output_dir == "":
        print('paso1')
        output_dir = input_dir[:-1] + '_evaluated/'
    elif output_dir[len(output_dir)-1] != '/':
        print(output_dir[len(output_dir)-1])
        output_dir = output_dir + '/'

    index = int(args.index)


main(input_dir, output_dir, index)
