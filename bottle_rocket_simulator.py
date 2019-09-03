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
        V_water = .5/1000
        m_water = V_water*998
        m_bottle = .186
        V_bottle = 1.5/1000
        alpha_0 = 46 * np.pi / 180
        g = 9.82
        gamma = 1.4 # adiabatic

        C = .3
        rho = 1.26
        d = 9.1/100
        A = (d/2)**2*np.pi 
        k = 1/2 * C * rho * A

        u_bottle_0 = InitialVelocityComputer.compute(
            p_over, 
            V_bottle, V_water, 
            m_bottle, m_water,
            gamma)

        flight_iterator = FlightIterator()
        flight_iterator.iterate(m_bottle, u_bottle_0, k, alpha_0, g)
        x_drag, y_drag, t_drag = flight_iterator.get_path_coordinates()
        flight_iterator.iterate(m_bottle, u_bottle_0, 0, alpha_0, g)
        x_no_drag, y_no_drag, t_no_drag = flight_iterator.get_path_coordinates()

        visualizer = ResultVisualizer(x_drag, y_drag, t_drag, x_no_drag, y_no_drag, t_no_drag, u_bottle_0)
        visualizer.save_plot()
        # visualizer.show_plot()
    
    @staticmethod
    def optimize():
        # To optimize
        V_water_range = np.linspace(.8/1000, 1/1000, 101)
        alpha_0_range = np.linspace(46*np.pi/180, 50*np.pi/180, 90)

        # Fixed
        p_over = 7*(10**5)
        m_bottle = .186
        V_bottle = 1.5/1000
        g = 9.82
        gamma = 1.4 # adiabatic

        C = .5
        rho = 1.26
        d = 9.1/100
        A = (d/2)**2*np.pi 
        k = 1/2 * C * rho * A

        # Optimized
        current_best_length = 0
        V_water_optimized = 0
        alpha_0_optimized = 0

        for V_water in V_water_range:
            for alpha_0 in alpha_0_range:
                m_water = V_water*998
                u_bottle_0 = InitialVelocityComputer.compute(
                    p_over, 
                    V_bottle, V_water, 
                    m_bottle, m_water,
                    gamma)
                flight_iterator = FlightIterator()
                flight_iterator.iterate(m_bottle, u_bottle_0, k, alpha_0, g)
                if flight_iterator.get_ground_distance() > current_best_length:
                    current_best_length = flight_iterator.get_ground_distance()
                    V_water_optimized = V_water
                    alpha_0_optimized = alpha_0
        
        # Plot optimized values
        print(V_water_optimized*1000)
        print(alpha_0_optimized*180/np.pi)
        print(current_best_length)
        m_water = V_water_optimized*998
        u_bottle_0 = InitialVelocityComputer.compute(
                    p_over, 
                    V_bottle, V_water_optimized, 
                    m_bottle, m_water,
                    gamma)
        flight_iterator = FlightIterator()
        flight_iterator.iterate(m_bottle, u_bottle_0, k, alpha_0_optimized, g)
        x_drag, y_drag, t_drag = flight_iterator.get_path_coordinates()
        flight_iterator.iterate(m_bottle, u_bottle_0, 0, alpha_0_optimized, g)
        x_no_drag, y_no_drag, t_no_drag = flight_iterator.get_path_coordinates()

        visualizer = ResultVisualizer(x_drag, y_drag, t_drag, x_no_drag, y_no_drag, t_no_drag, u_bottle_0)
        visualizer.save_plot()
        # visualizer.show_plot()    