class Category:
  def __init__(self,cat):
      self.category=cat
      self.ledger=[]
  def deposit(self,amount,description=""):
      tdic=dict()
      tdic['amount']=amount
      tdic['description']=description
      self.ledger.append(tdic)
  def get_balance(self):
      balance=0
      for i in self.ledger:
          balance+=i['amount']
      return balance
  def check_funds(self,amount):
    # print("dsbjh",str(amount))
    # print(self.get_balance())
    if amount>self.get_balance():
        # print("fal")
        return False
    else:
      return True
  def withdraw(self,wamt,description=""):
      if self.check_funds(wamt):
          tdic=dict()
          tdic['amount']=-1*wamt
          tdic['description']=description
          self.ledger.append(tdic)
          return True
      else:
        return False
  def transfer(self,amount,category2):
      if self.check_funds(amount):
          descp="Transfer to "+category2.category
          self.withdraw(amount,descp)
          descp="Transfer from "+self.category
          category2.deposit(amount,descp)
          return True
      else:
          return False  
  def __str__(self):
      stars=30-len(self.category)
      row1=""
      for i in range(int(stars/2)):
          row1+="*"
      row1+=self.category
      for i in range(stars-int(stars/2)):
          row1+="*"
      row1+="\n"
      
      rowi=""
      for trans in self.ledger:
          diff=23-len(trans['description'])
          if diff<0 :
              rowi+=trans['description'][0:23]
          else:
              rowi+=trans['description']
              for k in range(diff):
                  rowi+=" "
          amt='{:.2f}'.format(trans['amount'])
          diff2=7-len(amt)
          for j in range(diff2):
              rowi+=" "
          rowi+=amt+"\n"
      row2="Total: "+str(self.get_balance())
      return row1+rowi+row2

  def spent(self):
    spent=0
    for i in self.ledger:
      if i['amount']<0:
          spent+=abs(i['amount'])
    return round(spent,2)
  
def create_spend_chart(categories):
  rowtitle="Percentage spent by category\n"
  rowslist=["100| "," 90| "," 80| "," 70| "," 60| "," 50| "," 40| "," 30| "," 20| "," 10| ","  0| "]
  spentlist=[]
  rowdash="    -"
  catname=[]
  for category in categories:
      rowdash+="---"
      catname.append(category.category)
      spentlist.append(category.spent())
  rowdash+="\n"
  totalspt=0
  for j in spentlist:
    totalspt+=j
  # print(spentlist)
  for k in range(len(spentlist)):
    temp=(spentlist[k]*10)/totalspt
    spentlist[k]=int(temp)
  # print(spentlist)
  for i in range(11):
      for s in spentlist:
          if 10-i<=s:
            rowslist[i]+="o  "
          else :
            rowslist[i]+="   "
      rowslist[i]+="\n"

  maxlen=0
  for l in catname:
    if maxlen<len(l):
      maxlen=len(l)
  namelist=[]
  for i in range(maxlen):
    tempst="     "
    for n in catname:
      if i<len(n):
        tempst+=n[i]+"  "
      else:
        tempst+="   "
    if i != maxlen-1:
      tempst+="\n"
    namelist.append(tempst)

  ansstring=rowtitle
  for r in rowslist:
    ansstring+=r
  ansstring+=rowdash
  for n in namelist:
    ansstring+=n
  return ansstring