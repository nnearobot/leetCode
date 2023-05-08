# 2126. Destroying Asteroids
# Medium
# https://leetcode.com/problems/destroying-asteroids/

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid_mass in asteroids:
            if asteroid_mass > mass :
                return False
            mass += asteroid_mass
        
        return True