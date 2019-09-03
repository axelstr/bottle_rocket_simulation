import numpy as np

# TODO: Store velocity and speed in array to plot them later 

class FlightIterator():
    def __init__(self):
        self.x_coordinates = np.array([])
        self.y_coordinates = np.array([])
        self.t_coordinates = np.array([])
        self.vx_coordinates = np.array([])
        self.vy_coordinates = np.array([])
        self.vx_coordinates = np.array([])
        self.vy_coordinates = np.array([])

    def get_path_coordinates(self):
        return self.x_coordinates, self.y_coordinates, self.t_coordinates

    def get_ground_distance(self):
        first_negative_y_index = np.argmax(self.y_coordinates < 0)
        flight_length = self.x_coordinates[first_negative_y_index]
        return flight_length

    """
    Iterates given the initial conditions until the rocket has reached the ground.
    The x-, y- and t-coordinates are stored in the class fields.
    """
    def iterate(self, m, u_0, k, alpha_0, g):
        self.k = k
        self.alpha_0 = alpha_0
        self.g = g

        x = 0
        y = .1
        t = 0
        vx = np.sin(alpha_0) * u_0
        vy = np.cos(alpha_0) * u_0
        dt = .01
        x_coordinates = [x]
        y_coordinates = [y]
        t_coordinates = [t]

        while y >= -1:
            x, y, vx, vy = self.__newton_step(x, y, vx, vy, dt)
            # x, y, vx, vy = self.__verlet_step(x, y, vx, vy, dt)            
            t = t + dt
            x_coordinates.append(x)
            y_coordinates.append(y)
            t_coordinates.append(t)

        self.x_coordinates = np.array(x_coordinates)
        self.y_coordinates = np.array(y_coordinates)
        self.t_coordinates = np.array(t_coordinates)


    def __newton_step(self, x, y, vx, vy, dt):
        v = np.linalg.norm([vx, vy])
        ax = -self.k*vx*v
        ay = -self.k*vy*v -     self.g
        vx = vx + ax*dt
        vy = vy + ay*dt
        x = x + dt*vx
        y = y + dt*vy
        return x, y, vx, vy