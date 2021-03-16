# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        self.value_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.value_dict = set([(0, 0)])
        robot.clean()
        
        self.dfs(0, 0, 0, robot)
    
    def dfs(self, row, col, start, robot):
        for i in range(4):
            count = (i + start) % 4
            a = row + self.value_list[count][0]
            b = col + self.value_list[count][1]
            
            if not (a, b) in self.value_dict and robot.move():
                robot.clean()
                self.value_dict.add((a, b))
                self.dfs(a, b, count, robot)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()                

            robot.turnRight()