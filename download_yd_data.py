import argparse
import json
import logging
import multiprocessing as mp
import os
import requests
import csv
import pathlib



def parseArgs():
    parser = argparse.ArgumentParser(description="This program downloads data from the YouDescribe data repository for use in AI/ML applications.")
    parser.add_argument('--inputFile', help="The input file that contains all of the audio clips. This should be a CSV file with at least these columns: [videos_youtube_id, audio_descriptions_id, audio_clips_id, file_path, file_name]")
    parser.add_argument('--audioDescDir', help="The path to the directory where the downloaded audio clips will be stored. The downloaded audio clips will be separated into different folders by YouTube video ID and Audio Description ID. Should end with a '/'")
    parser.add_argument('--useAvailableOnly', default=True, help=("Choose whether or not you want to download the audio clips of YouTube videos that are no longer available."
     "Default is set to only download audio clips from available YouTube videos."
     "DISCLAIMER: We do not keep track of the status of all of the YouTube videos that we provide audio descriptions for in real time."
    " Therefore, we cannot guarantee that there are audio clips that say they are from an 'available' YouTube video but the YouTube video was taken down."))

    args = parser.parse_args()

    return args

def downloadAudioDescriptions(inputFile, audioDescDir, useAvailableOnly):
    
    if inputFile == None or len(inputFile) <= 0:
        print(f"Error: No input file given")
        return
    
    if audioDescDir == None or len(audioDescDir) <= 0:
        print(f"Error: No audioDescDir given")
        return

    with open(inputFile, "r", encoding='utf-8') as f:
        reader = csv.reader(f, dialect=csv.excel)

        header = next(reader)
        inputRows = [row for row in reader]

    videoIDCol = -1
    videoStatusCol = -1
    audioDescIDCol = -1
    audioClipsIDCol = -1
    filePathCol = -1
    fileNameCol = -1

    for col, heading in enumerate(header):
        headingLower = heading.lower()

        if headingLower.__contains__('videos_youtube_id'):
            videoIDCol = col
        elif headingLower.__contains__('videos_youtube_status'):
            videoStatusCol = col
        elif headingLower.__contains__('audio_descriptions_id'):
            audioDescIDCol = col
        elif headingLower.__contains__('audio_clips_id'):
            audioClipsIDCol = col
        elif headingLower.__contains__('file_path'):
            filePathCol = col
        elif headingLower.__contains__('file_name'):
            fileNameCol = col
    

    if videoIDCol == -1 or audioDescIDCol == -1 or audioClipsIDCol == -1 or filePathCol == -1 or fileNameCol == -1:
        print(f"Error: Input csv files does not contain columns named 'videos_youtube_id', 'audio_descriptions_id', 'audio_clips_id', 'file_path', and 'file_name'. Aborting...")
        return
    
    if videoStatusCol == -1:
        print(f"WARNING: No 'videos_youtube_status' column. Will assume to download all audio clips regardless of video status.")
    
    print(f"Input file format has been validated. Starting download.")

    for col, row in enumerate(inputRows):
        videoID = row[videoIDCol]
        videoStatus = row[videoStatusCol]
        audioDescID = row[audioDescIDCol]
        audioClipID = row[audioClipsIDCol]
        filePath = row[filePathCol]
        fileName = row[fileNameCol]

        if useAvailableOnly and videoStatus.lower() == 'unavailable':
            continue

        localFilePathDir = f"{audioDescDir}{videoID}/{audioDescID}"
        localFilePath = f"{localFilePathDir}/{fileName}"

        print(localFilePathDir)

        if not os.path.exists(localFilePathDir):
            print(f"Creating new directory for audio clips {localFilePathDir}")
            pathlib.Path(localFilePathDir).mkdir(parents=True, exist_ok=True)

        if os.path.exists(localFilePath):
            print(f"Already downloaded {fileName} before. Skipping...")
            continue
    
        print(f"Downloading Audio Clip: {fileName}...")

        print(f"http://13.58.32.80{filePath}/{fileName}")

        doc = requests.get(f"http://13.58.32.80{filePath}/{fileName}")

        if not (doc.status_code >=200 and doc.status_code < 300):
            print(f"Please download the latest version of this data repository to get the latest version of the download script.")

        with open(localFilePath, 'wb') as f:
            f.write(doc.content)



def main():
    opt = parseArgs()

    downloadAudioDescriptions(opt.inputFile, opt.audioDescDir, opt.useAvailableOnly)




    # Check if user already has an API key in this same folder


    # If user doesn't have API key, start onboarding process

    # Have user input email


    # Send verification email to user


    # Have user agree to Terms and Conditions for Creative Commons License


    # Ask user what purposes they are using data for (Need to come up with more possibilities)
    # 1. Research
    # 2. Education
    # 3. Other

    # Receive/Write API key to file

    # Move on to UI to allow users to download data


    # If user does have API key, give them four options:
    # 1. Download premium dataset
    # 2. Download transcribed dataset (includes any transcribed premium dataset)
    # 3. Download Untranscribed dataset (includes any untranscribed premium dataset)
    # 4. Download all











if __name__ == "__main__":
    main()