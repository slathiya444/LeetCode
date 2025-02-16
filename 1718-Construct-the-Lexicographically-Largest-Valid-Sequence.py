class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        self.size = 2*n-1 #size of the array
        self.arr = [-1]*self.size #construct output array
        
        def solve(i, seen):
            if len(seen) == n or i >= self.size: #if we have seen all n numbers or i > self.size return true
                return True
            if self.arr[i] != -1: #move to next index if current one is taken
                return solve(i+1, seen)
            
            for idx in range(n, 0, -1):
                if idx in seen: continue #continue if this number has been used
                if i+idx >= self.size and idx != 1: continue #continue if this number would be out of index
                if idx != 1 and self.arr[i+idx] != -1: continue #continue if the element that in index i+idx (this is the distance) is not available 
                
                seen.add(idx)
                
				#add the number to the array
                self.arr[i] = idx
                if idx != 1:
                    self.arr[i+idx] = idx
                
                ans = solve(i+1, seen)
                if ans: return True #stop once we find the first working sequence
                elif idx != 1: self.arr[i+idx] = -1 #if sequence did not work reset the element at index i+idx.
				#no need to do this for index i since it will be overwritten next iteration
                
                seen.remove(idx)
            
            self.arr[i] = -1 #reset index if no numbers worked
            return False
        solve(0, set())
        
        return self.arr