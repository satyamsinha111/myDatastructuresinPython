#creating stack data structures in python
# def kedenAlgorithm(array):
#     max_so_far = 0
#     max_ending_here = 0
#     for item in array:
#         max_ending_here=max_ending_here+item
#         if max_ending_here<0:
#             max_ending_here=0
#         elif max_so_far<max_ending_here:
#             max_so_far=max_ending_here
#     return max_so_far
class Stack:
    def __init__(self,Capacity):
        self.Capacity=Capacity
        self.array=[]

    def CreateStack(self,Cap):
        self.Capacity=Cap
        self.array=[]
        self.top=-1

    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False

    def isFull(self):
        if self.top==self.Capacity-1:
            return True
        else:
            return False

    def push(self,num):
        if self.isFull()==False:
            self.top+=1

            self.array.append(num)


        else:
            return "Overflow stack is full"

    def pop(self):
        if self.isEmpty()==False:
            item=self.array[-1]
            self.top-=1
            return item
        else:
            return -1

# finding the largest sum in contagious list using kedens algorithm

class Array:
    def __init__(self,array):
        self.max_ending_here=0
        self.max_so_far=0
        self.array=array
    def kedensAlgo(self):
        for item in self.array:
            self.max_ending_here=self.max_ending_here+item
            if self.max_ending_here<0:
                self.max_ending_here=0
            elif self.max_ending_here>self.max_so_far:
                self.max_so_far=self.max_ending_here
        return self.max_so_far




if __name__ == '__main__':
    stack=Stack(3)
    stack.CreateStack(4)
    print(stack.push(20))
    print(stack.push(20))
    print(stack.push(20))
    print(stack.push(20))



