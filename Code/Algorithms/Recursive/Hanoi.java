
public class Hanoi{

    public static void hanoi(int n){
        hanoi(n,"left","aux","right");
    }

    public static void hanoi(int height,String left, String aux, String right){

        if (height>0){
        
            hanoi(height-1,left,right,aux);
            System.out.println(left+ " => "+right);
            hanoi(height-1,aux,left,right);

        }

    }

    public static void main(String[] argv){

        hanoi(3);

    }

}
