import argparse
import json
import logging
import multiprocessing as mp
import os
import requests
import csv
import pathlib

"""
NOTICE: PLEASE DO NOT ALTER THIS FILE

The YouDescribe Team does not guarantee that you will be able to download the You Described, We Archived dataset
if this file has been changed. If you have issues accessing/downloading the dataset after following this script,
and you have already downloaded the latest version of this script from GitHub, then please create an issue on
the GitHub with your request ID, and we will try to get back to you as soon as possible. 
"""

url = "https://ai.youdescribe.org/api"

def parseArgs():
    parser = argparse.ArgumentParser(description="This program downloads data from the YouDescribe data repository for use in AI/ML applications.")
    parser.add_argument('--audioDescDir', default="./", help="The path to the directory where the downloaded audio clips will be stored. The downloaded audio clips will be separated into different folders by YouTube video ID and Audio Description ID. Should end with a '/'")
    parser.add_argument('--useAvailableOnly', default=True, help=("Choose whether or not you want to download the audio clips of YouTube videos that are no longer available."
     "Default is set to only download audio clips from available YouTube videos."
     "DISCLAIMER: We do not keep track of the status of all of the YouTube videos that we provide audio descriptions for in real time."
    " Therefore, we cannot guarantee that there are audio clips that say they are from an 'available' YouTube video but the YouTube video was taken down."))

    args = parser.parse_args()

    return args

def noError(statusCode):
    return statusCode < 400

def writeApiKeyToFile(apiKeyResponseJson):
    print("Writing API key to yuwa.json...")
    print("PLEASE MAKE SURE TO KEEP THIS API KEY SAFE, SECURE, AND DO NOT ALTER IT. IF YOU LOSE YOUR GIVEN API KEY, YOU MUST CREATE A NEW ISSUE ON GITHUB REQUESTING A NEW API KEY.")

    apiKey = {}

    apiKey['apiKey'] = apiKeyResponseJson['apiKey']
    apiKey['email'] = apiKeyResponseJson['email']



    with open('yuwa.json', "w") as f:
        json.dump(apiKey, f, indent=4)
        f.close()

    print("Finished writing API key to yuwa.json")



def downloadAudioDescriptions(email, apiKey, inputFile, audioDescDir, useAvailableOnly):
    
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

        print(f"{filePath}/{fileName}")

        doc = requests.get(f"{url}/audio-clips", json={
            "email": email,
            "apiKey": apiKey,
            "path": f"{filePath}/{fileName}"
        })

        if not (doc.status_code >=200 and doc.status_code < 300):

            if doc.status_code == 404:
                print(f"Requested path ({filePath}/{fileName}) could not be found in YuWA dataset. We are working on moving all audio clips over to the YuWA dataset. Please try again later.")
            else:
                print(f"Something went wrong. Please download the latest version of this data repository to get the latest version of the download script. If you already have the latest version, please create a new GitHub Issue describing the issue and the YouDescribe team will try to help as soon as possible.")
            
            continue

        with open(localFilePath, 'wb') as f:
            f.write(doc.content)
        




apiKeyLocation = "./yuwa.json"

def main():
    opt = parseArgs()


    response = requests.get(url)

    print(response.json())

    if not os.path.exists(apiKeyLocation):
        print("No API Key found, starting onboarding process...")

        email = input("Please enter your email:\n")

        response = requests.post(f"{url}/users/email", json={
            "email": email
        })


        if not(noError(response.status_code)):
            print(response.json()['message'])
            return

        print("Successfully registered email. Please check your email for a verification code.")

        while True:
            code = input("Please enter your given verification code (If you have already verified your email, just hit enter): ")

            response = requests.post(f"{url}/users/verify", json={
                "email": email,
                "code": code
            })

            if noError(response.status_code):
                break
            else:
                print("Incorrect verification code")

        
        response = requests.get(f"{url}/users/terms-and-conditions")

        print(response.json().get("termsAndConditions"))


        agreeInput = input("Do you agree to the terms and conditions of using the You Described, We Archived Dataset (Y/N)?: ")
        agree = False

        if agreeInput == "Y":
            agree = True

        response = requests.post(f"{url}/users/terms-and-conditions", json={
            "email": email,
            "agree": agree,
        })

        if not(noError(response.status_code)):
            print(response.json()['message'])
            return
        

        print("Under what category does your usage plan for this data fall under:")
        print("1. Research (Non-commerical purposes)")
        print("2. Education")
        print("3. Personal")
        print("4. Other")


        while True:
            reasonCategory = input("Choose the number that best corresponds to what you are using this data for: ")
            reason = input("Please give a more detailed description as to what you will be using this data for (The YouDescribe Team reserves the right to revoke access to this dataset at any time.):\n")

            response = requests.post(f"{url}/users/reason", json={
                "email": email,
                "reasonCategory": reasonCategory,
                "reason": reason
            })

            if noError(response.status_code):
                print(response.json()['message'])
                writeApiKeyToFile(response.json())
                print("Rerun this script to start downloading audio descriptions.")
                break
            else:
                print(response.json()['message'])

    else:
        print("API key found...")


        credentialsFile = open(apiKeyLocation, "r")

        credentials = json.loads(credentialsFile.read())


        print("Available Datasets:\n\t1. Download premium dataset\n\t2. Download transcribed dataset (includes any of the transcribed premium dataset)\n\t3. Download untranscribed dataset (includes any untranscribed premium dataset)\n\t4. Download all datasets")

        choice = input("Choose which dataset you would like to download (e.g. 1): ")

        choice = int(choice)


        if choice == 1:
            downloadAudioDescriptions(credentials['email'], credentials['apiKey'], './premium_transcribed_audio_clips_english.csv', opt.audioDescDir, opt.useAvailableOnly)
            downloadAudioDescriptions(credentials['email'], credentials['apiKey'], './premium_untranscribed_audio_clips_english.csv', opt.audioDescDir, opt.useAvailableOnly)
            return
        elif choice == 2:
            downloadAudioDescriptions(credentials['email'], credentials['apiKey'], './transcribed_audio_clips_english.csv', opt.audioDescDir, opt.useAvailableOnly)
            return
        elif choice == 3:
            downloadAudioDescriptions(credentials['email'], credentials['apiKey'], './untranscribed_audio_clips_english.csv', opt.audioDescDir, opt.useAvailableOnly)
            return
        elif choice == 4:
            downloadAudioDescriptions(credentials['email'], credentials['apiKey'], './premium_transcribed_audio_clips_english.csv', opt.audioDescDir, opt.useAvailableOnly)
            downloadAudioDescriptions(credentials['email'], credentials['apiKey'], './premium_untranscribed_audio_clips_english.csv', opt.audioDescDir, opt.useAvailableOnly)
            downloadAudioDescriptions(credentials['email'], credentials['apiKey'], './transcribed_audio_clips_english.csv', opt.audioDescDir, opt.useAvailableOnly)
            downloadAudioDescriptions(credentials['email'], credentials['apiKey'], './untranscribed_audio_clips_english.csv', opt.audioDescDir, opt.useAvailableOnly)

if __name__ == "__main__":
    main()