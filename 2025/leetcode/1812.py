class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        tate="12345678"
        yoko="abcdefgh"
        return (yoko.index(coordinates[0])%2==0 and tate.index(coordinates[1])%2==1) or (yoko.index(coordinates[0])%2==1 and tate.index(coordinates[1])%2==0)