# Spiral-Matrix-in-Python
In this code we Spin throw a 2d Matrix and print the elements.


 1  2  3  4
 5  6  7  8
 9 10 11 12
 13 14 15 16
                
Answer: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Notes
prints comes as
row col
[1, 1] 
[1, 2] 
[1, 3] 
[1, 4] 
[2, 4] 
[3, 4] 
[4, 4] 
[4, 3] 
[4, 2] 
[4, 1] 
[3, 1] 
[2, 1] 
[2, 2] 
[2, 3] 
[3, 3] 
[3, 2]

centre: No Centre
pattern[+, -] [-, -] [-, +] [+, -]
edge: [1, 4] [4, 4] [4, 1] [2, 1]
      [2, 3] [3, 3] [3, 2]
      
  
----------------------------------------------------------------------------------------------------------------------------------------
 1  2  3  4  5    
 6  7  8  9 10   
11 12 13 14 15   
16 17 18 19 20
21 22 23 24 25

Answer: 1 2 3 4 5 10 15 20 25 24 23 22 21 16 11 6 7 8 9 14 19 18 17 12 13

Notes
print comes as:
row col
[1, 1]
[1, 2]
[1, 3]
[1, 4]
[1, 5]
[2, 5]
[3, 5]
[4, 5]
[5, 5]
[5, 4]
[5, 3]
[5, 2]
[5, 1]
[4, 1]
[3, 1]
[2, 1]
[2, 2]
[2, 3]
[2, 4]
[3, 4]
[4, 4]
[4, 3]
[4, 2]
[3, 2]
[3, 3]

edges: [1, 5] [5, 5] [5, 1] [2, 1]
       [2, 4] [4, 4] [4, 2] [3, 2] 
pattern:[+, -] [-, -] [-, +] [+, -]

centre:[3, 3] 
