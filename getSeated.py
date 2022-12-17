def getSeated(seatType):
    global currentPassenger                          # making it global to know which passenger is waiting to be seated
    for row in range(passengers):
        ok=False
        if seatType == 'Window':                     # if its windows then either the leftmost or the right most has to be seated
            if currentPassenger>passengers:
                break
        
            if row < len(seats[0]):            
                seats[0][row][0]=currentPassenger
                currentPassenger+=1
                ok=True
            
            if (row < len(seats[n-1])) and (currentPassenger <= passengers): 
                rightWindowSeat = len(seats[n-1][0])-1
                seats[n-1][row][rightWindowSeat]=currentPassenger
                currentPassenger+=1
                ok=True
        
            if ok==False: 
                break
            
            continue
            
        if currentPassenger > passengers: 
            break
        for column in range(n):
            if currentPassenger > passengers: 
                break
            if row>=len(seats[column]): 
                continue
            ok=True;
            for currentSeat in range (len(seats[column][0])):
                if currentPassenger > passengers: 
                    break

                if seatType == 'Centre':
                    if (currentSeat>0) and (currentSeat<len(seats[column][0])-1):
                        seats[column][row][currentSeat]=currentPassenger
                        currentPassenger+=1
                    continue
                  
                canSeat = (currentSeat==0 and column>0) or (currentSeat+1==len(seats[column][0]) and column<n-1)
                if (seatType == 'Aisle') and canSeat == True:
                    seats[column][row][currentSeat]=currentPassenger
                    currentPassenger+=1
        
    
        if ok==False: 
            break



    


passengers= int(input())         # total number of passengers as input
n = int(input())                 # taking total number of 2D list as input
seats = []                       # making aeroplane seats in a 3D list
for x in range(n):
    seats.append([])
    a=int(input())
    b=int(input())
    for y in range(b):
        seats[x].append([])
        for z in range(a):
            seats[x][y].append(0)

currentPassenger=1              # passenger which is wating to get seated
getSeated('Aisle')              # first Aisle seats are filled
getSeated('Window')             # then window seats are filled
getSeated('Centre')             # at last centre seats are filled with the helper funtion
seats
