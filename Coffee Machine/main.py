
# MENU PROVIDED BY THE COURSE

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# PROGRAM START

safe_box = 0

# INPUT

print('Qual café você gostaria de beber?\nExpresso (R$1.50)\nCom Leite (R$2.50)\nCappuccino (R$3.00)')

option = input('Digite uma opção: ').lower()

while option != 'desligar':

    if option == 'desligar':
        break

    elif option == 'relatório':
        print(f'Há disponível R${safe_box:.0f} no caixa.')

        print(f'Há disponível {resources["water"]}ml de água, {resources["milk"]}ml de leite'
              f' e {resources["coffee"]}g de café.')

    # ESPRESSO

    elif option == 'expresso':
        check_resources = [
            resources["water"],
            resources["milk"],
            resources["coffee"]
        ]
        resources_espresso = [
            MENU["espresso"]["ingredients"]["water"],
            0,
            MENU["espresso"]["ingredients"]["coffee"]
        ]
        result = {
            data[0]: (data[1], data[2])
            for data in zip(resources.keys(), check_resources, resources_espresso)
        }

        if result["water"][0] - result["water"][1] >= 0 and \
                result["coffee"][0] - result["coffee"][1] >= 0:
            amount_25 = int(input('Quantas moedas de 25 centavos serão inseridas? '))
            amount_10 = int(input('Quantas moedas de 10 centavos serão inseridas? '))
            amount_5 = int(input('Quantas moedas de 5 centavos serão inseridas? '))
            amount_1 = int(input('Quantas moedas de 1 centavo serão inseridas? '))
            TOTAL = (amount_25 * 0.25) + (amount_10 * 0.10) + (amount_5 * 0.05) + (amount_1 * 0.01)

            if TOTAL > (MENU["espresso"]["cost"]):
                resources = {
                    "water": result["water"][0] - result["water"][1],
                    "milk": result["milk"][0] - result["milk"][1],
                    "coffee": result["coffee"][0] - result["coffee"][1],
                }
                safe_box += MENU["espresso"]["cost"]
                print(f'Aqui estão seus R${TOTAL - (MENU["espresso"]["cost"]):.2f} de troco.\n'
                      f'Aqui está o seu Café {option.title()}! Aproveite!')

            elif TOTAL == (MENU["espresso"]["cost"]):
                resources = {
                    "water": result["water"][0] - result["water"][1],
                    "milk": result["milk"][0] - result["milk"][1],
                    "coffee": result["coffee"][0] - result["coffee"][1],
                }
                safe_box += MENU["espresso"]["cost"]
                print(f'Aqui está o seu Café {option.title()}! Aproveite!')

            else:
                print('Desculpe, dinheiro insuficiente! Dinheiro devolvido.')

        else:

            if result["water"][0] - result["water"][1] < 0:
                print('Desculpe, não há água suficiente.')

            elif result["coffee"][0] - result["coffee"][1] < 0:
                print('Desculpe, não há café suficiente.')

    # LATTE

    elif option == 'com leite':
        check_resources = [
            resources["water"],
            resources["milk"],
            resources["coffee"]
        ]
        resources_latte = [
            MENU["latte"]["ingredients"]["water"],
            MENU["latte"]["ingredients"]["milk"],
            MENU["latte"]["ingredients"]["coffee"]
        ]
        result = {
            data[0]: (data[1], data[2])
            for data in zip(resources.keys(), check_resources, resources_latte)
        }

        if result["water"][0] - result["water"][1] >= 0 and \
                result["milk"][0] - result["milk"][1] >= 0 and \
                result["coffee"][0] - result["coffee"][1] >= 0:
            amount_25 = int(input('Quantas moedas de 25 centavos serão inseridas? '))
            amount_10 = int(input('Quantas moedas de 10 centavos serão inseridas? '))
            amount_5 = int(input('Quantas moedas de 5 centavos serão inseridas? '))
            amount_1 = int(input('Quantas moedas de 1 centavo serão inseridas? '))
            TOTAL = (amount_25 * 0.25) + (amount_10 * 0.10) + (amount_5 * 0.05) + (amount_1 * 0.01)

            if TOTAL > (MENU["latte"]["cost"]):
                resources = {
                    "water": result["water"][0] - result["water"][1],
                    "milk": result["milk"][0] - result["milk"][1],
                    "coffee": result["coffee"][0] - result["coffee"][1],
                }
                safe_box += MENU["latte"]["cost"]
                print(f'Aqui estão seus R${TOTAL - (MENU["latte"]["cost"]):.2f} de troco.\n'
                      f'Aqui está o seu Café {option.title()}! Aproveite!')

            elif TOTAL == (MENU["latte"]["cost"]):
                resources = {
                    "water": result["water"][0] - result["water"][1],
                    "milk": result["milk"][0] - result["milk"][1],
                    "coffee": result["coffee"][0] - result["coffee"][1],
                }
                safe_box += MENU["latte"]["cost"]
                print(f'Aqui está o seu Café {option.title()}! Aproveite!')

            else:
                print('Desculpe, dinheiro insuficiente! Dinheiro devolvido.')

        else:

            if result["water"][0] - result["water"][1] < 0:
                print('Desculpe, não há água suficiente.')

            elif result["latte"][0] - result["latte"][1] < 0:
                print('Desculpe, não há leite suficiente.')

            elif result["coffee"][0] - result["coffee"][1] < 0:
                print('Desculpe, não há café suficiente.')

    # CAPPUCCINO

    elif option == 'cappuccino':
        check_resources = [
            resources["water"],
            resources["milk"],
            resources["coffee"]
        ]
        resources_cappuccino = [
            MENU["cappuccino"]["ingredients"]["water"],
            MENU["cappuccino"]["ingredients"]["milk"],
            MENU["cappuccino"]["ingredients"]["coffee"]
        ]
        result = {
            data[0]: (data[1], data[2])
            for data in zip(resources.keys(), check_resources, resources_cappuccino)
        }

        if result["water"][0] - result["water"][1] >= 0 and \
                result["milk"][0] - result["milk"][1] >= 0 and \
                result["coffee"][0] - result["coffee"][1] >= 0:
            amount_25 = int(input('Quantas moedas de 25 centavos serão inseridas? '))
            amount_10 = int(input('Quantas moedas de 10 centavos serão inseridas? '))
            amount_5 = int(input('Quantas moedas de 5 centavos serão inseridas? '))
            amount_1 = int(input('Quantas moedas de 1 centavo serão inseridas? '))
            TOTAL = (amount_25 * 0.25) + (amount_10 * 0.10) + (amount_5 * 0.05) + (amount_1 * 0.01)

            if TOTAL > (MENU["cappuccino"]["cost"]):
                resources = {
                    "water": result["water"][0] - result["water"][1],
                    "milk": result["milk"][0] - result["milk"][1],
                    "coffee": result["coffee"][0] - result["coffee"][1],
                }
                safe_box += MENU["cappuccino"]["cost"]
                print(f'Aqui estão seus R${TOTAL - (MENU["cappuccino"]["cost"]):.2f} de troco.\n'
                      f'Aqui está o seu Café {option.title()}! Aproveite!')

            elif TOTAL == (MENU["cappuccino"]["cost"]):
                resources = {
                    "water": result["water"][0] - result["water"][1],
                    "milk": result["milk"][0] - result["milk"][1],
                    "coffee": result["coffee"][0] - result["coffee"][1],
                }
                safe_box += MENU["cappuccino"]["cost"]
                print(f'Aqui está o seu {option.title()}! Aproveite!')

            else:
                print('Desculpe, dinheiro insuficiente! Dinheiro devolvido.')

        else:

            if result["water"][0] - result["water"][1] < 0:
                print('Desculpe, não há água suficiente.')

            elif result["latte"][0] - result["latte"][1] < 0:
                print('Desculpe, não há leite suficiente.')

            elif result["coffee"][0] - result["coffee"][1] < 0:
                print('Desculpe, não há café suficiente.')

    # INVALID OPTION

    else:
        print('Esta é uma máquina de café! Por favor, digite uma opção válida!')

    # FEEDBACK

    print('\nQual café você gostaria de beber?\nExpresso ($1.50)\nCom Leite ($2.50)\nCappuccino ($3.00)')

    option = input('Digite uma opção: ').lower()

# BREAK

print('Obrigado pela preferência e volte sempre!')

# THE END!
