setwd("~/R/Projects/������ ������ � R/2 ���������� � R ����� 1/grants")

read_data <- function(){
  df <- data.frame()
  number <<- 0  # � ����� ������ ���������� number ���������� � ����� �������� �� ��������� �������
  for (i in dir(pattern = "*.csv")){
    temp_df <- read.csv(i)
    df <- rbind(temp_df, df)  # ��������� ������
    number <<- number + 1
  }
  print(paste(as.character(number), "files were combined"))
  return(df)
}

grants2 <- read_data()

