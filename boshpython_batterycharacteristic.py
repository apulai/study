import numpy


class BatteryCharacteritics:
    def __init__(self, voltageData, capacityData, deg):
        # Convert used up capacity value to remainĺng capacity percentage
        remainingCapacityPercentage = [(capacityData[-1] - i) / capacityData[-1] for i in capacityData]

        """
        numpy.polyfit:
        Fit a polynomíal p(x) = p[0] x ** deg + + p[deg) of degree deg to pointg(x, y).
        Returns a vector of coeffícíenť p that minimíses the squared error in the
        order deg, deg O. \
        """
        p = numpy.polyfit(voltageData, remainingCapacityPercentage, deg)

        """
        numpy.dot:
        dot(nD - array, nD—array) produces
        a scalar by makíng the dot product of the vectors.
        """

        def fit(v):
            x = numpy.array([v ** i for i in range(deg, -1, -1)])
            return numpy.dot(p, x)

        self.polyfit = lambda x: numpy.dot(p, numpy.array([x ** i for i in range(deg, -1, -1)]))

    def getCapacityPercentage(self, voltage):
        return self.polyfit(voltage)


if __name__ == '__main__':
    # Measurenent of FULL battery díscharge

    data = {'voltage': [4.0, 3.75, 3.5, 3.41, 3.4, 3.37, 3.2, 3.0],  # [V]
            'capacity': [0.0, 0.1, 1.0, 2.5, 3.1, 5.0, 6.0, 6.5]  # [Ah] used zp capacity (at the last measured point
            # the full capacity is used up
            }

    bc = BatteryCharacteritics(data['voltage'], data['capacity'], 4)

    # Get remaining capacity knowing the Voltage

    voltage = 3.4  # [V]
    capacity = bc.getCapacityPercentage(voltage)
    print(' Hurray!' if capacity == 0.516740722963732 else 'Nay')
