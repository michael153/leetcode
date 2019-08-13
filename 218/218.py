from Queue import PriorityQueue

class Solution(object):
    """Should be faster, but should bisect"""
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        q = PriorityQueue()
        for i, building in enumerate(buildings):
            q.put((building[0], 0, -building[2], i))
            q.put((building[1], 1, building[2], i))
        cur_height = 0
        pts = []
        running = []
        while not q.empty():
            skyline = q.get()
            i = skyline[3]
            if skyline[1] == 1:
                running = sorted(running)
                peek = running[0]
                if peek == (-buildings[i][2], buildings[i][0]):
                    running.remove(peek)
                    if running:
                        new_skyline = running[0]
                        if -new_skyline[0] != cur_height:
                            pts.append((buildings[i][1], -new_skyline[0]))
                            cur_height = -new_skyline[0]
                    else:
                        if 0 != cur_height:
                            pts.append((buildings[i][1], 0))
                            cur_height = 0
                else:
                    running.remove((-buildings[i][2], buildings[i][0]))
            else:
                if buildings[i][2] > cur_height:
                    pts.append((buildings[i][0], buildings[i][2]))
                    cur_height = buildings[i][2]
                running.append((-buildings[i][2], buildings[i][0]))
        return pts
