
import numpy as np
from numpy import cos, sin, deg2rad


def get_sensmat_itmx(a1,a2,a3,r):
    a1 = deg2rad(a1+90)
    a2 = deg2rad(a2+90)
    a3 = deg2rad(a3+90)
    S = np.array([[cos(a1),sin(a1),r],
                [cos(a2),sin(a2),r],
                [cos(a3),sin(a3),r]])
    print(np.linalg.inv(S))

def get_sensmat_etmx(a1,a2,a3,r):#?
    a1 = deg2rad(a1)
    a2 = deg2rad(a2)
    a3 = deg2rad(a3)
    S = np.array([[sin(a1),-cos(a1),r],
                [sin(a2),-cos(a2),r],
                [sin(a3),-cos(a3),r]])
    print(np.linalg.inv(S))

    
def get_sensmat(a1,a2,a3,r):
    a1 = deg2rad(a1)
    a2 = deg2rad(a2)
    a3 = deg2rad(a3)
    S = np.array([[cos(a1),sin(a1),r],
                [cos(a2),sin(a2),r],
                [cos(a3),sin(a3),r]])    
    print(np.linalg.inv(S))

def get_sensmat_etmy(a1,a2,a3,r):
    a1 = deg2rad(a1+180)
    a2 = deg2rad(a2+180)
    a3 = deg2rad(a3+180)
    S = np.array([[-cos(a1),-sin(a1),r],
                [-cos(a2),-sin(a2),r],
                [-cos(a3),-sin(a3),r]])
    S = np.array([[cos(a1),sin(a1),r],
                [cos(a2),sin(a2),r],
                [cos(a3),sin(a3),r]])    
    print(np.linalg.inv(S))
    
    
if __name__ == '__main__':
    params = {
        'ETMX':[84,324,204,0.5940],
        'ETMY':[174,54,294,0.5940],
        'ITMX':[264,144,24,0.5940],
        'ITMY':[354,234,114,0.5940],
        'BS':[],
        'SR2':[],
        'SR3':[],
        'SRM':[],
        }
    print('ITMY.. OK')
    get_sensmat(*params['ITMY'])
    print('ITMX.. OK')    
    get_sensmat_itmx(*params['ITMX'])
    print('ETMY.. OK')    
    get_sensmat_etmy(*params['ETMY'])
    print('ETMX.. NO')    
    get_sensmat_etmx(*params['ETMX'])   

    
