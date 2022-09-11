
import config
import random, os

DIR_PATH = config.DIR_PATH

NUM_LAYERS_LIST = []

FILE_PATH_layerOne = ''
FILE_PATH_layerTwo = ''


def generate_period():
    layer_one = random.randint(1, 3)
    layer_two = random.randint(1, 3)
    if layer_one != layer_two:
          NUM_LAYERS_LIST.append(layer_one)
          NUM_LAYERS_LIST.append(layer_two)
    else:
      generate_period()
    return NUM_LAYERS_LIST


def create_name_layer():
  name_layers_list = []
  generate_period()
  FILE_PATH_layerOne = os.path.join(DIR_PATH, f'{NUM_LAYERS_LIST[0]}' + '.png')
  FILE_PATH_layerTwo = os.path.join(DIR_PATH, f'{NUM_LAYERS_LIST[1]}' + '.png')
  name_layers_list.insert(0, FILE_PATH_layerOne)
  name_layers_list.insert(1, FILE_PATH_layerTwo)
  print(name_layers_list)


if __name__ == '__main__':
    create_name_layer()