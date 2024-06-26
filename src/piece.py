class Piece:

    def __init__(self, name, value, color):
        
        '''
        Inputs: 
        name of piece (string)
        value of piece (int)
        
        '''
        self.name = name
        self.value = value
        self.color = color
        self.set_image()

    def set_image(self):
        path = "./Images/"
        match self.name:
            case "Pawn":
                pass
            case "Knight":
                pass
            case "Bishop":
                pass
            case "Rook":
                pass
            case "Queen":
                pass
            case "King":
                pass

        path += "Untitled.png"
        self.image = path

class Pawn(Piece):
    def __init__(self, color):
        self.name = "Pawn"
        self.color = color

class Knight(Piece):
    def __init__(self, color):
        self.name = "Knight"
        self.color = color

class Bishop(Piece):
    def __init__(self, color):
        self.name = "Bishop"
        self.color = color

class Rook(Piece):
    def __init__(self, color):
        self.name = "Rook"
        self.color = color

class Queen(Piece):
    def __init__(self, color):
        self.name = "Queen"
        self.color = color

class King(Piece):
    def __init__(self, color):
        self.name = "King"
        self.color = color
