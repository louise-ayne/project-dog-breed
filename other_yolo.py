#from utils import DataGenerator
from utils import read_annotation_lines

train_lines, val_lines = read_annotation_lines('./AnnotationYOLO', test_size=0.1)

""" 
FOLDER_PATH = './Images'
class_name_path = './classes.txt'

data_gen_train = DataGenerator(train_lines, class_name_path, FOLDER_PATH)
data_gen_val = DataGenerator(val_lines, class_name_path, FOLDER_PATH) """