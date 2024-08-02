# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.idx = -1
        self.iter = None
        self.nl = nestedList
        self.__advanceIdx()
        
    
    def next(self) -> int:
        if self.iter:
            res = self.iter.next()
            if not self.iter.hasNext():
                self.__advanceIdx()
        else:
            res = self.nl[self.idx].getInteger()
            self.__advanceIdx()
        return res
        
    
    def hasNext(self) -> bool:
                return self.idx < len(self.nl)
    def __advanceIdx(self):
        while True:
            self.idx += 1
            self.iter = None
            if self.idx < len(self.nl) and not self.nl[self.idx].isInteger():
                self.iter = NestedIterator(self.nl[self.idx].getList())
            if self.iter == None or self.iter.hasNext():
                break
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())