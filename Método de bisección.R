e<-2.718281828459045090795598298427648842334747314453125;
f <- function(x) {
función <- (e**x) - (x**2);
return(función)
}
a <- -50;
b <- 40;
p <- 0;
Max <- 100;
Tolerancia <- 10e-16;
FA <- 0;
FP <-0;
i <- 1;
root_found <- FALSE;
print("Buscando raiz de la funcion ingresada por medio de bisección...")
  while (i <= Max & root_found == FALSE) {
    p = a + ((b - a) / 2);
    FP = f(x=p);
    FA = f(x=a);
    if (p == 0 + Tolerancia || p == 0 - Tolerancia || (b - a) / 2 < Tolerancia) {
    cat("Programa exitoso\n");
    num<-sprintf("La raiz vale %.16f",p);
    cat("La raiz vale:",num,"\n")
    cat("Fueron requeridas ", i , " iteraciones para llegar al resultado");
      root_found = TRUE
      break;
    }
    else {
      i = i + 1;
    }
    if (FA * FP > 0) {
      a = p;
      FA = FP;
    }
    else {
      b = p;
    }
  }
  if (root_found == FALSE) {
print("No se ha logrado encontrar una raíz");
print("Ejecución finalizada");
  }