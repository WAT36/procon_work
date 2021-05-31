#線分交差判定を行う関数
#線分(p1x,p1y)(p2x,p2y)と線分(p3x,p3y)(p4x,p4y)が交差しているかを判定する
def isLineSegmentInterSected(p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y):
    if(((p1x - p2x) * (p3y - p1y) + (p1y - p2y) * (p1x - p3x)) *
       ((p1x - p2x) * (p4y - p1y) + (p1y - p2y) * (p1x - p4x)) < 0):
        if(((p3x - p4x) * (p1y - p3y) + (p3y - p4y) * (p3x - p1x)) *
           ((p3x - p4x) * (p2y - p3y) + (p3y - p4y) * (p3x - p2x)) < 0):
            return True
    return False