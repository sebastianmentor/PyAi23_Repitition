def not_good_func(value ,standard_value:list = []):
    standard_value.append(value)
    print(standard_value)


# not_good_func(42)
# not_good_func('Hello world')
# not_good_func(42, [])
# not_good_func('opps')


def main(list_of_data:list) -> None:
    
    while True:
        value = input('Skriv in ett värde eller q för att avsluta: ')

        if value == 'q': break

        list_of_data.append(value)

def start_up() -> callable:
    our_list = []
    
    def main() -> None:
        
        while True:
            value = input('Skriv in ett värde eller q för att avsluta: ')

            if value == 'q': break

            our_list.append(value)

        print(our_list)
    
    return main

# def start_up() -> list:
#     our_list = []
#     main(our_list)
#     return our_list


if __name__ == '__main__':
    func = start_up()
    func()

