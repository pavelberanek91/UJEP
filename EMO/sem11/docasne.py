import random
import matplotlib.pyplot as plt
from typing import List, Tuple

class Particle:
    '''
    Class that represents particle from PSO technique.
    '''

    def __init__(self, r: Tuple, v: Tuple):
        self._r = r
        self._v = v

    @property
    def r(self) -> Tuple:
        return self._r
    
    @r.setter
    def r(self, value: Tuple) -> None:
        self._r = value

    @property
    def v(self) -> Tuple:
        return self._v
    
    @v.setter
    def v(self, value: Tuple) -> None:
        self._v = value


class Swarm:

    def __init__(self, n_particles: int, r_boundaries: List[Tuple[float]], v_boundaries: List[Tuple[float]]):
        self._r_boundaries = r_boundaries
        self._v_boundaries = v_boundaries
        self._n_particles = n_particles
        self._n_dims = min([len(r_boundaries), len(v_boundaries)])
        self._particles = self.generate_random_particles()

    def generate_random_particles(self) -> List[Particle]:
        '''
        Generates speficied number of particle objects with random coordinates. Currently coordinates generating and velocity generating has same algorithm.
        '''
        particles = []
        for iparticle in self._n_particles:
            random_r = self._generate_random_coordinates()
            random_v = self._generate_random_coordinates()
            particles.append(Particle(r=random_r, v=random_v))
        return particles

    def _generate_random_coordinates(self) -> Tuple:
        '''
        Generates random coordinates for specified number of dimensions between boundaries for each dimension.
        '''
        coordinates = []
        for idim in range(self._n_dims):
            coordinates.append(random.uniform(self._r_boundaries[idim][0], self._r_boundaries[idim][1]))
        return tuple(coordinates)
    
    def plot_swarm(self) -> None:
        x_coordinates = [particle.x for particle in self._particles]
        y_coordinates = [particle.y for particle in self._particles]
        plt.scatter(x=x_coordinates, y=y_coordinates)
    
    @property
    def r_boundaries(self) -> List[Tuple]:
        return self._r_boundaries
    
    @r_boundaries.setter
    def r_boundaries(self, value) -> None:
        self._r_boundaries = value
        self._n_dims = min([len(value), len(self._v_boundaries)])
        self._particles = self.generate_random_particles()

    @property
    def v_boundaries(self) -> List[Tuple]:
        return self._v_boundaries
    
    @v_boundaries.setter
    def v_boundaries(self, value) -> None:
        self._v_boundaries = value
        self._n_dims = min([len(value), len(self._r_boundaries)])
        self._particles = self.generate_random_particles()
    
    @property
    def n_particles(self) -> int:
        return self._n_particles
    
    @n_particles.setter
    def n_particles(self, value) -> None:
        self._n_particles = value
        self._particles = self.generate_random_particles()
    
    @property
    def n_dims(self) -> int:
        return self._n_dims
    
    @property
    def particles(self) -> List[Particle]:
        return self._particles
    
    @particles.setter
    def particles(self, value) -> None:
        try:
            for particle in value:
                for idim in range(self._n_dims): 
                    assert self._r_boundaries[idim][0] <= particle.r[idim] <= self._r_boundaries[idim][1]
                    assert self._v_boundaries[idim][0] <= particle.v[idim] <= self._v_boundaries[idim][1]
        except:
            print("Particles boundaries arent correct! Setting new particles denied.")
        self._particles = value
        self._n_particles = len(value)

if __name__ == '__main__':
    swarm = Swarm(n_particles=10, r_boundaries=[(0,10), (0,5)], v_boundaries=[(0,10), (0,5)])