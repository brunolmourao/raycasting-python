import numpy as np

class Camera:
	def __init__(self, pos, fov, faspect,  zNear, zFar):
        self.__pos = pos
        self.__forward = np.array([0.0, 0.0, 1.0])
        self.__up = np.array([0.0, 1.0, 0.0])
        self.__projection = perspective(fov, aspect, zNear, zFar)

    def getViewProjection(self): 
        return projection * lookAt(self.__pos, self.__pos + self.__forward, self.__up)

    def perspective():
    	return None

    def lookAt():
    	return None	  

   def cross(up, forward):
   		return None

   def normalize(vector):
   		return None

   def rotate(angle, target):
   		return None		

    def move_forward(amt):
    	self.__pos += self.__forward * amt
  

    def move_right(amt):
    	self.__pos += cross(self.__up, self.__forward) * amt
   

    def pitch(angle): 
   		right = normalize(cross(self.__up, self.__forward))
		self.__forward = normalize(rotate(angle, right) *  np.array([self.__forward, 0, 0]))
    	self.__up = normalize(cross(self.__forward, self.__right))
   

    def rotate_Y(angle)
    	UP = np.array([0.0, 1.0, 0.0])
        rotation = rotate(angle, UP)
    	forward = glm::normalize(rotation * glm::vec4(forward, 0.0))
   	    up = glm::normalize(rotation * glm::vec4(up, 0.0))
    