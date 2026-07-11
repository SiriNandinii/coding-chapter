class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obstacles = set(map(tuple, obstacles))
        dir = 0
        x = 0
        y = 0
        max_dist = 0   # 🔥 track max distance
        
        for com in commands:
            if com == -1:
                dir = (dir + 1) % 4
            elif com == -2:
                dir = (dir + 3) % 4
            else:
                for _ in range(com):
                    temp_x = x
                    temp_y = y
                    
                    if dir == 0:
                        temp_y += 1
                    elif dir == 1:
                        temp_x += 1
                    elif dir == 2:
                        temp_y -= 1
                    else:
                        temp_x -= 1

                    if (temp_x, temp_y) not in obstacles:
                        x = temp_x
                        y = temp_y
                        max_dist = max(max_dist, x*x + y*y)  # 🔥 update here
                    else:
                        break
        
        return max_dist