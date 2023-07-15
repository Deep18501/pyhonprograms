

def arithmetic_arranger(problems,showAns=False):
    if len(problems)>5:
      return "Error: Too many problems."
    c1=[]
    op=[]
    c2=[]
    for i in problems:
      prob=i.split(" ")
      try :
        c1.append(int(prob[0]))
        c2.append(int(prob[2]))
      except:
        return "Error: Numbers must only contain digits."
      op.append(prob[1])


    for i in range(len(c1)):
      if op[i]!="+" and op[i]!="-":
        # print(i," ",op[i])
        return "Error: Operator must be '+' or '-'."
      if c2[i]>9999|c1[i]>9999 :
        return "Error: Numbers cannot be more than four digits."
    
    res=[]
    for r in range(len(c1)):
      if op[r]=='+':
        res.append(c1[r]+c2[r])
      else :
        res.append(c1[r]-c2[r])
      c1[r]=str(c1[r])
      c2[r]=str(c2[r])
      res[r]=str(res[r])
    row1=""
    row2=""
    row3=""
    row4=""
    for j in range(len(res)):
      row1+="  "
      row2+=op[j]+" "
      max=0
      if len(c1[j])>=len(c2[j]):
          max=len(c1[j])
          row1+=c1[j]
          diff=max-len(c2[j])

          for d in range(diff):
              row2+=" "
          row2+=c2[j]
          for minus in range(max+2):
              row3+="-"
          diff2=max+2-len(res[j])
          for d in range(diff2):
              row4+=" "
          row4+=res[j]
  
      else:
          max=len(c2[j])
          row2+=c2[j]
          diff=max-len(c1[j])
          # print(" diff=",row1,"e")
          for d in range(diff):
              row1+=" "
          row1+=c1[j]
          
          for minus in range(max+2):
              row3+="-"
          diff2=max+2-len(res[j])
          for d in range(diff2):
              row4+=" "
          row4+=res[j]
  
      if j!=len(res)-1:
        row1+="    "
        row2+="    "
        row3+="    "
        row4+="    "
      else:
        row1+="\n"
        row2+="\n"
        
    arranged_problems=""
    if showAns :
        arranged_problems=row1+row2+row3+"\n"+row4
    else :
        arranged_problems=row1+row2+row3
    # print(arranged_problems)
    return arranged_problems