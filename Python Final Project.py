import random

def move(pr,pp,ps):
    p=random.uniform(0, 1)
    if p<pr:
        return('r')
    elif p<pr+pp:
        return('p')
    elif p<pr+pp+ps:
        return('s')
def adprob(p1,p2):
    dp=0.001
    if p1+dp>1 and p2-dp<0:
        p1=1
        p2=0
    elif p1+dp<1 and p2-dp>0:
        p1=p1+dp
        p2=p2-dp
    return([p1,p2])
    
    
def game():
    print("Welcome to Rock Paper Scissor Game by Hoang Le Cong.")
    print("Option 1: You will play Rock Paper Scissor with the computer")
    print("For option 1, you will input your choice as r, p, s")
    print("Option 2: Watch the result of two computer players")
    print("For option 2, 2 computers will play against each other and they will remember the last opponent move and adjust their strategy accordingly")
    option=0
    while(option!=1 and option!=2):
        try:
            option=int(input("Please select your option, only input 1 or 2: "))
        except (ValueError, IOError):
            print("Invalid input,try again. Only input 1 or 2")
    if option==1:
        hmovel=[]
        hscore=0
        hscorel=[]
        cmovel=[]
        cscore=0
        cscorel=[]
        print('You selected option 1, you will play against the computer')
        again=1
        rprob=1/3
        pprob=1/3
        sprob=1/3
        while again==1:
            hmove=1
            while(hmove!='r'and hmove!='p'and hmove!='s'):
                try:
                    hmove=str(input('Please input your move, either r, p, or s: ')).lower()
                except(TypeError, ValueError, IOError):
                    print("Invalid Input. Please only input r, p, or s: ")
            hmovel.append(hmove)
            rprobd=rprob #dummy for probabilities          
            pprobd=pprob
            sprobd=sprob
            cmove=move(rprob,pprob,sprob)
            cmovel.append(cmove)
            if hmove=='r' and cmove=='r':
                hscore=hscore+1
                hscorel.append(hscore)
                cscore=cscore+1
                cscorel.append(cscore)
                print('We have a draw')
            elif hmove=='r' and cmove=='p':
                cscore=cscore+2
                cscorel.append(cscore)
                hscorel.append(hscore)
                pprob=adprob(pprobd,sprobd)[0]
                sprob=adprob(pprobd,sprobd)[1]
                print('You lost, computer win with Paper')
            elif hmove=='r' and cmove=='s':
                hscore=hscore+2
                cscorel.append(cscore)
                hscorel.append(hscore)
                pprob=adprob(pprobd,sprobd)[0]
                sprob=adprob(pprobd,sprobd)[1]
                print('You win, computer lost with Scissor')
            elif hmove=='p' and cmove=='r':
                hscore=hscore+2
                cscorel.append(cscore)
                hscorel.append(hscore)
                sprob=adprob(sprobd,rprobd)[0]
                rprob=adprob(sprobd,rprobd)[1]
                print('You win, computer lost with Rock')
            elif hmove=='p' and cmove=='p':
                cscorel.append(cscore)
                hscorel.append(hscore)
                print('We have a draw')                
            elif hmove=='p' and cmove=='s':
                cscore=cscore+2
                cscorel.append(cscore)
                hscorel.append(hscore)
                sprob=adprob(sprobd,rprobd)[0]
                rprob=adprob(sprobd,rprobd)[1]
                print('You lose, computer win with Scissor')
            elif hmove=='s' and cmove=='r':
                cscore=cscore+2
                cscorel.append(cscore)
                hscorel.append(hscore)
                rprob=adprob(rprobd,pprobd)[0]
                pprob=adprob(rprobd,pprobd)[1]
                print('You lose, computer win with Rock')                
            elif hmove=='s' and cmove=='p':
                hscore=hscore+2
                cscorel.append(cscore)
                hscorel.append(hscore)
                rprob=adprob(rprobd,pprobd)[0]
                pprob=adprob(rprobd,pprobd)[1]
                print('You win, computer lose with Paper')
            elif hmove=='s' and cmove=='s':
                cscorel.append(cscore)
                hscorel.append(hscore)
                print('We have a draw')  
            try:
                again=int(input('Do you want to play again? 0 for no and 1 for yes: '))
            except(TypeError, ValueError, IOError):
                print("Invalid Input. Please choose 0 or 1: ")
        print('Game ended, thank you for playing the game')
        print('Your total score is %s and computer score is %s'%(hscore,cscore))
    else:
        c1movel=[]
        c1score=0
        c1scorel=[]
        c2movel=[]
        c2score=0
        c2scorel=[]
        print('You selected option 1, you will play against the computer')
        again=1
        rprob1=1/3
        pprob1=1/3
        sprob1=1/3
        rprob2=1/3
        pprob2=1/3
        sprob2=1/3
        while again==1:
            c1move=move(rprob1,pprob1,sprob1)
            c1movel.append(c1move)
            rprobd1=rprob1 #dummy for probabilities of computer 1         
            pprobd1=pprob1
            sprobd1=sprob1
            rprobd2=rprob2 #dummy for probabilities of computer 1         
            pprobd2=pprob2
            sprobd2=sprob2
            c2move=move(rprob2,pprob2,sprob2)
            c2movel.append(c2move)
            if (c1move=='r' and c2move=='r'):
                c1score=c1score+1
                c1scorel.append(c1score)
                c2score=cscore+1
                c2scorel.append(cscore2)
                print('We have a draw')
            elif (c1move=='r' and c2move=='p'):
                c2score=c2score+2
                c2scorel.append(c2score)
                c1scorel.append(c1score)
                sprob1=adprob(sprobd1,rprobd1)[0]
                rprob1=adprob(sprobd1,rprobd1)[1]
                pprob2=adprob(pprobd2,sprobd2)[0]
                sprob2=adprob(pprobd2,sprobd2)[1]
                print('computer 1 lost, computer 2 win with Paper')
            elif c1move=='r' and c2move=='s':
                c1score=c1score+2
                c2scorel.append(c2score)
                c1scorel.append(c1score)
                rprob1=adprob(rprobd1,pprobd1)[0]
                pprob1=adprob(rprobd1,pprobd1)[1]
                pprob2=adprob(pprobd2,sprobd2)[0]
                sprob2=adprob(pprobd2,sprobd2)[1]
                print('You win, computer 2 lost with Scissor')
            elif hmove=='p' and cmove=='r':
                c1score=c1score+2
                c2scorel.append(c2score)
                c1scorel.append(c1score)
                pprob1=adprob(pprobd1,sprobd1)[0]
                sprob1=adprob(pprobd1,sprobd1)[1]
                sprob2=adprob(sprobd2,rprobd2)[0]
                rprob2=adprob(sprobd2,rprobd2)[1]
                print('You win, computer 2 lost with Rock')
            elif (c1move=='p' and c2move=='p'):
                c1score=c1score+1
                c1scorel.append(c1score)
                c2score=cscore+1
                c2scorel.append(cscore2)
                print('We have a draw')                
            elif c1move=='p' and c2move=='s':
                c2score=c2score+2
                c2scorel.append(c2score)
                c1scorel.append(c1score)
                pprob1=adprob(pprobd1,rprobd1)[0]
                rprob1=adprob(pprobd1,rprobd1)[1]
                sprob2=adprob(sprobd2,rprobd2)[0]
                rprob2=adprob(sprobd2,rprobd2)[1]
                print('You lose, computer 2 win with Scissor')
            elif c1move=='s' and c2move=='r':
                c2score=c2score+2
                c2scorel.append(c2score)
                c1scorel.append(c1score)
                sprob1=adprob(sprobd1,pprobd1)[0]
                pprob1=adprob(sprobd1,pprobd1)[1]
                rprob2=adprob(rprobd2,pprobd2)[0]
                pprob2=adprob(rprobd2,pprobd2)[1]
                print('You lose, computer win with Rock')                
            elif c1move=='s' and c2move=='p':
                c1score=c1score+2
                c2scorel.append(c2score)
                c1scorel.append(c1score)
                sprob1=adprob(sprobd1,rprobd1)[0]
                rprob1=adprob(sprobd1,rprobd1)[1]
                rprob2=adprob(rprobd2,pprobd2)[0]
                pprob2=adprob(rprobd2,pprobd2)[1]
                print('You win, computer 2 lose with Paper')
            elif hmove=='s' and cmove=='s':
                c1score=c1score+1
                c1scorel.append(c1score)
                c2score=cscore+1
                c2scorel.append(cscore2)
                print('We have a draw')  
            try:
                again=int(input('Do you want to watch another match? 0 for no and 1 for yes: '))
            except(TypeError, ValueError, IOError):
                print("Invalid Input. Please choose 0 or 1: ")
        print('Game ended, thank you for watching the game')
        print('computer 1 score is %s and computer 2 score is %s'%(c1score,c2score))
game()
