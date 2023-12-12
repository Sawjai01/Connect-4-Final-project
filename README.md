# Connect-4-Final-project
Creator: Wesley Ng
Title: Connect 4 
Year: 2023


My project is Connect 4. It's a 2 player board game where you will need to have 4 piece in a row of circle blocks ( actual game ) to win the game. It can be vertically, horizontally, or diagonally. 

Section 1: Taking turns to drop the piece (x or o)
- However, in this case, we will use player 1 = x and player 2 = O. 
In my code. You can see I created a def function "turn". This function has a while loop where you want to drop the number in, which is in "columns", [1,2,3,4,5,6,7,]. If a user would enter incorrectly, they would need to input a number again. 

Section 2: Win-condition rule
- Created a function called "check_win". This ehecks if the win-condition for each player if they made the pieces 4 times in a row. However, in my code, I tried creating the win for vertically first, but somehow the code isn't running and it won't work. So I didn't give up on it, I just didn't know how and didn't have enough time to finish it. So, basically, the code is still there, but I skipped that part. 

Section 3: Creating the board (6 rows x 7 column)
- defined a function called "empty_board". This function creates the board and puts the elements in it. Created a loop so it can be used later on in the actual game.

Sectino 4: Playing the game
- Defined a function called "play_game". This is where we actually play the game. We call the function from the board game to open up the board. We start with player 1 first, always. Created a variable called "r" which is a row indicator that gets resetted per turn. A while loop, to display each players turn.
- In the play_game, we then, need to create a player where they can go up the row 1 by 1 without in a specific space only. Player 1 = x , player 2 = 0 and it switches players per turn until one wins(however, this doesn't work since the win-condition-rule that I created didn't work). We will then need to reset the row indicator and goes back to the while loop, again and again.

Journey through this project:
- At first I thought this project was going to be REALLY REALLY REALLY hard. . . and it was still. This was my first time creating a board game, so I had to go through resources/help to understand how to do it and how to start it. The difficulties I struggled most in this project, was actually going through which direction to start first and the horrendous feeling that the code wasn't working, really pissed me off. And I learned that just start it step by step and don't make your code look jumbled up. 
- Aside from struggling hard, I actually learned a lot in this project and overall this course in general. I enjoyed actually created this game, where I was like, " OH THIS IS HOW YOU DO IT. WAIT NEVERMIND THAT'S NOT HOW YOU DO IT. OHHHHH WHAT IF I DID THIS". It was quite a journey and I hated and loved every second of it. Although I couldn't finish this project that I envisioned on. I'm glad that I'm able to progress and learn from it.
- Recording my presentation was also what I hated the most. I have stage fright and I am EXTREMELY nervous in front of audience.
      - The recording you see: Me being very nervous, when you see a unsure pause(I was literally gulping because I can't stand hearing my own voice and recording myself infront of a audience. Afraid that I don't know what I'm talking about. 
      - But, I was glad it was including in this project because more practice makes me better at presenting, although in this case, I didn't really do well.

Overall, this journey was a cold/hot breeze. Enjoyed every hour/sec/min of it. 

URL link for the presentation: 
https://youtu.be/q65PZVmtC0I

  




