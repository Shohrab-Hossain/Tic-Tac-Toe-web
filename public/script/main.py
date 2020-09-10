from lib import *
from computerBrain import *
from browser import document, html, alert, timer   # Brython

# this will hide the flash message
document['game-message'].style.display = 'none' 

# this will print initial player name
player_name()

# taking data from dom
def start_play(event):
    document['gameType'].style.display = 'none'
    document['start-button'].style.display = 'none'
    document['game-message'].style.display = 'none'
    reset_board() 

    # this dictionary holds the data of each movement
    game_data = {'b1':' ', 'b2':' ', 'b3':' ', 'b4':' ', 'b5':' ', 'b6':' ', 'b7':' ', 'b8':' ', 'b9':' '}

    # selecting game type
    game_type = game_type_selection()

    # taking Character for Players
    player_char = character_selection(game_type)

    # this varoiable holds the 9steps for the game
    count = 1

    def make_move(selected_button):
        nonlocal count

        if count%2 == 0 :
            character = player_char[1]
            flash_message(player_char[2] + "'s turn", 'turn')
        else:
            character = player_char[0]
            flash_message(player_char[3] + "'s turn", 'turn')

        if selected_button.isnumeric() and int(selected_button) in range(1,10):
            if game_data['b'+selected_button] == ' ':
                game_data['b'+selected_button] = character
                
                # Printing to Board. This selects '#board1 p' and then add character
                document.select('#board' + str(selected_button)+' p')[0].text = character
        
                # checking for winner
                if count > 4:
                    winner_data = get_winner(game_data, player_char[0], player_char[1])
                    
                    winner = winner_data[0]
                
                    if not winner == 'none':
                        winner_board = winner_data[1]
                        for boardNumber in winner_board:
                            document['board' + str(boardNumber)].classList.add('bg-clr')

                        if(game_type == 'PvP'):
                            winner_str = 'Congratulations! ' + winner + ' is winner.'
                            flash_message('Congratulations! ' + winner + ' is winner.', 'end')
                        else:
                            if winner == 'player 01':   # Computer wins                
                                flash_message('Sorry! You lose.', 'end')
                            else:   # Player wins
                                flash_message('Congratulations! You win.', 'end')

                        document['start-button'].style.display = 'inline'
                        document['start-button'].style.marginLeft = '15px'
                        document['start-button'].text = 'Play again' 
                        document['gameType'].style.display = 'inline'
 
                        unbind_click()

                # game reached in last step, meaning no one wins 
                if count == 9 and  winner == 'none':
                    flash_message('AHH! No one wins. It is a draw.', 'end')

                    document['start-button'].style.display = 'inline'
                    document['start-button'].style.marginLeft = '15px'
                    document['start-button'].text = 'Play again'
                    document['gameType'].style.display = 'inline'

                    unbind_click()   # this will remove click-bind before game ends
                
                count += 1

                # this will remove the click-event for the board-cell, because the cell is used
                document['board' + selected_button].unbind('click', event_handler)
                document['board' + selected_button].style.cursor = 'default'

                # this will initiate computer move, in PvC, after 1.5sec
                def gopi():
                    bind_click()
                    make_move(selected_button)

                if game_type == 'PvC' and count%2 != 0:
                    unbind_click()
                    selected_button = computer_brain(game_data, player_char[0], player_char[1])
                    timer.set_timeout(gopi, 1500)


    def event_handler(event):
        selected_button = event.currentTarget.id[5:6]
        make_move(selected_button)

    def bind_click():
        for i in range(1,10):
            if game_data['b'+str(i)] == ' ':
                document['board' + str(i)].bind('click', event_handler)

    def unbind_click():
        for i in range(1,10):
            document['board' + str(i)].unbind('click', event_handler)

    bind_click()

    if count%2 == 0 :
        flash_message(player_char[3] + "'s turn", 'turn')
    else:
        flash_message(player_char[2] + "'s turn", 'turn')

    if game_type == 'PvC' and count%2 != 0:
        selected_button = computer_brain(game_data, player_char[0], player_char[1])
        make_move(selected_button)


document['gameType'].bind('click', toggle_game_type)
document['start-button'].bind('click', start_play)
    
    