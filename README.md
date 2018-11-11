# SmashFrameCalculator_Ultimate
Calculates the frame data of a move based on given timestamps. Compares Ultimate frame data to Smash 4 framedata
**NOTE. DOES NOT SUPPORT LANDING LAG AND AUTOCANCELS F AERIALS CURRENTLY**

Format goes as follows

NAME STARTING_TIME IMAGELINK HIT_TIME IMAGELINK FAF_TIME IMAGELINK ORIGINAL_FIRST_HITFRAME ORIGINAL_FAF AERIAL_FLAG NOTES

NAME
  Simply the name of the move. Must have NO SPACES (i.e "DThrow")
STARTING_TIME
  Time the animation started. Formatted as M.SS.XX, M being minute, SS being seconds, and XX being centiseconds (i.e 2:50.60 would just be 2.50.60)
IMAGELINK
  Simply a link to the timestamp. If you dont' want to include an image (as all it does is reprint the URL), just put 'X' or some other text
HIT_TIME
  Time when the move has a first hitbox. Formatted as M.SS.XX, M being minute, SS being seconds, and XX being centiseconds (i.e 2:50.60 would just be 2.50.60)
FAF_TIME
  Time when the character can act out of a move. Formatted as M.SS.XX, M being minute, SS being seconds, and XX being centiseconds (i.e 2:50.60 would just be 2.50.60)
ORIGINAL_FIRST_HITFRAME
  Frame the move hits in Smash 4 (i.e "14" for Palu's DTilt)
ORIGINAL_FAF
  Frame the character can act out of the move (i.e "40" for Palu's DTilt)
AERIAL_FLAG
  For Aerials in the future. For now, put 0
NOTES
  Whatever ever you want to put, like notes about the footage or move
  
