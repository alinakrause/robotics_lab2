# import the rigid body motion module
import rbm
import math
import numpy as np

if __name__ == '__main__':
	# define a test value 
	theta = math.pi/2 
	phi = math.pi/2 
	psi = math.pi/2
	# update the output format
	np.set_printoptions(precision = 2, suppress = True)
	# define a 3D vector
	v0 = rbm.vec(0,1,1) # values from the example in class
	# define a 3D rotation about x axes
	Rx = rbm.rot_x(psi)
	# define a 3D rotation about y axes
	Ry = rbm.rot_y(phi)
	# define a 3D rotation about z axes
	Rz = rbm.rot_z(theta)

	# calculate a total rotation via FIXED FRAME
	R = np.matmul(np.matmul(Rz, Ry), Rz)
	# calculate the results of rotation
	v01 = R.dot(v0)
	print('The transformed vector (rotations about FIXED FRAME) is:\n',v01)

	
