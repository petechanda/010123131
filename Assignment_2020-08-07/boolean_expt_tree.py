### STUDENT NUMBER : 6201012630029
### Assignment_2020-08-07

class boolean_tree(object):
    def __init__(self, expression):
        self.boolExp = expression
        self.listVar = []
    
    def lstExpt(self):
        var = ''
        num = 1
        for i in self.boolExp:
            if i == '&' or i == '+' or i == '!':
                self.listVar.append(i)
            elif i == 'l'or i == '0'or i == '1'or i == '2'or i == '3'or i == '4'or i == '5':
                var += i
                if i != 'l':
                    self.listVar.append(var)
                    var = ''
            elif i =='(' or i ==')':
                self.listVar.append(i)
            elif i == ' ':
                self.listVar.append(i)
                num += 1
        return self.listVar
    
    def exptTree(self):
        T = []
        n = []
        for i in range(len(self.listVar)):
            if self.listVar[i]=='!':
                if self.listVar[i+1] != '(':
                    t = [self.listVar[i],None,self.listVar[i+1]]
                    T.append(t)
                elif self.listVar[i+1] == '(':
                    t = [self.listVar[i],None,' ']
                    T.append(t)
            elif self.listVar[i]=='&'or self.listVar[i]=='+':
                t = [self.listVar[i],self.listVar[i-1],self.listVar[i+1]]
                T.append(t)
        for i in range(len(T)):
            n.append(1)
        for i in range(len(T)):
            if T[i][1]==' ':
                T[i][1] = T[i-1]
                n[i] += 1
            if T[i][2]==' ':
                T[i][2] = T[i+1]
                n[i] += 1
        index_max = n.index(max(n))
        return T[index_max]
            
b1 = boolean_tree('l0&l1 + !(l1&l2)')
print(b1.lstExpt())
print(b1.exptTree())