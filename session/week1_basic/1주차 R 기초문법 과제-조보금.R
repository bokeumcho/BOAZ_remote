#1.	sum() 함수와 똑같은 기능을 하는 함수를 for문을 이용하여 작성하시오.
s<-function(x){
  sum=0
  for(i in x){
    sum=sum+i
  }
  return(sum)
}
s(c(1,3,5,4,7))

#2.	which.max() 함수와 똑같은 기능을 하는 함수를 for문, if문을 이용하여 작성하시오.
m<-function(x){
  if(length(x)==1){
    return(1)
    }
  else{
    a<-x[1]
    for (i in 2:length(x)){
      if(a<x[i]){
        a<-x[i]}
      else{
        a<-a
      }
    }
    return(match(a,x))
  }
}

m(c(14,-3,0,20,3))

#3.	for문을 이용하여 피보나치 수열을 작성하시오.
fibo <- function(n,x1,x2){
  for (i in 3:n){
    x3<-x1+x2
    x1<-x2
    x2<-x3
  }
  return(x3)
}

fibo(6,1,2)

#4.	1 + 1/(1+2) + 1/(1+2+3) +...+ 1/(1+2+..+N) 을 함수로 구현하시오.
g<-function(n){
  if(n==1){
    return(1)}
  else{b<-1
  for(i in 2:n){
    a<-1/sum(1,i)
    b<-b+a}
  return(b)
  }
}
g(10)
g(2)

#5.	for 문을 활용해서 (별탑)을 만들어주세요
for(a in 1:5){
  for(b in 1:a) cat("*")
  cat("\n")
}