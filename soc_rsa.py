  
def gcd(m,n): 
    if n==0: 
        return abs(m) 
    else: 
        return gcd(n,m%n) 

#input variables
p = input()
q = input()
msg = input()

#calculate n
n = int(p)*int(q) 

#calculate phi
phi = (int(p)-1)*(int(q)-1) 

#calculate k
for k in range(2,phi): 
    if gcd(k,phi)== 1: 
        break
  
for i in range(1,10): 
    x = 1 + i*phi 
    if x % k == 0: 
        d = int(x/k) 
        break

local_cipher = pow(int(msg),k) 
public_key = local_cipher % n 
  
decrypt_t = pow(public_key,d) 
private_key = decrypt_t % n 
  
print(' n = '+str(n))
print(' k = '+str(k))
print(' phi = '+str(phi))
print(' d = '+str(d)) 
print(' public key = '+str(public_key))
print(' private key = '+str(private_key))