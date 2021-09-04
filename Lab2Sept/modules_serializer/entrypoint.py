from modules_serializer.arg import *
from modules_serializer.fabric import *
from modules_serializer.file1 import *


def make_files(obj):
    TOMLSerializer = TOML_S()
    TOMLSerializer.dump(obj, "/home/dimasbort/PycharmProjects/Lab2Sept/docs/input.toml")

    PICKLESerializer = PICKLE_S()
    PICKLESerializer.dump(obj, "/home/dimasbort/PycharmProjects/Lab2Sept/docs/input.pickle")

    JSONSerializer = JSON_S()
    JSONSerializer.dump(obj, "/home/dimasbort/PycharmProjects/Lab2Sept/docs/input.json")

    YAMLSerializer = YAML_S()
    YAMLSerializer.dump(obj, "/home/dimasbort/PycharmProjects/Lab2Sept/docs/input.yaml")

    return 0


def main():
    make_files(Dima())
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    if len(sys.argv) < 9 and not sys.argv.__contains__("-c"):
        raise Exception("Not enough arguments")
    elif args.config and len(sys.argv) != 3:
        raise Exception('Incorrect input')

    if args.config:
        config = read_config(str(args.config))
        check_formats(config['ifr'], config['ofr'], config['ifl'], config['ofl'])
        if config['ifr'] == config['ofr']:
            return
        serializer, deserializer = create_serializers(config['ifr'], config['ofr'])
        obj = deserializer.load(config['ifl'])
        serializer.dump(obj, config['ofl'])

    else:
        check_formats(args.ifr, args.ofr, args.ifl, args.ofl)
        if args.ifr == args.ofr:
            return
        serializer, deserializer = create_serializers(args.ifr, args.ofr)
        obj = deserializer.load(args.ifl)
        serializer.dump(obj, args.ofl)


if __name__ == '__main__':
    main()





