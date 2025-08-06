class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans="" 
        for j in range(len(num2)-1,-1,-1):
            #print("j:",num2[j])
            ans_j=""
            kuriagari=0
            for i in range(len(num1)-1,-1,-1):
                ans_j = str((int(num1[i])*int(num2[j]) + kuriagari)%10) + ans_j
                kuriagari = (int(num1[i])*int(num2[j])+ kuriagari)//10
            else:
                if kuriagari > 0:
                    ans_j = str(kuriagari) + ans_j
            ans_j+=("0"*(len(num2)-1-j))

            digit=max(len(ans),len(ans_j))
            ans=(("0"*digit)+ans)[-1*digit:]            
            ans_j=(("0"*digit)+ans_j)[-1*digit:]     
            #print("ansbf:",ans)
            #print("ans_j:",ans_j)

            new_ans=""
            kuriagari=0
            for i in range(digit-1,-1,-1):
                new_ans = str((int(ans[i])+int(ans_j[i]) + kuriagari)%10) + new_ans
                kuriagari = (int(ans[i])+int(ans_j[i])+ kuriagari)//10
            else:
                #print("kuriagari:",kuriagari)
                if kuriagari>0:
                    new_ans = str(kuriagari) + new_ans
            ans=new_ans
            #print("ansaf:",ans)
            #print("------")
        
        new_ans=""
        for i in range(len(ans)):
            if(ans[i] != "0"):
                new_ans=ans[i:]
                break
        else:
            if len(new_ans) == 0:
                new_ans="0"
        ans=new_ans
        return ans