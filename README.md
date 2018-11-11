# SmashFrameCalculator_Ultimate
Calculates the frame data of a move based on given timestamps. Compares Ultimate frame data to Smash 4 framedata

**NOTE. DOES NOT SUPPORT LANDING LAG AND AUTOCANCELS F AERIALS CURRENTLY**

<h2> REQUIRES PYTHON </h2>

<h1> Setup </h1>
  
Download create_FAF_script.py and frame_data.txt and place them in a folder of your choice
Edit frame_data.txt to fit the format listed below and then run create_FAF_script.py

The script will create a summary.txt containing an outline of all the moves as well as a folder full of txt files that go over the specific changes.

<h1> Format </h1>

`NAME STARTING_TIME IMAGELINK HIT_TIME IMAGELINK FAF_TIME IMAGELINK ORIGINAL_FIRST_HITFRAME ORIGINAL_FAF AERIAL_FLAG NOTES`

<h2> Explainations </h2>
  
**NAME**
  Simply the name of the move. Must have NO SPACES (i.e "DThrow")
  
**STARTING_TIME**
  Time the animation started. Formatted as M.SS.XX, M being minute, SS being seconds, and XX being centiseconds (i.e 2:50.60 would just be 2.50.60)
  
**IMAGELINK**
  Simply a link to the timestamp. If you dont' want to include an image (as all it does is reprint the URL), just put 'X' or some other text
  
**HIT_TIME**
  Time when the move has a first hitbox. Formatted as M.SS.XX, M being minute, SS being seconds, and XX being centiseconds (i.e 2:50.60 would just be 2.50.60)
  
**FAF_TIME**
  Time when the character can act out of a move. Formatted as M.SS.XX, M being minute, SS being seconds, and XX being centiseconds (i.e 2:50.60 would just be 2.50.60)
  
**ORIGINAL_FIRST_HITFRAME**
  Frame the move hits in Smash 4 (i.e "14" for Palu's DTilt)
  
**ORIGINAL_FAF**
  Frame the character can act out of the move (i.e "40" for Palu's DTilt)
  
**AERIAL_FLAG**
  For Aerials in the future. For now, put 0
  
**NOTES**
  Whatever ever you want to put, like notes about the footage or move
  
  <h2> Example for Palu's DTilt: </h2>
  
`DTilt 2.17.60 https://i.imgur.com/XtJoXCI.png 2.17.36 https://i.imgur.com/U4HBA2y.png 2.16.95 https://i.imgur.com/Op26Ian.png 14 40 0 Footage suffers from ghosting at this segment. Will probably have to redo`
