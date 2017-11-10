from fractions import Fraction as Frac
def probs(n,m): #returns a set of probabilities of winning,
    #drawing and losing given your opponent must take n steps and you must take m
    win = Frac()
    draw = Frac()
    loss = Frac()
    i=0
    while (i<6):
        i+=1
        j=0
        while j<6:
            j+=1
            if(n-i<=0):
                if(n-i-(m-j)<0):
                    loss+=Frac(1,36)
                elif (n-i-(m-j)>0):
                    win+=Frac(1,36)
                elif (n-i-(m-j)==0):
                    draw+=Frac(1,36)
                else:
                    print("Error: difference neither above, below, or equal to 0")
            else: #n-i>0 ie the opponent has not reached the end
                if (m-j<=0):
                    win+=Frac(1,36)
                else: #m-j>0 ie we have not reached the end
                    cascade=probs(n-i,m-j)
                    win+=(Frac(1/36)*cascade[0])
                    draw+=(Frac(1/36)*cascade[1])
                    loss+=(Frac(1/36)*cascade[2])

    return [win,draw,loss]

def decompose(a):
    win=a[0]
    draw=a[1]
    loss=a[2]
    print("Win:  %.4f" %win)
    print("Draw: %.4f" %draw)
    print("Loss: %.4f" %loss)

def profit(a):
    win=a[0]
    draw=a[1]
    loss=a[2]
    profit=win*20+draw*15+loss*10
    print("Profit: %.4f" %profit)

def calculate(n,m):
    distribution=probs(n,m)
    decompose(distribution)
    profit(distribution)
    
