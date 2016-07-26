<<<<<<< HEAD
from . import start, n1, s1, e1, w1, n1w1, w2, s1w2, n1e1, s2, s3, e3
=======
from . import start, n1, s1, e1, e2, w1, n1w1, w2, s1w2, n1e1, s2, s3, s1e1
>>>>>>> 9ae5f698999dff9bcd6b3fcf737610eaf6175807

grid = {
    (0, 0): start,
    (0, 1): n1,
    (0, -1): s1,
    (0, -2): s2,
    (0, -3): s3,
    (1, 0): e1,
    (2, 0): e2,
    (-1, 0): w1,
    (-1, 1): n1w1,
    (-2, 0): w2,
    (-2, 1): w2,
    (-2, -1): s1w2,
    (1, 1): n1e1,
    (1, 3): e3,
    (1, -1): s1e1
}
