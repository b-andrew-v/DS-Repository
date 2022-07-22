import numpy as np

def random_predict(number:int=1) -> int:
    """Multiline comment
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return(count)

print(f'Tryouts: {random_predict()}')