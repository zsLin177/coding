import pdb
class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        all_num = m*n
        i = j = 0
        right_b = n-1
        low_b = m-1
        res = []
        while len(res) < all_num:
            for k in range(j, right_b+1):
                res.append(matrix[i][k])
                if len(res) == all_num:
                    return res
            for k in range(i+1, low_b+1):
                res.append(matrix[k][right_b])
                if len(res) == all_num:
                    return res
            for k in range(right_b-1, j-1, -1):
                res.append(matrix[low_b][k])
                if len(res) == all_num:
                    return res
            for k in range(low_b-1, i, -1):
                res.append(matrix[k][j])
                if len(res) == all_num:
                    return res
            i += 1
            j += 1
            right_b -= 1
            low_b -= 1
        return res


if __name__ == "__main__":
    s = Solution(
    )
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))