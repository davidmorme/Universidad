data=c(0.06,0.8,0.3,0.03,1.2,0.7,0.92,0.41,0.23,0.32,1.1,1.9,0.4,1.31,1.2,0.7,1.4,0.9,0.93,0.27)
data=sort(data)

t=c(0,unique(data))
RHat=rep(0, length(t))

for(i in 1:length(RHat)){
  RHat[i]=sum(data>t[i])/length(data)
}

plot(t,RHat, type = "s")

RHat*20
