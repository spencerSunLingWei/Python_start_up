class Matrix(object):
    def __init__(self, matrix):
        '''(Matrix, list)-> NoneType
        creates a data attribute elements and instantiate it to the matrix.

        Preconditions: list e contains 2 sublists, all the sublists in e have the same length.

        Complete the instance variable definitions DO NOT CHANGE THE VARIABLE NAMES. Feel free to
        add new ones
        '''
        self.elements = matrix
        if len(matrix) == 0:
            self.cols = 0
            self.rows = 0
        else:
            self.cols = len(matrix[0])
            self.rows = len(matrix)
            
    def __str__(self):
        '''(Matrix) -> str 
        returns a string representation of the elements of the matrix. When passed to print() this
        representation should result in the original matrix being displayed as follows: each row
        will be displayed on a separate line, with each element in a row separated from the next by
        one, and only one blank space. The string representation should not contain any additional
        blank spaces. Print nothing if the matrix is empty.

        >>> print(Matrix([[1,2], [3,4]]))
        1 2
        3 4
        >>> print(Matrix([[0,-1.5,2.0], [-1, 4.5, 0]]))
        0 -1.5 2.0
        -1 4.5 0 
        >>> print(Matrix([[]]))

        '''
        matrix = self.elements
        result=''
        for i in range (0, len(matrix)-1):
            for j in range (0,len(matrix[0])):
                result += str(matrix[i][j])
                result += " "
            result += "\n"
        for i in range(len(matrix)-1,len(matrix)):
             for j in range (0,len(matrix[0])):
                result += str(matrix[i][j])
                result += " "
        return result
        
    
    def __repr__(self):
        """Do not change this."""
        return self.__str__()

    def __eq__(self, other):
        ''' (Matrix) -> bool
        Returns if the self matrix is equal (elementwise) to the other matrix

        >>> Matrix([[1,1],[1,1]]) == Matrix([[1,1],[1,1]])
        True
        >>> Matrix([[1,1],[1,2]]) == Matrix([[1,1],[1,1]])
        False
        '''
        
        if self.elements == other.elements:
            return True
        else:
            return False

        
        

    def add(self, other):
        ''' (Matrix, Matrix) -> Matrix
        Returns the result (as a new Matrix object) of adding the second input Matrix to the first.
        Return an empty matrix if the matrices has mismatching sizes.
        
        >>> Matrix([[1,1],[1,1]]).add(Matrix([[-1,3],[0,0]]))
        0 4
        1 1
        >>> Matrix([[-1,3,0],[0,0,0],[1.5,1,1]]).add(Matrix([[2,-0.5,1],[0,0,0],[0,0,1]]))
        1 2.5 1
        0 0 0
        1.5 1 2
        '''

        matrix = self.elements
        matrix2 = other.elements
        result=[]
        if len(matrix) != len(matrix2) or len(matrix[0]) != len(matrix2[0]):
            return Matrix([[]])
        else:

        
            for i in range (0, len(matrix)):
                smallresult=[]
                for j in range (0,len(matrix[0])):
                    smallresult.append(matrix[i][j]+matrix2[i][j])
                result.append(smallresult)
            
            
            return Matrix(result)
        


    def mul(self, k):
        '''(Matrix, Matrix) -> Matrix
        Returns the scalar product of the input matrix with scalar k as a new matrix onject.
        
        >>> Matrix([[1,1],[1,1]]).mul(1)
        1 1
        1 1
        >>> Matrix([[1,3],[-2,-1]]).mul(-1)
        -1 -3
        2 1
        '''
        matrix = self.elements
        
        result=[]
        for i in range (0, len(matrix)):
            smallresult=[]
            for j in range (0,len(matrix[0])):
                smallresult.append(matrix[i][j]*k)
            result.append(smallresult)
            
            
        return Matrix(result)
        


    def sub(self, other):
        ''' (Matrix, Matrix) -> Matrix
        Returns the result (as a new Matrix object) of subtract the second input Matrix to the
        first. Return an empty matrix if the matrices has mismatching sizes.

        >>> Matrix([[1,1],[1,1]]).sub(Matrix([[-1,3],[0,0]]))
        2 -2
        1 1
        >>> Matrix([[-1,3,0],[0,0,0],[1.5,1,1]]).sub(Matrix([[2,-0.5,1],[0,0,0],[0,0,1]]))
        -3 3.5 -1
        0 0 0
        1.5 1 0
        '''

        matrix = self.elements
        matrix2 = other.elements
        result=[]

        if len(matrix) != len(matrix2) or len(matrix[0]) != len(matrix2[0]):
            return Matrix([[]])
        else:

        
            for i in range (0, len(matrix)):
                smallresult=[]
                for j in range (0,len(matrix[0])):
                    smallresult.append(matrix[i][j]-matrix2[i][j])
                result.append(smallresult)
            
            
        return Matrix(result)
        

    def trace(self):
        '''(Matrix) -> float
        Returns the trace of the input matrix as a floating point number. If the matrix is not
        square, return float('inf')

        >>> Matrix([[1,1],[2,2]]).trace() 
        3.0 
        >>> Matrix([[-1,3,0],[0,0,0],[1.5,1,1]]).trace()
        0.0
        '''

        matrix = self.elements
        resultList = []
        for i in range(0,len(matrix)):
            resultList.append(matrix[i][i])
        result = float(sum(resultList))
        return result
        
            
            



        

    def transpose(self):
        '''(Matrix) -> Matrix
        Returns the transpose of the input matrix as a new Matrix object.
        
        >>> Matrix([[1,2],[3,4]]).transpose()
        1 3
        2 4
        '''

        matrix = self.elements
        result=[]
        for i in range (0, len(matrix)):
            smallresult=[]
            for j in range (0,len(matrix[0])):
                smallresult.append(matrix[i][j])
            result.append(smallresult)

        tranresult=[]
        for j in range(0,len(matrix[0])):
            smalltranresult=[]
            for i in range(0,len(matrix)):
                smalltranresult.append(matrix[i][j])
            tranresult.append(smalltranresult)
        return Matrix(tranresult)
                
  

    def dot(self, other):
        '''(Matrix, Matrix) -> Matrix
        Returns a matrix product between self and other.

        If self and other has mismatching dimension, return an empty Matrix object. If not, return
        the result of self (dot) other

        >>> A = Matrix([[1,2],[3,4],[5,6]])
        >>> A.dot(A.transpose()) 
        5 11 17
        11 25 39
        17 39 61
        '''
        #making two list for matrix and other
        matrix = self.elements
        other = other.elements
        matrixlist=[]
        for i in range (0, len(matrix)):
            smallmatrixlist=[]
            for j in range (0,len(matrix[0])):
                smallmatrixlist.append(matrix[i][j])
            matrixlist.append(smallmatrixlist)
        otherlist=[]
        for i in range (0, len(other)):
            smallotherlist=[]
            for j in range (0,len(other[0])):
                smallotherlist.append(other[i][j])
            otherlist.append(smallotherlist)
            
        # consider if it can have dot product or not
        if len(matrixlist) != len(otherlist[0]):
            return Matrix([])
        else:
            lista=[]
            for j in range(0,len(matrix)):
                list1=[]
                for i in range(0,len(matrix)):
                    listb=[]
                    for a in range(0,len(matrix[0])):
                        listb.append(matrixlist[j][a]*otherlist[a][i])
                        b2 = sum(listb)
                    list1.append(b2)
                lista.append(list1)
            return Matrix(lista)
                
            
            
                
        
        
        
        


















        
    
