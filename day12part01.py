"""With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of this cave
anytime soon is by finding a path yourself. Not just a path - the only way to know if you've found the best path is to
find all of them.

Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle
input). For example:

start-A
start-b
A-c
A-b
b-d
A-end
b-end

This is a list of how all of the caves are connected. You start in the cave named start, and your destination is the cave
named end. An entry like b-d means that cave b is connected to cave d - that is, you can move between them.

So, the above cave system looks roughly like this:

    start
    /   \
c--A-----b--d
    \   /
     end

Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more than once.
There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b). It would
be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them
multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

Given these rules, there are 10 paths through this example cave system:

start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end

(Each line in the above list corresponds to a single path; the caves visited by that path are listed in the order they are visited
and separated by commas.)

Note that in this cave system, cave d is never visited by any path: to do so, cave b would need to be visited twice (once on the way
to cave d and a second time when returning from cave d), and since cave b is small, this is not allowed.

How many paths through this cave system are there that visit small caves at most once?
"""

routes = '''zi-end
XR-start
zk-zi
TS-zk
zw-vl
zk-zw
end-po
ws-zw
TS-ws
po-TS
po-YH
po-xk
zi-ws
zk-end
zi-XR
XR-zk
vl-TS
start-zw
vl-start
XR-zw
XR-vl
XR-ws'''

routes = routes.strip().split('\n')
routes = [route.split('-') for route in routes]

routeDict = {}
for route in routes:
    routeDict[route[0]] = []
    routeDict[route[1]] = []
for route in routes:
    routeDict[route[0]].append(route[1])
    routeDict[route[1]].append(route[0])

def countPaths(seen=[],root='start'):
    if root == 'end':
        return 1
    if root in seen:
        if root == 'start':
            return 0
        if root.islower():
             return 0
    return sum(countPaths(seen+[root], n) for n in routeDict[root])

print(countPaths())
