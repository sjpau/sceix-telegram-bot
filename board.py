import chess
import pygame
import os

def generate_board_image_with_pygame(board: chess.Board, move: str, path: str):

   
    # Define chessboard size and cell size
    BORDER_WIDTH = 30
    SCREEN_WIDTH, SCREEN_HEIGHT = 52*8 + BORDER_WIDTH, 52*8 + BORDER_WIDTH
    BOARD_WIDTH, BOARD_HEIGHT = 52*8, 52*8
    CELL_SIZE = (BOARD_WIDTH) // 8

    # Define colors
    WHITE = (254, 206, 157)
    BLACK = (233, 145, 159)
    BORDER = (200, 145, 159)

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    board_rect = pygame.FRect(0, 0, BOARD_WIDTH, BOARD_HEIGHT)
    board_rect.center = screen.get_rect().center
    board_surf = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
    pygame.display.set_caption("Chessboard")

    assets = {
        'p': pygame.image.load('asset/pawnB.png').convert_alpha(),
        'P': pygame.image.load('asset/pawnW.png').convert_alpha(),
        'b': pygame.image.load('asset/bishopB.png').convert_alpha(),
        'B': pygame.image.load('asset/bishopW.png').convert_alpha(),
        'r': pygame.image.load('asset/rookB.png').convert_alpha(),
        'R': pygame.image.load('asset/rookW.png').convert_alpha(),
        'n': pygame.image.load('asset/knightB.png').convert_alpha(),
        'N': pygame.image.load('asset/knightW.png').convert_alpha(),
        'k': pygame.image.load('asset/kingB.png').convert_alpha(),
        'K': pygame.image.load('asset/kingW.png').convert_alpha(),
        'q': pygame.image.load('asset/queenB.png').convert_alpha(),
        'Q': pygame.image.load('asset/queenW.png').convert_alpha(),
    }

    # Chessboard data
    if move != '':
        board.push(chess.Move.from_uci(move))
    board_slice = board.__str__()
    board = [[piece for piece in row.split()] for row in board_slice.split('\n')]

    # Draw the chessboard and pieces
    for row in range(8):
        for col in range(8):
            x, y = col * CELL_SIZE, row * CELL_SIZE
            
            # Determine the cell color
            cell_color = WHITE if (row + col) % 2 == 0 else BLACK
            
            # Draw the cell with borders
            pygame.draw.rect(board_surf, cell_color, (x, y, CELL_SIZE, CELL_SIZE))
            
            piece = board[row][col]
            if piece != ".":
                img = assets[piece]
                img_rect = img.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                board_surf.blit(img, img_rect)

    # Draw the border around the entire chessboard
    pygame.draw.rect(screen, BORDER, (0,0,SCREEN_WIDTH,SCREEN_HEIGHT), BORDER_WIDTH)

    # Draw labels for rows (numbers)
    for row in range(8):
        font = pygame.font.Font(None, 24)
        text_surface = font.render(str(8 - row), True, (0, 0, 0))
        text_rect = text_surface.get_rect(x=(0), centery=(row * CELL_SIZE + CELL_SIZE // 2) + BORDER_WIDTH//2)
        screen.blit(text_surface, text_rect)
        text_rect = text_surface.get_rect(x=(SCREEN_WIDTH - BORDER_WIDTH / 2), centery=(row * CELL_SIZE + CELL_SIZE // 2) + BORDER_WIDTH//2)
        screen.blit(text_surface, text_rect)

    # Draw labels for columns (letters)
    for col in range(8):
        font = pygame.font.Font(None, 24)
        text_surface = font.render(chr(ord('a') + col), True, (0, 0, 0))
        text_rect = text_surface.get_rect(centerx=(col * CELL_SIZE + CELL_SIZE / 2) + BORDER_WIDTH//2, y=(SCREEN_HEIGHT - BORDER_WIDTH/ 2))
        screen.blit(text_surface, text_rect)
        text_rect = text_surface.get_rect(centerx=(col * CELL_SIZE + CELL_SIZE / 2) + BORDER_WIDTH//2, y=(0))
        screen.blit(text_surface, text_rect)

    screen.blit(board_surf, board_rect)
    pygame.display.flip()
    pygame.image.save(screen, os.path.abspath(path))

    pygame.quit()
