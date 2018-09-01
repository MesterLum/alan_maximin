from utils.constants import DATA
from utils.process import Process



if __name__ == '__main__':
    Proc = Process(DATA)
    print(Proc.get_results_maximin())
    print(Proc.get_results_maximax())
