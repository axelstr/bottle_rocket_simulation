import numpy as np

from initial_velocity_computer import InitialVelocityComputer
from flight_iterator import FlightIterator
from result_visualizer import ResultVisualizer


class BottleRocketSimulator():
    @staticmethod
    def simulate():
        # All problem parameters are to be specified here
        # Unit descriptions: SI-units (pa, kg, m^3, radians, m, s)
        p_over = 7*(10**5)
        p_atmospheric = 101300
        V_water = .56/1000
        m_water = V_water*998
        m_bottle = .186
        V_bottle = 1.5/1000
        alpha_0 = 46 * np.pi / 180
        g = 9.82
        efficiency = .7 # work effiency (not currently used)
        gamma = 1.4 # adiabatic

        C = .5
        rho = 1.26
        d = 9.1/100
        A = (d/2)**2*np.pi 
        k = 1/2 * C * rho * A

        u_bottle_0 = InitialVelocityComputer.compute(
            p_over, p_atmospheric, 
            V_bottle, V_water, 
            m_bottle, m_water,
            efficiency, gamma)

        flight_iterator = FlightIterator()
        flight_iterator.iterate(m_bottle, u_bottle_0, k, alpha_0, g)
        x_drag, y_drag, t_drag = flight_iterator.get_path_coordinates()
        flight_iterator.iterate(m_bottle, u_bottle_0, 0, alpha_0, g)
        x_no_drag, y_no_drag, t_no_drag = flight_iterator.get_path_coordinates()

        visualizer = ResultVisualizer(x_drag, y_drag, t_drag, x_no_drag, y_no_drag, t_no_drag, u_bottle_0)
        visualizer.save_plot()
        # visualizer.show_plot()