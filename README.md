# You Described, We Archived: A Rich Audio Description Dataset

The You Described, We Archived dataset (YuWA) is a collaboration between San Francisco State University and The Smith-Kettlewell Eye Research Institute. It includes audio description (AD) data collected worldwide 2013-2022 through YouDescribe, an accessibility tool for adding audio descriptions to YouTube videos. YouDescribe, a web-based audio description tool along with an iOS viewing app, has a community of 12,000+ average annual visitors, with 3,000+ volunteer describers, and has created over 5,500+ audio described YouTube videos. 

Blind and visually impaired (BVI) viewers request YouTube videos that are saved to a wishlist and volunteer audio describers select a video, write a script, record audio clips, and edit clip placement to create an audio description. The audio description tracks are stored separately and played together with the YouTube video then posted for public view at [YouDescribe](https://youdescribe.org/)

The YuWA dataset covers a vast domain of videos in 15  titled categories including Film & Animation, Music, Autos & Vehicles, Travel & Events, Pets & Animals, Sports, People & Blogs, Gaming, Comedy, Entertainment, How-To & Style, News & Politics, Nonprofits & Activism, Education, Science & Technology. A video can have multiple audio descriptions and an audio description can have multiple audio clips recorded by volunteer describers. The audio clips recorded before May, 2020 were transcribed using Listen By Code and the audio clips recorded after that are transcribed using Google Cloud Speech to Text API. Viewers can rate the audio descriptions on a scale ranging from 1-5 (1 being poor, 5 being excellent). Viewers can also provide feedback to the describers by selecting some improvements from the list. 

The YuWA data repository includes all YouDescribe related audio descriptions from 2013-2022 and can be sorted to include or exclude important YouDescribe milestones. We have focused on data collected by YouDescribe since March 17, 2017 and Google Analytics data which started tracking traffic since July 30, 2020.  This scalable dataset will be regularly updated as new videos, audio descriptions and audio clips gets uploaded. 

## Run Instructions
The `download_yd_data.py` file was tested using Python 3.9. So, please make sure that when you use `python`, your Python version is at least Python 3 or make sure you specify `python3`.


1. Install the requests module:

```bash
pip install requests

# If using python3
pip3 install requests
```

2. Run the python file:

```bash
# The default configuration will store the audio clips in the current directory
# separated by YouTube video ID and Audio Description ID.
# --audioDescDir: This option allows you to specify the output directory where
#                 the audio clips will be stored.

python download_yd_data.py

# If specifying python3
python3 download_yd_data.py

# Specify output directory
python download_yd_data.py --audioDescDir=<PATH_TO_OUTPUT_DIR>
```




## Data Analysis


<b> Audio Descriptions Yearly </b>

<p align="center">
  <img width="620" height="400" alt="Audio Descriptions Yearly" align="center" src="https://user-images.githubusercontent.com/59475801/198155956-78d80916-81ad-4f64-b579-740dd79f4210.png">
</p>
<p align="center"> March 17, 2017 - December 31, 2021 </p>


<b> Audio Descriptions Grouped by Year and Month </b>

<p align="center">
  <img width="900" height="450" alt="Audio Descriptions Grouped by Year and Month" align="center" src="https://user-images.githubusercontent.com/59475801/198099798-febff3b8-0251-47f9-92dc-13ff794d85ef.png">
</p>
<p align="center"> March 17, 2017 - September 21, 2022 </p>


<b> Premium dataset - Number of New and Existing Descriptions by year </b>

<p align="center">
  <img width="900" height="450" alt="Premium dataset - Number of New and Existing Descriptions by year" align="center" src="https://user-images.githubusercontent.com/59475801/198412337-5e4e63e6-99d4-4964-a940-b05872faa876.png">
</p>
<p align="center"> September 1, 2017 - August 31, 2022 </p>


<b> Premium dataset - Number of New and Existing Describers by year </b>

<p align="center">
  <img width="900" height="450" alt="Premium dataset - Number of New and Existing Describers by year" align="center" src="https://user-images.githubusercontent.com/59475801/198412472-f2cd9f9b-a9f7-4e91-bdcd-ea252fed0708.png">
</p>
<p align="center"> September 1, 2017 - August 31, 2022 </p>


<b> Percentage of Rated / Unrated Audio Descriptions </b>

<p align="center">
  <img width="354" alt="Percentage of Rated / Unrated Audio Descriptions" align="center" src="https://user-images.githubusercontent.com/59475801/204149790-2daa292c-582b-4a37-99e5-4bdc4b0add37.png">
</p>
<p align="center"> March 17, 2017 - September 21, 2022 </p>


<b> Audio Descriptions Ratings </b>

<p align="center">
  <img width="405" alt="Audio Descriptions Ratings (excellent to poor)" align="center" src="https://user-images.githubusercontent.com/59475801/204149848-731c2e06-c32f-4dac-b03b-d92e8744f21d.png"> 
</p>
<p align="center"> March 17, 2017 - September 21, 2022 </p>


<b> Statistics for Videos, Audio Descriptions and Audio Clips </b>

<p align="center">
  <img width="363" alt="Statistics for Videos, Audio Descriptions and Audio Clips" align="center" src="https://user-images.githubusercontent.com/59475801/195052435-ac1cc044-6a4d-45f3-bdb9-cab35e726cea.png">
</p>
<p align="center"> March 17, 2017 - September 21, 2022 </p>


<b> Audio Clips by Playback Type </b>

<p align="center">
  <img width="500" height="350" alt="Audio Clips by Playback Type" align="center" src="https://user-images.githubusercontent.com/59475801/198100077-45126cf7-d690-480d-90c1-a37c89e77d65.png">
</p>
<p align="center"> March 17, 2017 - September 21, 2022 </p>


<b> Described Videos in each YouTube video category </b>

<p align="center">
  <img width="621" alt="Described Videos in each YouTube video category" align="center" src="https://user-images.githubusercontent.com/59475801/195052683-4b44483d-d786-4630-9485-584b848a67b1.png">
</p>
<p align="center"> March 17, 2017 - September 21, 2022 </p>


<b> Audio Descriptions with Extended Audio Clips grouped by Video Category </b>

<p align="center">
  <img width="722" alt="Audio Descriptions with Extended Audio Clips grouped by Video Category" align="center" src="https://user-images.githubusercontent.com/59475801/198099072-6851df2a-fa93-43fb-8d60-3f48dc8f2ab5.png">
</p>
<p align="center"> March 17, 2017 - September 21, 2022 </p>


<b> Audio Descriptions with Inline Audio Clips grouped by Video Category </b>

<p align="center">
  <img width="722" alt="Audio Descriptions with Inline Audio Clips grouped by Video Category" align="center" src="https://user-images.githubusercontent.com/59475801/198099349-bd294387-54eb-4b17-ad97-db606b567cfe.png">
</p>
<p align="center"> March 17, 2017 - September 21, 2022 </p>


<b> Top 10 most requested videos </b>

<p align="center">
  <img width="722" alt="Top 10 most requested videos" align="center" src="https://user-images.githubusercontent.com/59475801/195052826-f5a8e179-b942-496f-8a3d-549f8141f16f.png">
</p>
<p align="center"> March 17, 2017 - September 21, 2022 </p>


<b> Wishlist videos for each YouTube video category </b>

<p align="center">
  <img width="718" alt="Wishlist videos for each YouTube video category" align="center" src="https://user-images.githubusercontent.com/59475801/195052975-85a62b6d-6b03-4cd1-b363-7c5690a156a4.png">
</p>
<p align="center"> March 17, 2017 - September 21, 2022 </p>


<b> Wishlist videos requested and described per year </b>

<p align="center">
  <img width="690" alt="Wishlist videos queued and described per year" align="center" src="https://user-images.githubusercontent.com/59475801/198350697-64e7a2b2-272e-44ff-a33f-789e3d31837c.png">
</p>
<p align="center"> March 17, 2017 - December 31, 2021 </p>


## Contributions

<p align="center">
  <img width="617" alt="The Smith-Kettlewell Eye Research Institute" align="center" src="https://user-images.githubusercontent.com/59475801/195065687-ae6605bd-f4e4-456d-87ef-8a3662144632.png">
</p>

<p align="center">
  <img width="1152" alt="San Francisco State University" align="center" src="https://user-images.githubusercontent.com/59475801/195056038-a862c4f8-4cf3-47d0-944d-843cc8d4d505.png">
</p>

<p align="center">
<img width="664" alt="Ability Central" align="center" src="https://user-images.githubusercontent.com/59475801/195056260-d0d90274-f1c7-4e9b-898c-cfb974e3fbc7.png">
</p>

## Meet the Team Members

| Team Member Name | Year | Role |
| :-------------: | :---: | :---: |
| Dr. Joshua Miele | 2013 - Present | YouDescribe Creator	|
| Charity Pitcher-Cooper | 2017 - Present | Product Manager	|
| Rodrigo Leme de Mello | 2017 - 2020 | Principal Software Engineer |
| Dr. Ilmi Yoon | 2018 - Present | Principal Investigator |
| Rupal Khilari	| 2016 - 2017 | Software Developer | 
| Andrew Taylor Scott	| 2019 - Present | Machine Learning Lead Engineer	|
| Dr. Yue-Ting Siu | 2013 - Present | Describer Trainer, Interface Design Researcher |
| Dr. Shasta Ihorn | 2020 - Present | User Study Researcher |
| Dr. Abhishek Das	| 2018 - 2020 | Machine Learning Engineer	|
| Yash Kant	| 2018 - 2020 | Machine Learning Engineer	|
| Umang Mathur | 2018 - 2020 | Software Developer	|
| Dr. Beste Yuksel | 2018 - 2020 | HCI Researcher |
| Jianfei Zhao | 2018 - 2020 | Software Developer	|
| Poorva Rathi | 2018 - 2020 | Software Developer	|
| Vaishali Bisht | 2018 - 2020 | Software Developer |
| Raya Farshad	|	2018 - 2020 |  |
| Jose Castanon	| 2018 - Present | Software Developer |
| Aditya Bodi	| 2018 - 2020 | Software Developer |
| Brenna Tirumalashetty | 2018 - 2020 |  |
| Manish Patil | 2018 - 2020 |	Software Developer	|
| Varun Sura	| 2020 - Present | iOS App Developer	
| Lothar Narins	| 2019 - Present  | Machine Learning Engineer | 	
| Bhavani Gorganthu	| 2021 - 2022  | YouDescribeX Web Interface |		
| Benjamin Kao	| 2022 - Present | Team Leader/Software Engineer |		
| Hirva Patel	| 2022 - Present | Software Developer |		
| Kishan Patel	| 2022 - Present | Mobile Developer	|
| Manali Seth	| 2022 - Present | Software/Data Engineer |
| Sanket Naik	| 2022 - Present | Software Developer |		
| Vishal Sharma	| 2022 - Present | Software Developer |
| Ishank Aggarwal | 2022 - Present | Machine Learning Engineer |		
| Caelen Wang	| 2022 - Present | Machine Learning Engineer |
| Kimon Monokandilos | 2022 - Present | Software Engineer |		



Dr. Joshua Miele	2013 - 2020	YouDescribe Creator
Charity Pitcher-Cooper	2017 - Present	Product Manager
Rodrigo Leme de Mello	2017 - 2020	Principal Software Engineer
Dr. Ilmi Yoon	2015 - Present	Principal Investigator
Rupal Khilari	2016 - 2017	Software Developer
Andrew Taylor Scott	2019 - Present	Machine Learning Lead Engineer
Dr. Abhishek Das	2018 - 2020	Machine Learning Engineer
Yash Kant	2018 - 2020	Machine Learning Engineer
Umang Mathur	2018 - 2020	Software Developer
Dr. Beste Yuksel	2019 - 2020	HCI Researcher
Jianfei Zhao	2018 - 2020	Software Developer
Poorva Rathi	2018 - 2020	Software Developer
Vaishali Bisht	2018 - 2020	Software Developer
Raya Farshad 2018 -2020 
Jose Castanon	2018 - 2022	Software Developer
Aditya Bodi	2018 - 2020	Software Developer
Brenna Tirumalashetty	2018 - 2020	
Manish Patil	2018 - 2020	Software Developer
Varun Sura	2020 - 2021	iOS App Developer
Lothar Narins	2019 - Present	Machine Learning Engineer
Bhavani Gorganthu	2021 - 2022	YouDescribeX Web Interface
Benjamin Kao	2022 - Present Team Leader/Software Engineer
Hirva Patel	2022 - Present Software Developer
Kishan Patel	2022 - Present	Mobile Developer
Manali Seth	2022 - Present Software/Data Engineer
Sanket Naik	2022 - Present Software Developer
Vishal Sharma	2022 - Present Software Developer
Ishank Aggarwal 2022 - Present Machine Learning Engineer
Caelen Wang	2022 - Present Machine Learning Engineer
Kimon Monokandilos 2022 - Present Software Engineer



# Licensing
You Described, We Archived ©️ 2022 by Smith-Kettlewell Eye Research Institute, San Francisco State University is licensed under CC BY-NC-ND 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-nd/4.0/


