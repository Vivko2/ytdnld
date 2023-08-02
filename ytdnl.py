# program skida yt videe definisane linkovima u csv fileu
# csv file je lista oblika: link, string datuma
# po downloadu filea fajl se reimenuje dodavanjem tog datumskog prefiksa što donosi slog u folderu


from pytube import YouTube
import csv
import os

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    # youtubeObject = youtubeObject.streams.get_audio_only()
    youtubeObject.download()
    return youtubeObject.default_filename

    # try:
    #     youtubeObject.download()
    # except:
    #     print("An error has occurred")
    # # print("Download is completed successfully")

def read_csv_file(filename):
    data = []
    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    return data

def rename_file_with_prefix(file_path, prefix):
    # Extract the file name from the provided file path
    file_name = os.path.basename(file_path)

    # Check if the file exists
    if os.path.exists(file_path):
        # Get the directory path without the file name
        # directory_path = os.path.dirname(file_path)

        # Combine the prefix with the original file name
        new_file_name = prefix + file_name

        # Create the new file path
        # new_file_path = os.path.join(directory_path, new_file_name)
        new_file_path = os.path.join(new_file_name)

        try:
            # Rename the file with the new name
            os.rename(file_path, new_file_path)
            print(f"File renamed to '{new_file_name}' successfully.")
        except OSError as e:
            print(f"Error occurred while renaming the file: {e}")
    else:
        print(f"File '{file_path}' does not exist.")



csv_path = 'ytlinks.csv'
youtube_video = read_csv_file(csv_path)
for video in youtube_video:
    print(video[0])
    Download(video[0])
    print(Download(video[0]))

    file_path=Download(video[0])
    file_prefix=video[1]
    rename_file_with_prefix(file_path, file_prefix)

