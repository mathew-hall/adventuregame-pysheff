from . import start, n1, s1, e1, w1, n1w1, w2

grid = {
(0,0): start,
(0,1): n1,
(0,-1): s1,
(1,0): e1,
(-1,0): w1,
(-1,1): n1w1,
(-2,0): w2,
(-2,1): w2,
}
