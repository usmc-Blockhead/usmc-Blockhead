import os

filename = 'budget.txt'
dataDir = 'data'

def get_file_path(filename):
    currenDirPath = os.getcwd()
    filepath = os.path.join(currenDirPath, dataDir, filename)
    return filepath

def readBudget(file_path):
    with open(file_path, 'r') as f:
        cBudget = f.read()
        return cBudget

# def saveBudget(totalBudget):
#     with open(path, 'w') as f:
#         f.write(str(totalBudget))
#     f.close()

path = get_file_path(filename)
currentBudget = float(readBudget(path))

if __name__ == '__main__':
    readBudget(path)