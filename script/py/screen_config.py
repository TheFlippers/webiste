'''Read configuration string and write settings to config file'''
import sys
import json


def main():
    '''Take json config string and output'''
    try:
        config = json.loads(sys.argv[1])

    except json.JSONDecodeError:
        print('json decode error')
        return

    min_config = {k: v for (k, v) in config.items() if v}

    if len(min_config) == 1:
        print('7x7')
        for val in config.values():
            if val:
                print(val)

    elif len(min_config) == 2:
        shape = get_two(config)
        if shape:
            if len(shape[0]) == 1:
                print('7x14')
                for screen in shape[0]:
                    print(screen)
                for screen in shape[1]:
                    print(screen)

            else:
                print('14x7')
                print(f"{shape[0][0]} {shape[0][1]}")

        else:
            return

    elif len(min_config) == 4:
        print('14x14')
        print(f"{config['top_left']} {config['top_right']}")
        print(f"{config['bot_left']} {config['bot_right']}")

    else:
        return


def get_two(config):
    if config['top_left']:
        if config['top_right']:
            return [[config['top_left'], config['top_right']]]
        elif config['bot_left']:
            return [[config['top_left']], [config['bot_left']]]
        else:
            return []

    elif config['top_right']:
        if config['bot_right']:
            return [[config['top_right']], [config['bot_right']]]
        else:
            return []

    else:
        if config['bot_left'] and config['bot_right']:
            return [[config['bot_left'], config['bot_right']]]
        else:
            return []


if __name__ == '__main__':
    main()
