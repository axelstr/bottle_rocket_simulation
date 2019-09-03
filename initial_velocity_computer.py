import numpy as np

class InitialVelocityComputer():
    @staticmethod
    def compute(p_over, 
            V_bottle, V_water, 
            m_bottle, m_water,
            gamma):
            
        # Non-adiabatic    
        # work = p_over*(V_bottle-V_water)*np.log(V_bottle/(V_bottle-V_water))
        
        # Aidabatic
        work = p_over*(V_bottle-V_water)**gamma*((V_bottle-V_water)**(1-gamma) - V_bottle**(1-gamma))

        u = np.sqrt(2*work/(m_bottle+m_bottle**2/m_water))

        u_water_0 = m_bottle/m_water * u

        # print("u_0 water = %s" %(u_water_0))

        # u = np.sqrt(
        #     (p_over*V_water**2/(V_bottle-V_water))
        #     /(m_bottle+m_bottle**2/m_water)
        #     )

        return u