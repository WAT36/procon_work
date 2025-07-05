class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i=0
        ind=0
        zigzag=[]
        zigzag_i=[''] * numRows
        down=True
        up=False
        while i<len(s):
            if down:
                zigzag_i[ind] = s[i]
                ind+=1
                i+=1
            elif up:
                ind-=1
                if ind != 0:
                    zigzag_i = [''] * numRows
                    zigzag_i[ind] = s[i]
                    zigzag.append(zigzag_i)
                    zigzag_i=[''] * numRows
                    i+=1
            if down and ind==numRows:
                zigzag.append(zigzag_i)
                zigzag_i = [''] * numRows
                ind-=1
                down=False
                up=True
            if up and ind == 0:
                down=True
                up=False
        zigzag.append(zigzag_i)
        #print(zigzag)
        ans=''
        for i in range(numRows):
            for j in range(len(zigzag)):
                if zigzag[j][i] != '':
                    ans += zigzag[j][i]
        return ans

        # 模範
        # # numRows が 1 の場合は変換不要
        # if numRows == 1 or numRows >= len(s):
        #     return s

        # # 各行のバッファを用意
        # rows = ['' for _ in range(numRows)]
        # curr_row = 0
        # going_down = False

        # # 各文字を対応する行に振り分け
        # for ch in s:
        #     rows[curr_row] += ch
        #     # 端に到達したら折り返す
        #     if curr_row == 0 or curr_row == numRows - 1:
        #         going_down = not going_down
        #     curr_row += 1 if going_down else -1

        # # 行をつなげて返す
        # return ''.join(rows)