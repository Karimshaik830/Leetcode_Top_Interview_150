class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row ,col=len(matrix),len(matrix[0])
        x,y,dx,dy=0,0,1,0
        res=[]
        for _ in range(row*col):
            res.append(matrix[y][x])
            matrix[y][x]="."
            if not 0<=x+dx<col or not 0<=y+dy<row or matrix[y+dy][x+dx]==".":
                dx,dy=-dy,dx
            x+=dx
            y+=dy
        return res