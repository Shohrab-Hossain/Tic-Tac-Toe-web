from browser import document, html

game_type_str = ['Play with friend', 'Play against Computer']

# this will toggle game type
def toggle_game_type(event):
    str = document['gameType'].text

    if str == game_type_str[0]:
        document['gameType'].text = game_type_str[1]
    else:
        document['gameType'].text = game_type_str[0]
    
    player_name()

# this print player name
def player_name():
    str = document['gameType'].text

    if str == game_type_str[0]:
        document['player01Name'].text = 'Computer'
        document['player02Name'].text = 'Player'
    else:
        document['player01Name'].text = 'Player 01'
        document['player02Name'].text = 'Player 02'

def game_type_selection():
    str = document['gameType'].text

    if str == game_type_str[0]:
        return 'PvC'
    else:
        return 'PvP'


def character_selection(game_type):
    if(game_type == 'PvP'):     # taking character for Player-vs-Player game 
        player1_char = document['player01Char'].text.upper()
        player2_char = document['player02Char'].text.upper()
        return [player1_char, player2_char, 'Player 1', 'Player 2']
    elif(game_type == 'PvC'):   # taking character for Player-vs-Computer game
        computer_char = document['player01Char'].text.upper()
        player_char = document['player02Char'].text.upper()
        return [computer_char, player_char, 'Computer', 'Player']
    else:
        return ['error']

def reset_board():
    for i in range(1,10):
        document.select('#board' + str(i) + ' p')[0].text = ''
        document['board' + str(i)].classList.remove('bg-clr')
        

def print_board(game_data):
    placeholder1 = '       |       |       '
    placeholder2 = '-----------------------'
    
    print('\n\n\n\t\t{}'.format(placeholder1))
    print('\t\t   {}   |   {}   |   {}   '.format( game_data['b7'], game_data['b8'], game_data['b9'] ))
    print('\t\t{}\n\t\t{}\n\t\t{}'.format( placeholder1, placeholder2, placeholder1 ))
    print('\t\t   {}   |   {}   |   {}   '.format( game_data['b4'], game_data['b5'], game_data['b6'] ))
    print('\t\t{}\n\t\t{}\n\t\t{}'.format( placeholder1, placeholder2, placeholder1 ))
    print('\t\t   {}   |   {}   |   {}  '.format( game_data['b1'], game_data['b2'], game_data['b3'] ))
    print('\t\t{}\n\n\n'.format( placeholder1 ))


def get_winner(game_data, player1_char, player2_char):
    # checking Rows
    if game_data['b1'] == game_data['b2'] == game_data['b3'] and game_data['b1'] != ' ':
        winner=game_data['b1']
        winner_board=['1', '2', '3']
    elif game_data['b4'] == game_data['b5'] == game_data['b6'] and game_data['b4'] != ' ':
        winner=game_data['b4']
        winner_board=[4, '5', '6']
    elif game_data['b7'] == game_data['b8'] == game_data['b9'] and game_data['b7'] != ' ':
        winner=game_data['b7']
        winner_board=['7', '8', '9']
    
    # checking Columns
    elif game_data['b1'] == game_data['b4'] == game_data['b7'] and game_data['b1'] != ' ':
        winner=game_data['b1']
        winner_board=['1', '4', '7']
    elif game_data['b2'] == game_data['b5'] == game_data['b8'] and game_data['b2'] != ' ':
        winner=game_data['b2']
        winner_board=['2', '5', '8']
    elif game_data['b3'] == game_data['b6'] == game_data['b9'] and game_data['b3'] != ' ':
        winner=game_data['b3']
        winner_board=['3', '6', '9']
    
    # checking Diagonals
    elif game_data['b1'] == game_data['b5'] == game_data['b9'] and game_data['b1'] != ' ':
        winner=game_data['b1']
        winner_board=['1', '5', '9']
    elif game_data['b3'] == game_data['b5'] == game_data['b7'] and game_data['b3'] != ' ':
        winner=game_data['b3']
        winner_board=['3', '5', '7']
    else:
        winner='none'

    # returning the winner name
    if winner == player1_char:
        return ['player 01', winner_board]
    elif winner == player2_char:
        return ['player 02', winner_board]
    else:
        return ['none']


def flash_message(message, trigger):
    document['game-message'].style.display = 'inline'
    document['game-message'].text = message

    if trigger.lower() == 'turn':
        document['game-message'].style.color = '#8c7979'
    else:
        document['game-message'].style.color = '#003e0a'

   