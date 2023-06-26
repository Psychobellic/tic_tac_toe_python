# Define variaveis
play_count = 0
first_player = True
first_player_moves = []
second_player_moves = []

r1 = [' ', ' ', ' ']
r2 = [' ', ' ', ' ']
r3 = [' ', ' ', ' ']

# Define funções
def display_game(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

def user_choice():
    user_input = input("Please select a cell from 1 to 9: ")
    # Se o Input não for aceitável, perguntar novamente, verifica tanto se é não digito, como se caso seja um digito fora do esperado 1 - 9
    if not user_input.isdigit():
        user_choice()
    else:
        if int(user_input) < 1 or int(user_input) > 9:
            user_choice()
    # Quando houver um input esperado, retorná-lo
    if int(user_input) >= 1 and int(user_input) <= 9:
        return int(user_input)
        
# Lógica do game
while play_count < 9:
    # Verifica de quem é o turno
    if (play_count % 2) == 0:
        first_player = True
    else:
        first_player = False
    
    user_input_int = user_choice()
    if user_input_int is None:
        user_input_int = user_choice()
    else:
        if first_player:
            mark = "X"
            first_player_moves.append(user_input_int)
        if not first_player:
            mark = "O"
            second_player_moves.append(user_input_int)
        if user_input_int / 3 <= 1:
            index = user_input_int - 1
            r1[index] = mark
        if user_input_int / 3 > 1 and user_input_int / 3 <= 2:
            index = user_input_int - 4
            r2[index] = mark
        if user_input_int / 3 > 2:
            index = user_input_int - 7
            r3[index] = mark
        
        display_game(r1, r2, r3)
        play_count += 1
        
        
print("Game Over! No turns left.")
display_game(r1, r2, r3)