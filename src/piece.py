class Piece:

    def __init__(self, name, value, position, color):
        
        '''
        Initializes a piece on the board

        Inputs: 
        name of piece (string)
        value of piece (int)
        position of piece (tuple)
        
        '''
        self.name = name
        self.value = value
        self.position = position
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
