# This program saves a sequence of video running times
# to the video_times.txt file

file = "video_times.txt"


def main():
    # Get the number of videos in the project
    num_videos = int(input("How many videos are in the project? "))

    # Open the file
    video_file = open(file, "w")

    # Get each video's running time
    print("Enter the running time for each video.")
    for count in range(1, num_videos + 1):
        run_time = float(input("Video #" + str(count) + ": "))
        video_file.write(str(run_time) + "\n")

    # Close the file
    video_file.close()
    print("The times have been saved to file", file)


main()
