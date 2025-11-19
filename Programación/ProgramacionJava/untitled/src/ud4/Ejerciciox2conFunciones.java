package ud4;

import java.util.Scanner;

public class Ejerciciox2conFunciones {
    static Scanner in = new Scanner(System.in);
    static final int TAM=3;
    public static void main(String[] args) {
        int[] nums = {2,3,4};
        rellenaArray(nums);
        int[] numsX2=multiplicaPorDos(nums);

        for (int i=0;i<TAM;i++) {
            System.out.println(numsX2[i]);
        }


    }

    public static int [] rellenaArray(int [] nums) {
        System.out.println("Introduce"+TAM+"numeros");
        for (int i=0;i<TAM;i++) {
            nums[i] = in.nextInt();
        }
    return nums;
    }
    public static int [] multiplicaPorDos(int[] nums) {
        int[] numsX2=new int [TAM];

        for (int i=0;i<TAM;i++) {
            numsX2[i] = nums[i] * 2;
        }
        return numsX2;


    }

}
