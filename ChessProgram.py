from sys import setrecursionlimit #Allows a change in recursion limit.

setrecursionlimit(15000)  #WARNING This recursion limit is very high. I checked multiple times to make sure my machine and system could handle this
                          # and this is about the highest it would go without crashing (I did this on repl.it, so it may be more than my computer could handle
                          #on its own. Therefore, if someone happens to want to look at this. It would be a good idea to lower this to a reasonable value otherwise
                          #it might crash. You will need to change the code though, because even trying to half the amount of recursion (seen in using two halves
                          # down when I call the function, it still needs about a recursion limit of 13000. If lower than that, you will have to change that part
                          # of the code a bit to fit. I wanted to do more with that, but I realized going down that road of trying to make less recursion was really
                          # just doing it iteratively, which I didn't want. So, that is just some info on that.

#Simply initializing some values I'll need later. 'values' will be the number of ways to get from the original place to the end,
#cvalue is just an intermediate variable to help with navigating the squares (and the stack I have later)
#recursiondepth is just used if I am debugging and optimizing how much recursion the program does
#oldina and oldinb are what I used to keep track of the original input inside the function when it is calling itself with different inputs all the time
#positionstack is what I use to fully navigate the chess board. I basically use it to push down one path until the end and then pop out of it
#until I can go down another path.
values = 0
cvalue = []
for i in range(9):
  cvalue.append([])
  for j in range(9):
    cvalue[i].append([])
    cvalue[i][j].append(False)
    cvalue[i][j].append(False)
recursiondepth = 0
oldina = 0
oldinb = 0
positionstack = []
positionstack.append(0)

#just taking the input and parsing out what I want from the input format

inp = input()
origcoora = int(inp[1])
origcoorb = int(inp[3])
inpa = int(inp[6])
inpb = int(inp[8])

def function(a, b):
  global values
  global positionstack
  
  #Basically, I am seeing if I am calling the function a new time or not (because I make positionstack = 0 when I end the function)
  #and then if I am, setting up some stuff and starting the stack, and if not, just adding whatever position on the board I am to the stack
  if positionstack[0] != 0:
    if (positionstack[-1] != [a, b]):
      positionstack.append([a, b])
  elif positionstack[0] == 0:
    values = 0
    global oldina
    global oldinb
    oldina = a
    oldinb = b
    positionstack = []
    positionstack.append([a,b])
  
  global recursiondepth  #for debugging purposes
  recursiondepth += 1    #same
  
  if (a==origcoora and b==origcoorb): #Basically, if (as I am solving backwards) the spot on the board is the original starting spot
    values += 1                       #Then, add one to values (the number of paths), delete this value I am at on the stack
    positionstack.pop()               #and go back to the last value on the stack
    newa = positionstack[-1][0]
    newb = positionstack[-1][1]
    function(newa, newb)
  
  if (a-1) < origcoora:
    cvalue[a][b][0] = True            #cvalue is used to see if I have gone down the path (so I don't go down it twice) and this just
  if (b-1) < origcoorb:               #tells it to also mark that I have gone down the path if that potential path is outside the bounds of the problem at hand
    cvalue[a][b][1] = True
  if (cvalue[a][b][0] == True):       #If going left (again, solving in reverse here) is blocked
    if (cvalue[a][b][1] == False):    #and going down isn't
      cvalue[a][b][1] = True          #going down is now blocked for the future
      function(a, (b-1))              #go down
    else:                             #otherwise (if going left and going down are blocked)
      if(a == oldina and b == oldinb):#if the present coordinates are the far right and top coordinate (the spot I am trying to get to (really, I'm coming from there)
        positionstack = []            #so basically, if every pathway is blocked and I am at the farmost coordinate, it has finished
        positionstack.append(0)       #so I just reset positionstack so that it can be used again (cause I have to call two halves of the problem so recursion depth isn't a problem)
        return values                 #and return the number of paths so that I can print it later
      elif(b == inpb and a != inpa):  #if going left and going down are blocked, and I am as far up as I can go, but not as far right
        if len(positionstack) == 0 or len(positionstack) == 1: #sometimes I'd get a weird error where it didn't realize it matched, so this just fixed that 
          return values
        positionstack.pop()           #go back to the previous position (which would be to the right. Don't know why I was forced to create this scenario)
        newa = positionstack[-1][0]   #same process                                                   I shouldn't have needed, but it fixed errors, so, whatever)
        newb = positionstack[-1][1]   #etc.
        cvalue[a][b][0] = False       #etc.  (This part is just making it so if I encounter this square again, it won't be blocked, because I'll have come from a different square farther up
        cvalue[a][b][1] = False
        function(newa, newb)          #you get the point
      else:      #otherwise (if going left and down is blocked but we aren't at the top value) (again, didn't know why I needed the previous part, but it worked, so hey)
        cvalue[a][b][0] = False       #same as before
        cvalue[a][b][1] = False
        if len(positionstack) == 0 or len(positionstack) == 1:
          return values               #same error correction deal here
        positionstack.pop()           #same going back to previous position, etc. etc.
        newa = positionstack[-1][0]
        newb = positionstack[-1][1]
        function(newa, newb)
  elif (cvalue[a][b][0] == False):    #otherwise, if going left isn't blocked
    cvalue[a][b][0] = True            #block going left for this square
    function((a-1), b)                #go left on the path
  else: print("Error")                #if some other thing happens, error (this has never happened)
  return values                       #in case the other return values doesn't work (happens sometimes)

print(function(inpa-1, inpb) +function(inpa, inpb-1))   #basically, just doing the function twice for the two squares around the target square
                                                        #because going from 1,1 to 8,8 required too much recursion, so this splits it up
                                                        #because adding the distance for a-1, b and a, b-1 is the same as going to a,b

  
