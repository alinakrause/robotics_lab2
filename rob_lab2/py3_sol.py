# import the rigid body motion module
import rbm
import p2_sol
import math
import numpy as np

if __name__ == '__main__':
	# define a test value 
	alpha = math.pi/2 
	gamma = math.pi/2 
	# update the output format
	np.set_printoptions(precision = 2, suppress = True)
	# define a 3D vector
	v0 = rbm.vec(0,1,1) # values from the example in class
	# define a 3D rotation about y axes
	
	tx1 = p2_sol.trans_x(2.5)
	tz1 = p2_sol.trans_z(0.5)
	ty1 = p2_sol.trans_y(-1.5)
	
	H_1 = np.matmul(np.matmul(tx1,tz1),ty1)
	#v01 = H_1.dot(v0)
	
	print('The transformed vector (rotations about CURRENT FRAME) is:\n',H_1)
	
	H_2 = np.matmul(np.matmul(tz1,tx1),ty1)
	#v02 = H_2.dot(v0)
	
	print('The transformed vector (rotations about CURRENT FRAME) is:\n',H_2)
	
	# calculate a total rotation via FIXED FRAME
	H_3 = np.matmul(np.matmul(ty1,tz1),tx1)
	# calculate the results of rotation
	#v03 = H_3.dot(v0)
	print('The transformed vector (rotations about FIXED FRAME) is:\n',H_3)
	
	# calculate a total rotation via FIXED FRAME
	H_4 = np.matmul(np.matmul(ty1,tx1),tz1)
	# calculate the results of rotation
	#v04 = H_4.dot(v0)
	print('The transformed vector (rotations about FIXED FRAME) is:\n',H_4)

	rx = p2_sol.rot_x(alpha)
	tx2 = p2_sol.trans_x(3)
	tz2 = p2_sol.trans_z(-3)
	rz = p2_sol.rot_z(gamma)
	
	test = np.matmul(rx,tx2)
	test2 = np.matmul(test, tz2)
	H_5 = np.matmul(test2,rz)
	#H_5 = np.matmul(np.matmul(np.matmul(rx,tx2),tz2),rz)
	#v05 = H_5.dot(v0)
	print('The transformed vector (rotations about CURRENT FRAME) is:\n',H_5)
	
