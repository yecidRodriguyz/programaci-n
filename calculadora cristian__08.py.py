#calculadora 
sele=int(input("""*************************************************************
SELECCIONE LA OPERACION:
1. Suma
2. Resta
3. Multiplicacion
4. Divsion
5. Potencia
6. raiz
7. suma de potencias
8. promedio
9. comparacion
*************************************************************
"""))
if sele<1:
    print ("Error")
else:
    if sele>9:
        print ("Error")
if sele==1:
    num1=int(input("""**********
Primer numero: """))
    num2=int(input("""**********
Segundo numero: """))
    result= num1 + num2
    print (num1,"+",num2,"=",result)
    
else:
    if sele ==2:
        num1=int(input("""**********
Primer numero: """))
        num2=int(input("""**********
Segundo numero: """))
        result= num1 - num2
        print (num1,"-",num2,"=",result)
        
    else:
        if sele==3:
            num1=int(input("""**********
Primer numero: """))
            num2=int(input("""**********
Segundo numero: """))
            result=num1 *num2
            print(num1,"*",num2,"=",result)
            
        else:
            if sele==4:
                num1=int(input("""**********
Primer numero: """))
                num2=int(input("""**********
Segundo numero: """))
                result=num1 / num2
                print (num1,"/",num2,"=",result)
                
            else:
                if sele==5:
                     num1=int(input("""**********
Primer numero: """))
                     num2=int(input("""**********
Segundo numero: """))
                     result= num1 ** num2
                     print (num1,"**",num2,"=",result)
                     
                else:
                    if sele==6:
                         num1=int(input("""**********
primer numero: """))
                         num2=int(input("""**********
Segundo numero: """))
                         result= num1** (1/num2)
                         print (num1, "**", "1/", num2, "=", result)
                         
                    else:
                        if sele==7:
                             num1=int(input("""**********
primer numero: """))
                             num2=int(input("""**********
Segundo numero: """))
                             result= (num1**num2)+(num2**num1)
                             print (num1,"**",num2+num2,"**",num1,"=", result)
                             
                        else:
                            if sele==8:
                                num1=int(input("""**********
primer numero: """))
                                num2=int(input("""**********
Segundo numero: """))
                                result=(num1+num2)/2
                                print(num1,"+",num2/2,"=", result)
                                
                            else:
                                if sele==9:
                                     num1=int(input("""**********
primer numero: """))
                                     num2=int(input("""**********
Segundo numero: """))
                                     result=(num1<num2)(num1>num2)
                                     print(num1,"<",num2,"=",result)(num1,">",num2,"=",result)


                                    
                            
                    
                        
                    
                    
                    
                         
            
            
                    
    
    