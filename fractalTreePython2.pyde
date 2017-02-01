import random, math, time

def setup():
    global leafFall
    global counter
    global tree
    global leaves
    tree = []
    leaves = []
    size(600, 600)
    counter = 0
    v1 = PVector(width/2, height)
    v2 = PVector(width/2, height-100)
     
    def leafFall():
        leafLen = len(leaves)
        randomLeaf = math.floor(random.random()*leafLen)
        while leaves[int(randomLeaf)].y < height-1:
            leaves[int(randomLeaf)].y += 0.1
            
    root = Branch(v1, v2)
    tree.append(root)
    
def keyReleased():
    if key == 'r' or key == 'R':
        frameRate(60)
        setup()
    
    
def mouseClicked():
    global counter
    for i in range(0, len(tree)):
        if not tree[i].finished:
            tree.append(tree[i].branchL())
            tree.append(tree[i].branchR())
        tree[i].finished = True
    counter += 1
    #print counter
    if counter % 3 == 0 and counter < 9:
        for i in range(0, len(tree)):
            if not tree[i].finished:
                leaf = tree[i].ending.copy()
                leaves.append(leaf)
                
#-----------------#
#branch objects
class Branch():
    
    def __init__(self, begin, ending):
        self.begin = begin
        self.ending = ending
        self.finished = False
    
    
    def branchR(self):
        
        dir = PVector.sub(self.ending, self.begin)
        dir.rotate(PI / 4)
        dir.mult(0.86)
        newEnd = PVector.add(self.ending, dir)
        
        right = Branch(self.ending, newEnd)
        return right
    
    def branchL(self):
        
        dir = PVector.sub(self.ending, self.begin)
        dir.rotate(-PI / 4)
        dir.mult(0.6)
        newEnd = PVector.add(self.ending, dir)
        
        left = Branch(self.ending, newEnd)
        return left
    
    def show(self):
        stroke(255)
        line(self.begin.x, self.begin.y, self.ending.x, self.ending.y)
#--------------------#

def draw():
    
    global counter
    background(51)
    fill(0, 102, 154)
    textSize(32)
    
    for i in range(0, len(tree)):
        tree[i].show()
   
    #r = random.random()    
    #if len(leaves) > 0 and r > 0 and r < 0.09:
    #    print 'run',
    #    leafFall()
       
    
    #leafLen = len(leaves)
    #randomLeaf = math.floor(random.random()*leafLen)
    #if len(leaves) > 0:
    #    leaves[int(randomLeaf)].y += 1
    #    frameRate(3)

    
    # if r < 0.01 and r > 0 and len(leaves) > 0:
    #     while True:
    #         for i in leaves:
    #             i.y += 1
    #             if i.y > height - 1:
    #                 return False
        
    for i in range(0, len(leaves)):
        fill(255, 0, 100)
        ellipse(leaves[i].x, leaves[i].y, 8, 8)
        if len(tree) > 0:
            if keyPressed:
                for i in leaves:
                    if counter > 5:
                        frameRate(8)
                    r = random.random()*0.5
                    i.y += r
                    if i.y > height-1:
                        i.y = height-1
                
            

    
    
    