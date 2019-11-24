# why not tell the person what's about to happen?
print("This output will give instructions for solving")
print("a Tower of Hanoi with n discs.")

def solve_hanoi(n, start_peg, end_peg):

    #move disks 1 through n from start_peg
    #to end_peg
    #calculate what the spare peg is
    spare_peg = 6 - start_peg - end_peg
    if n==1:
        print ("Move disk 1 from peg " + str(start_peg) +" to peg " +str(end_peg)+".")
        return
    while n>=2:
        solve_hanoi(n-1, start_peg, spare_peg)
        print("Move disk "+str(n)+" from peg " + str(start_peg) + " to peg " + str(end_peg) +".")
        solve_hanoi(n-1,spare_peg,end_peg)
        n = n-2
    return

solve_hanoi(5,1,2)


    # #discs  #moves
      #1        1
      #2        3  (2^2-1)
      #3        3+1+3 = 7 (2^3-1)
      #4        7+1+7 = 15 (2^4-1)
      #5        15+1+15 = 31 (2^5-1_
    #therefore there will be 7 moves for this exercise
      #goal- sort the list

    #result should look like this:

#for n=4
# Move disk 1 from peg 1 to peg 3.
# Move disk 2 from peg 1 to peg 2.
# Move disk 1 from peg 3 to peg 2.
# Move disk 3 from peg 1 to peg 3.
# Move disk 1 from peg 2 to peg 1.
# Move disk 2 from peg 2 to peg 3.
# Move disk 1 from peg 1 to peg 3.
# Move disk 4 from peg 1 to peg 2.
# Move disk 1 from peg 3 to peg 2.
# Move disk 2 from peg 3 to peg 1.
# Move disk 1 from peg 2 to peg 1.
# Move disk 3 from peg 3 to peg 2.
# Move disk 1 from peg 1 to peg 3.
# Move disk 2 from peg 1 to peg 2.
# Move disk 1 from peg 3 to peg 2.