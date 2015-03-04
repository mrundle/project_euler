public class p002 {

  public static void next_fib(int a, int b){
    //return a + b;
    int c = 2;
  }

  public static void main(String[] args){
    int a, b, c, sum;
    a = b = 1;
    c = 0;
    sum = 0;
    while(c < 4000000){
      c = a + b;
      a = b;
      b = c;
      if(c % 2 == 0) sum += c; 
    }
    System.out.println(sum);
    
    next_fib(1,2);
  }
}
