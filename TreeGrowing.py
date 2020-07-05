# imports libraries
import time, math, random

programRunning = 0
# makes it so it can loop program over and over
while programRunning == 0:
    # selection screen
    print("""Choose a number below:
1 - Oak Tree
2 - Birch Tree
3 - Bamboo""")
    treeType = int(input())

    # sets tree data
    if treeType == int(1):
        treeNum = 10000000
        treeGrowthMultiplier = random.uniform(0.5, 2.0)
    elif treeType == int(2):
        treeNum = 50000000
        treeGrowthMultiplier = random.uniform(0.2, 1.2)
    elif treeType == int(3):
        treeNum = 255000000
        treeGrowthMultiplier = random.uniform(0.087, 1.211)
    # messing around with more custom things
    elif treeType == int(1616):
        treeNum = time.time()
        treeGrowthMultiplier = 1
    else:
        print("Invalid Input")
        treeNum = 0
        treeGrowthMultiplier = 0


    # Events
    eventGrade = "Y"
    treeEventMultiplier = float(1)
    event = random.choice((
        "winter", "deforestation", "forest_fire", "team_trees", 
        "fertilizer", "perfect_weather", "flood", 
        "rain", "nothing"))
    if event == "winter":
        print("Winter has strucken!")
        treeEventMultiplier = float(2)
    elif event == "deforestation":
        print("Your tree has been chopped down due to deforestation!")
        eventGrade = "N"
        treeEventMultiplier = float(0)
    elif event == "forest_fire":
        print("Your tree has burned down due to a forest fire!")
        eventGrade = "N"
        treeEventMultiplier = float(0)
    elif event == "team_trees":
        print("#TeamTrees")
        treeEventMultiplier = float(0.82)
    elif event == "fertilizer":
        print("Your tree has been fertilized")
        treeEventMultiplier = float(0.94)
    elif event == "perfect_weather":
        print("Perfect Weather!")
    elif event == "flood":
        print("Flooding has occured!")
        treeEventMultiplier = float(2.42)
    elif event == "rain":
        print("It has started raining!")
        treeEventMultiplier = float(0.98)

    # Global Calculations
    treeGrown = float(round(treeNum*treeGrowthMultiplier*treeEventMultiplier, 2))
    treeGrowth = 0

    # In Progress: Tree Display
    treeDisplayQuarters = round(treeGrown/4, 0)
    quarterCount = 0
    quarterCurrent = 0
    printBreak = """
    """
    time.sleep(2.1)
    # starts timer
    timerStart = time.time()
    if treeNum > 0:
        # loop system
        while treeGrowth < treeGrown:
            treeGrowth = treeGrowth + 1
            quarterCount = quarterCount + 1
            # checks and only posts if number is divisible by 100k
            #if treeGrowth % 100000 == 0:
            #    print(treeGrowth)
            if quarterCount == 1 and quarterCurrent == 0:
                print("""






      ()
                """)
                quarterCurrent = 1
                quarterCount = 0
            if quarterCount == treeDisplayQuarters and quarterCurrent == 1:
                print(50*printBreak)
                print("""



    __
   (  )
    ||
    ||
                """)
                quarterCurrent = 2
                quarterCount = 0
            if quarterCount == treeDisplayQuarters and quarterCurrent == 2:
                print(50*printBreak)
                print("""


    ____
   (    )
    |  |
    |  |
   /    \ 
                """)
                quarterCurrent = 3
                quarterCount = 0
            if quarterCount == treeDisplayQuarters and quarterCurrent == 3:
                print(50*printBreak)
                print("""
   _ _ _
 (\  |  /)  
  (\ | /)
    | |
    | |
    | |
    | |

                """)
    # stops timer
    timerStop = time.time()

    # calculuates the time taken
    timer = round(timerStop - timerStart, 2)

    # prints statistics
    if eventGrade == "Y" and treeNum > 0:
        print(timer, "seconds")
        print(treeNum, "Base Tree Growth", timer, "Timer", treeGrowthMultiplier, 
            "Tree Growth Multiplier", treeGrown, "Full Tree Grown", 
            treeEventMultiplier, "Event Multiplier", sep=" | ")
    if eventGrade == "N":
        print("")
    # looping thing
    programRun = input("Would you like to play again? (Y/N): ")
    if programRun == "Y":
        print("")
    elif programRun == "N":
        exit()
    else:
        print("")
