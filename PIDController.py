K_P = 0 
K_I = 0
K_D = 0

past_err: int = 0
sum_err: int = 0

def calc(err):
    global past_err, sum_err
    output = K_P * err + K_I * sum_err + K_D * (err - past_err)
    past_err = err
    sum_err += err
    return output