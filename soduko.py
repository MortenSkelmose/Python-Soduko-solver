#!/usr/bin/env python
import copy



class Board(object):
    def __init__(self):
        """ [row][column] """
        self.partial_solution = []
        self.original = False
        self.numbers = 0
        self.rownumbers = [0,0,0,0,0,0,0,0,0]
        self.colnumbers = [0,0,0,0,0,0,0,0,0]
        self.order = []
        self.ordertype = []
        for i in range(9):
            self.partial_solution.append([0,0,0,0,0,0,0,0,0])
        pass


    def orderStartState(self):
        taken = {'row' : [], 'col' : []}
        ordertype = ''
        j=0
        while j < self.numbers:
            no = 0
            val = 0
            for i in range(9):
                if self.rownumbers[i] > val and not (i in taken['row']):
                    val = self.rownumbers[i]
                    no = i
                    ordertype = 'row'
                elif self.colnumbers[i] > val and not (i in taken['col']):
                    val = self.colnumbers[i]
                    no = i
                    ordertype = 'col'
            self.order.append(no)
            self.ordertype.append(ordertype)
            taken[ordertype].append(no)
            j += 1
        pass


    def putNumber(self,x,y,number,original=False):
        if self.isValid(x,y,number):
            self.partial_solution[x][y] = number
            if original:
                self.rownumbers[x] += 1
                self.colnumbers[y] += 1
            self.numbers += 1
            return True
        else:
            return False


    def numberOfNumbers(self):
        return self.numbers

    def isValid(self,x,y,number):
        return self.checkRowFor(x,number) and self.checkColumnFor(y,number)
        
    def checkRowFor(self,row,number):
        for i in range(9):
            if self.partial_solution[row][i] == number:
                return False
        return True

    def checkColumnFor(self,col,number):
        for i in range(9):
            if self.partial_solution[i][col] == number:
                return False
        return True
        pass


    def getHighestCol(self):
        highcol = 0
        highval = 0
        for idx,col in enumerate(self.colnumbers):
            if col > highval:
                highcol = idx
                highval = col
        return idx, highval
        pass


    def getHighestRow(self):
        highrow = 0
        highval = 0
        for idx,row in enumerate(self.rownumbers):
            if row > highval:
                highrow = idx
                highval = row
        return idx, highval
        pass

    def getNextOriginal(self):
        for typ, index in zip(self.ordertype, self.order):
            if typ == 'row':
                for i in range(9):
                    if self.partial_solution[index][i]  == 0:
                        return index,i
            else:
                for i in range(9):
                    if self.partial_solution[i][index]  == 0:
                        return i,index
        self.original = True
        return 0,0
        pass

    def getNext(self):
        if not self.original:
            x,y = self.getNextOriginal()    
            if not self.original:
                return x,y
        if self.original:
            i=0
            j=0
            for i in range(9):
                for j in range(9):
                    if self.partial_solution[i][j]  == 0:
                        return i,j
        return 8,8

    def complete(self):
        if self.numbers == 81:
            return True
        else:
            return False

    def __str__(self):
        lines = ""
        for i in range(9):
            line = ""
            for j in range(9):
               line += ("{0} ".format(self.partial_solution[i][j]))
            lines += "{0}\n".format(line)   
        return lines

def solver(solution):
    x,y = solution.getNext()
    new_solutions = []
    for i in range(9):
        new_solution = copy.deepcopy(solution)
        if new_solution.putNumber(x,y,i+1):
            new_solutions.append(new_solution)

    return new_solutions

    

class Soduko(object):
    def __init__(self):
        self.iterations = 0
        self.solutions = [] 
        self.complete_solutions = []
        self.best_solution = Board() 
        solved = False

    def addSolution(self, solution):
        self.solutions.append(solution)

    def printSolutios(self):
        for solution in self.complete_solutions:
            print(solution)

    def solve(self):
        self.solutions[0].orderStartState()
        print('Starting board: \n')
        print(self.solutions[0])
        while len(self.solutions) > 0:
            partial = self.solutions.pop()

            new_solutions = solver(partial)

            for solution in new_solutions:
                self.iterations += 1
                if solution.numberOfNumbers() > self.best_solution.numberOfNumbers():
                    self.best_solution = solution
                if solution.complete():
                    self.complete_solutions.append(partial)
                    print("Partial solutions found: \n")
                    print(partial)
                    print("Number of iterations: {0}\n".format(self.iterations))
                else:
                    self.solutions.append(solution)    
            if self.iterations % 10000 == 0:
                print('Number of iterations: {0}\n'.format(self.iterations))
        self.printSolutions()
        print("Number of iterations: {0}\n".format(self.iterations))


                    
soduko = Soduko()
board = Board()


board.putNumber(0,3,7,True)
board.putNumber(1,0,1,True)
board.putNumber(2,3,4,True)
board.putNumber(2,4,3,True)
board.putNumber(2,6,2,True)
board.putNumber(3,8,6,True)
board.putNumber(4,3,5,True)
board.putNumber(4,5,9,True)
board.putNumber(5,6,4,True)
board.putNumber(5,7,1,True)
board.putNumber(5,8,8,True)
board.putNumber(6,4,8,True)
board.putNumber(6,5,1,True)
board.putNumber(7,2,2,True)
board.putNumber(7,7,5,True)
board.putNumber(8,1,4,True)
board.putNumber(8,6,3,True)

soduko.addSolution(board)
soduko.solve()
