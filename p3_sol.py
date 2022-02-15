# import the rigid body motion module
import rbm
import p2_sol
import math
import numpy as np

if __name__ == '__main__':

	# update the output format
	np.set_printoptions(precision = 2, suppress = True)
	# define a 3D vector
	v0 = rbm.vec(0,1,1) # values from the example in class
	
	#define values
	alpha = math.pi/2 
	gamma = math.pi/2 
	
	#translation along x-axis
	tx1 = p2_sol.trans_x(2.5)
	#translation along z-axis
	tz1 = p2_sol.trans_z(0.5)
	#translation along y-axis
	ty1 = p2_sol.trans_y(-1.5)
	
	#calculate total Transformation 1 (current frame)
	H_1 = np.matmul(np.matmul(tx1,tz1),ty1)
	print('The transformed matrix (CURRENT FRAME) is:\n',H_1)
	
	#calculate total Transformation 2 (current frame)
	H_2 = np.matmul(np.matmul(tz1,tx1),ty1)
	print('The transformed matrix (CURRENT FRAME) is:\n',H_2)
	
	#calculate total Transformation 3 (fixed frame)
	H_3 = np.matmul(np.matmul(ty1,tz1),tx1)
	print('The transformed matrix (FIXED FRAME) is:\n',H_3)

	#calculate total Transformation 4 (fixed frame)
	H_4 = np.matmul(np.matmul(ty1,tx1),tz1)
	print('The transformed matrix (FIXED FRAME) is:\n',H_4)

	#rotation about x-axis
	rx = p2_sol.rot_x(alpha)
	#translation along x-axis
	tx2 = p2_sol.trans_x(3)
	#translation along z-axis
	tz2 = p2_sol.trans_z(-3)
	#rotation about z-axis
	rz = p2_sol.rot_z(gamma)
	
	#calculate total (current frame)
	H_5 = np.matmul(np.matmul(np.matmul(rx,tx2),tz2),rz)
	print('The transformed matrix (rotations about CURRENT FRAME) is:\n',H_5)
	
