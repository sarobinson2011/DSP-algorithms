import math

""" takes an angle in radians and the number of iterations to perform as input, 
   and returns the sine and cosine of the angle as output """

def cordic_sine_cosine(angle, iterations):
    # Initialize variables
    x = 1.0
    y = 0.0
    z = angle
    for i in range(iterations):
        # Calculate next iteration
        d = 1.0 if z > 0 else -1.0
        x_new = x - d * y / (2**i)
        y_new = y + d * x / (2**i)
        z_new = z - d * math.atan(1 / (2**i))
        # Update variables
        x = x_new
        y = y_new
        z = z_new
    # Calculate sine and cosine
    sine = y
    cosine = x
    return sine, cosine

""" The number of iterations determines the accuracy of the result; 
   more iterations will result in a more accurate answer, but will also take longer to compute. """

angle = math.pi / 4  # 45 degrees in radians
iterations = 10
sine, cosine = cordic_sine_cosine(angle, iterations)
print(f'sine({angle}): {sine}, cosine({angle}): {cosine}')
