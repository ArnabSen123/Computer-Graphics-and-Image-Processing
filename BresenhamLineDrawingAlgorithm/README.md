For m>1:
Instead of x, y is increased by 1. Because here dy is greater than dx. So by increasing y everytime by 1 we calculate the value of x(xk Or xk+1).
Also the Equation has been adjusted.
pk = (2 * dx) - dy

if pk<0
    (pk = pk + (2 * dx))

else
    (x = x + 1),
    (pk = pk + (2 * dx) - (2 * dy))

Output:
For 0<m<1:
(1,1)
(2,1)
(3,2)
(4,2)
(5,3)
(6,3)
(7,4)
(8,4)

For(m>1):
(1,1)
(1,2)
(2,3)
(2,4)
(3,5)
(3,6)
(4,7)
(4,8)
  
