import os

class Piece:
    """
    Represents a generic chess piece.

    Attributes:
        name (str): The name of the piece.
        color (str): The color of the piece, either 'white' or 'black'.
        value (float): The value of the piece, with a sign based on its color.
        texture (str): The file path to the piece's texture image.
        texture_rect (tuple): The rectangle area for the piece's texture.
        moves (list): A list to store possible moves for the piece.
        moved (bool): Indicates whether the piece has moved from its initial position.
    """

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        """
        Initializes a Piece object.

        Args:
            name (str): The name of the piece.
            color (str): The color of the piece.
            value (float): The value of the piece.
            texture (str, optional): The file path to the piece's texture image.
            texture_rect (tuple, optional): The rectangle area for the piece's texture.
        """
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80):
        """
        Sets the file path for the piece's texture image based on the given size.

        Args:
            size (int, optional): The size of the texture image in pixels. Default is 80.
        """
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )

class Pawn(Piece):
    """
    Represents a pawn chess piece.
    
    Attributes:
        dir (int): The direction of movement for the pawn based on its color.
    """

    def __init__(self, color):
        """
        Initializes a Pawn object.

        Args:
            color (str): The color of the pawn.
        """
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)

class Knight(Piece):
    """
    Represents a knight chess piece.
    """

    def __init__(self, color):
        """
        Initializes a Knight object.

        Args:
            color (str): The color of the knight.
        """
        super().__init__('knight', color, 3.0)

class Bishop(Piece):
    """
    Represents a bishop chess piece.
    """

    def __init__(self, color):
        """
        Initializes a Bishop object.

        Args:
            color (str): The color of the bishop.
        """
        super().__init__('bishop', color, 3.0)

class Rook(Piece):
    """
    Represents a rook chess piece.
    """

    def __init__(self, color):
        """
        Initializes a Rook object.

        Args:
            color (str): The color of the rook.
        """
        super().__init__('rook', color, 5.0)

class Queen(Piece):
    """
    Represents a queen chess piece.
    """

    def __init__(self, color):
        """
        Initializes a Queen object.

        Args:
            color (str): The color of the queen.
        """
        super().__init__('queen', color, 9.0)

class King(Piece):
    """
    Represents a king chess piece.
    """

    def __init__(self, color):
        """
        Initializes a King object.

        Args:
            color (str): The color of the king.
        """
        super().__init__('king', color, 10000.0)
