# So there were a few gramatical things that I made adjustments too, also I dont know if its something that you guys would 
#to do or change but for the request string prompts maybe put keywords to type in caps so the player has a hint as to what the
#command could be because that was a little difficult if I couldn't see the code.  

#Christopher Barbarick, Joshua Anaya, and Evan Cristensen Final Project CST 205
def escapeGame():
  north = false
  south = true
  east = false
  west = false
  hid = false
  win = false
  items = []
  chair = true
  tp = true
  key1 = false
  key2 = false
  ch = false
  chs = false
  
  #be sure to adjust the directory according to your locations before playing
  bt = makePicture("G:\\Final Project\\Final Project\\bear-trap.jpg")
  chest = makePicture("G:\\Final Project\\Final Project\\chest.jpg")
  tiles = makePicture("G:\\Final Project\\Final Project\\floor-tiles.jpg")
  hshelf = makePicture("G:\\Final Project\\Final Project\\high shelf.jpg")
  pbed = makePicture("G:\\Final Project\\Final Project\\prison bed.jpg")
  study = makePicture("G:\\Final Project\\Final Project\\study.jpg")
  tapestry = makePicture("G:\\Final Project\\Final Project\\tapestry.jpg")
  bsnap = makeSound("G:\\Final Project\\Final Project\\beartrap snap.wav")
  bboxes = makeSound("G:\\Final Project\\Final Project\\breaking boxes.wav")
  dcreak = makeSound("G:\\Final Project\\Final Project\\door_creak.wav")
  btmetal = makeSound("G:\\Final Project\\Final Project\\metal beartrap.wav")
  nm = requestString("Let's play ESCAPE (Enter the name of the player)")
  rm = " "
  
  #gramatical errors in the begining
  showInformation("(Version 1.00) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn't know where they are or how long it has been. But "+str(nm)+" does know that they have to get out somehow?")
  while rm != "exit": #exit will exit the game
  
    #South Room
    if south == true and north == false and east == false and west == false:
      show(pbed)
      play(dcreak)
      rm = requestString("The room is small with only a bedframe and a small spring mattress, with some springs on the side of the bed in sight.\n It feels like those rooms you see torture victims live in from cop shows and movies. There is a door opposite of the bed.  \n Do you Wish to LEAVE?").lower()
      if rm  == "leave" or rm == "yes":
        south = false
      elif rm == "help":
       showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there. "+ str(nm)+" doesn\'t know where they are or how long it has been. But "+str(nm)+" dooes know that they have to get out somehow?")
      
      else:
       rm = requestString("Please try again.").lower()
       
    #North Room
    if south == false and north == true and east == false and west == false:
      show(tiles)
      rm = requestString("There is a window in the room but it is too tall for you to reach and see out of. \n Day light is peering into the room. This room\'s floor has some tiles that\n look as though they were recently changed. Do you want to leave?").lower()
      if rm == "leave" or rm == "yes":
        north = false
      elif rm == "items":
        showInformation("All items in your possession are shown in the command area")
      elif rm == "help":
       showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
        #you need to type "use scalpel" and also have the scalpel
      elif rm == "use scalpel" and "scalpel" in items:
        showInformation("You found a box, but its locked. If you have a key, try using it.")
      elif rm == "use key" and "key2" in items:
        items.append("O")
        print items
        showInformation("The key opened the box and the letter O was inside. This will be kept with your other items.\nGo to the center room and enter \"secret\"")
      elif rm == "use key" and "key1" in items and "key2" == false:
        showInformation("This key did not work. Maybe there is another.")
      else:
        requestString("Wrong Command! Please try again.").lower()
        
    #East room contains a bear trap that will trap the player and end the game
    #but it will only end the game if you have obtained the scalpel       
    if south == false and north == false and east == true and west == false:
      if key1 == false:
        rm = requestString("The foul smell you were smelling in the last room is coming from something in the corner.\n It looks like an animal corpse, though it is hard to tell what it is due to being mangled and decayed. \n There seems to be a pile of animal paws littered around  open bear traps.\nThere seems to be a key attached to a letter under the corpses. \n But you dont know if that thing will help you escape?\n You should try to use somthing to move them with something other than your hand. \n Do you want to leave the room?").lower()
      elif key1 == true:
        rm = requestString("The foul smell you were smelling in the last room is coming from something in the corner.\n It looks like an animal corpse, though it is hard to tell what it is due to being mangled and decayed. \n There seems to be a pile of animal paws littered around  open bear traps. \n But you dont know if that thing will help you escape?\n You should try to use somthing to move them with something other than your hand. \n Do you want to leave the room?").lower()
      if rm == "leave" or rm == "yes":
        east = false
      elif rm == "south":
        south = true
      elif rm == "north": 
        north = true
      elif rm == "take key":
        items.append("key1")
        key1 = true
        items.append("T")
        showInformation("You found the letter T and a key. If only we knew what the key was for.")  
      elif rm == "use scalpel" and "scalpel" in items:
        show(bt)
        play(btmetal)
        play(bsnap)
        showInformation(" You use the scalpel to try to move the paws and \n*SNAP*\n The trap closes and you are now stuck, bleeding. \nYou try to move and another bear trap falls onto your head. \n*SNAP!*\n GAME OVER")
        break
      elif rm == "items":
        print items
        showInformation("All items in your possession are shown in the command area")
      elif rm == "help":
       showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
      else:
        requestString("Wrong Command! Please try again.").lower()
        
    #West room has an object, a scalpel
    #it is used to escape the main room ,get you caught in the bear trap, and get get a key from behind the tapestry  
    if south == false and north == false and east == false and west == true:
      if "scalpel" in items:
        rm = requestString("There is a metal stand at the center with a tray of surgical equipment sitting on top. \n Some appear to be rusted, while others looked like they have just been sterilized.\n Do you want to leave this room?").lower()
      else:
        rm = requestString("There is a metal stand at the center with a tray of surgical equipment sitting on top. \n Some appear to be rusted, while others looked like they have just been sterilized.\n A bright light is coming from the ceiling and is being reflected into your eyes by one of the tools on the stand, a scalpel. \n Do you want to leave this room?").lower()
      if rm == "leave" or rm == "yes":
        west = false 
      elif rm == "south":
        south = true
      elif rm == "north": 
        north = true 
      elif rm == "take scalpel":
        items.append("scalpel")
        showInformation ("You walked to the table and picked up the shiny scalpel. This might come in handy later.")
      elif rm == "items":
        print items
        showInformation("All items in your possession are shown in the command area")
      elif rm == "help":
       showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
      else:
        requestString("Wrong Command!Please try again.").lower()
        

    #SouthWest Room
    if south == true and north == false and east == false and west == true:
      if chair == true: 
        show(study)
        rm = requestString("There is a broken table and an old chair near a book case, this seemed to be a small\n library or study. There is something on top of the book case. You can\'t reach it without a\n boost. Do you want to go back to the room you came from?").lower()
      elif chair == false:
        rm = requestString("There is a broken table near a book case,\nthis seemed to be a small library or study.").lower()
      if rm == "leave" or rm == "yes":
        south = false
      elif rm == "use chair":
        chair = false
        items.append("P")
        play(bboxes)
        showInformation("You put the chair near the bookcase to reach he box. After grabbing the box\n and stepping down, the chair breaks and the chairleg \nlands next to you. You also grabbed the letter P from the book case.\n this will be added to your items.")
      elif rm == "take chairleg":
        items.append("chairleg")
        showInformation("This chairleg could be used to extend my reach.")
      elif rm == "items":
        print items
        showInformation("All items in your possession are shown in the command area")
      elif rm == "help":
        showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
      else:
        requestString("Wrong Command!Please try again.").lower()
        
    #NorthWest Room
    if south == false and north == true and east == false and west == true:
      if tp == true:  
        show(tapestry)
        rm = requestString("There is a tapestry on a wall in the corner of the room.\n It is very long and written in a language you cannot read.\n After closer inspection there is a bulge in the middle of the tapestry.\n The holder of the tapestry looks heavy and not sturdy.\n Moving it might make it fall.").lower()
      if tp == false:
        rm = requestString("There is a metal bar hanging on the wall and a hole in the wall under the metal bar.")        
      if rm == "leave" or rm == "yes":
        north = false  
      elif rm == "use scalpel":
        items.append("Y")
        tapestry = false
        showInformation("You used the scalpel to cut the tapestry,\n revealing another block letter,Y. This will be\nadded to your items.")
      elif rm == "items":
        print items
        showInformation("All items in your possession are shown in the command area")
      elif rm == "help":
        showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
      else:
        rm = requestString("Wrong Command!Please try again.").lower()


    #NorthEast Room
    if south == false and north == true and east == true and west == false:
      if ch == false:
        show(chest)
        rm = requestString("There is a chest in this room. It seems to be locked. Maybe a key will open it... Do you want to go back to the room you came from?").lower()
      elif ch == true:
        rm = requestString("There is an open chest in this room but nothing else. \nDo you want to go back to the room you came from?").lower()  
      if rm == "leave" or rm == "yes":
        north = false  
      elif rm == "use key" and "key1" in items:
        ch = true
        items.append("H")
        items.append("key2")
        showInformation("The key found in side the paw on top of the bear trap fits perfectly in this chest, inside the chest is a block letter H and another key.")
      elif rm == "items":
        print items
        showInformation("All items in your possession are shown in the command area")
      elif rm == "help":
        showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
      else:
        requestString("Wrong Command!Please try again.").lower()

    #SouthEast Room
    if south == true and north == false and east == true and west == false:
      if chs == false:
        show(hshelf)
        rm = requestString("Looking around, there is not much in this room.\nWhen you turn around, there is a small lock box on top of a shelf that is too high and out of your reach.").lower()
      elif chs == true:
        rm = requestString("There is an open box on the ground, but nothing else.\nDo you want to go back to the room you came from?").lower()   
      if rm == "leave" or rm == "yes":
        south = false  
      elif rm == "use chairleg" and "chairleg" in items:
        chs = true
        items.append("N")
        play(bboxes)
        showInformation("You knocked the box off the shelf with the chairleg! It\nbroke as it hit the floor and a block letter N fell out.\nYou picked it up, and it is now one of your items.")
      elif rm == "items":
        print items
        showInformation("All items in your possession are shown in the command area")
      elif rm == "help":
        showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn?t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
      else:
        requestString("Wrong Command!Please try again.").lower()



    #this room is the center and will get you to each room. 
    if south == false and north == false and east == false and west == false and hid == false:
        rm = requestString("This room is full of clutter and dirt. \n The walls seemed to be stained and torn linen lie in the corner. \n Attatched to the wall are a set of rusted shackles, they seem to be warm.\n  There seems to be a foul odor but you cannot figure out where it is coming from.\n There are doors on all sides of you. One for each direction with the room with the bed being to the south.\n Which direction do you want to enter? North, South, East, or West.").lower()
        if rm == "south":
          south = true
        elif rm == "north":
          north = true
        elif rm == "east":
          east = true
        elif rm == "west":
          west = true
        elif "P" in items and "Y" in items and "T" in items and "H" in items and "O" in items and "N" in items and rm == "secret":
          print items
          count = 0
          ans = requestString("What is the secret word?").lower()
          print ans
          while count < 4:
            if ans == "python":
              win = true
              play(dcreak)
              showInformation("You WIN! You have Escaped!")
              break
            else:
              count += 1
              requestString("Please try again. %d tries out of 5 used." % count).lower() 
        elif rm == "items":
          print items
          showInformation("All items in your possession are shown in the command area")
        elif rm == "help":
          showInformation("(alpha version .03) What is going on? " +str(nm)+" has awoken in a room with no memory of how they got there."+ str(nm)+" doesn\'t know where they are or how long it has been. But "+str(nm)+" do know that they have to get out somehow?")
        else:
          requestString("Wrong Command! Please try again.").lower()
  #if you lose, this text will show
  if win == false:
    showInformation("Thanks for playing ESCAPE")