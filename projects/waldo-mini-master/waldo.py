Waldo = 'W'
Other = '.'

def all_row_exists_waldo(collection):
    """For all rows in the matrix, Waldo is in some column"""
    for row in collection:
        if Waldo not in row:
            return False
    return True

def all_col_exists_waldo(collection):
    """For all columns in the matrix, Waldo is in some row"""
    col_true = 0
    if len(collection) == 0:
        return True
    for col in range(len(collection[0])):
        for row in range(len(collection)):
            if Waldo == collection[row][col]:
                col_true += 1
                break
    if col_true == len(collection[0]):
        return True
    return False

def all_row_all_waldo(collection):
    """For all rows in the matrix, Waldo is in every column"""
    for row in collection:
        for col in row:
            if col != Waldo:
                return False
    return True

def all_col_all_waldo(collection):
    """For all the columns in the matrix, Waldo is in every row"""
    for col in range(len(collection[0])):
        for row in range(len(collection)):
            if collection[row][col] != Waldo:
                return False
    return True

def exists_row_all_waldo(collection):
    """There is some row in the matrix in which Waldo is in every column"""
    if (len(collection) > 0) and len(collection[0]) == 0:
        return True
    for row in range(len(collection)):
        row_true = 0
        for col in range(len(collection[row])):
            if collection[row][col] == Waldo:
                row_true += 1
            if row_true == len(collection[0]):
                return True
    return False

def exists_col_all_waldo(collection):
    """There is some column in the matrix in which Waldo is in every row"""
    if len(collection) == 0:
        return False
    for col in range(len(collection[0])):
        col_true = 0
        for row in range(len(collection)):
            if collection[row][col] == Waldo:
                col_true += 1
            if col_true == len(collection):
                return True
    return False

def exists_row_exists_waldo(collection):
    """There is some row in the matrix in which Waldo is in some column"""
    for row in collection:
        for col in row:
            if col == Waldo:
                return True
    return False

    
def exists_col_exists_waldo(collection):
    """There is some column in the matrix in which Waldo is in some row"""
    if len(collection) == 0:
        return False
    for col in range(len(collection[0])):
        for row in range(len(collection)):
            if collection[row][col] == Waldo:
                return True
    return False