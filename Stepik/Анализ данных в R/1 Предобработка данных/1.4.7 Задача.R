?AirPassengers # справка о данных
str(AirPassengers) # структура данных

plot(AirPassengers) # plot the raw data
abline(reg=lm(AirPassengers~time(AirPassengers))) # fit a trend line
cycle(AirPassengers)
boxplot(AirPassengers~cycle(AirPassengers)) #Box plot across months to explore seasonal effects

a <- as.vector(AirPassengers)
a
good_months <- NA
for (i in 2:length(a)){
  if (a[i] > a[i-1]){
    good_months <- c(good_months, a[i])
  } else {
    NA
  }
}
good_months[2:length(good_months)]

good_months <- AirPassengers[-1][AirPassengers[-1] > AirPassengers[-144]]  # решение в одну строчку
good_months

a <- as.vector(AirPassengers)
