from mypackage import myModule
"""makes sure that 
"""
assert myModule.top_n([5,7,3,9,4], 3) == [9,7,5], "incorrect"
assert myModule.top_n([5,7,3,6,4,1,2], 5) == [7,6,5,4,3], "incorrect" 
assert myModule.top_n([4,7,1,8,3], 4) == [8,7,4,3], "incorrect"