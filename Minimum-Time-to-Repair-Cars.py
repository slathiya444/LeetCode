# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def calculate_repaired_cars(time):
            total_cars=0
            for rank in ranks:
                total_cars += int(sqrt(time / rank))
            return total_cars
                

        left, right = 1, ranks[0]*cars*cars
        res = -1

        while left <= right:
            mid = (left+right)//2
            repaired = calculate_repaired_cars(mid)
            if repaired >= cars:
                res = mid
                right=mid-1
            else:
                left=mid+1
        
        return res