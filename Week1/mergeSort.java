import java.util.Arrays;

public class mergeSort{
    public static void main (String args []){
        int [] a = {3,6,8};
        int [] b= {8, 4, 10, 7,9, 2};
        System.out.println(Arrays.toString(mergeSort(b)));
    }

    public static int[] mergeSort(int[]list){
        if (list.length == 1){
            return list;
        }
        else {
            int midIndex = (int) Math.floor(list.length/2);
            int [] a = Arrays.copyOfRange(list, 0, midIndex);
            int[] b = Arrays.copyOfRange(list,midIndex,list.length);
            a = mergeSort(a);
            b = mergeSort(b);
            return merge(a, b);
        }
    }

    public static int[] merge(int []a , int []b){
        int [] ansArr = new int [a.length + b.length];
        int indexA = 0;
        int indexB = 0;
        int indexAns = 0;
        while (indexA < a.length && indexB < b.length){
            if(a[indexA] <= b[indexB]){
                ansArr[indexAns] = a[indexA];
                indexAns ++;
                indexA ++;
            }
            else if(a[indexA] > b[indexB]){
                ansArr[indexAns] = b[indexB];
                indexAns ++;
                indexB ++;
            }
        }
        while (indexA < a.length){
            ansArr[indexAns] = a[indexA];
            indexA ++;
            indexAns ++;
        }
        while(indexB < b.length){
            ansArr[indexAns] = b[indexB];
            indexB ++;
            indexAns ++;
        }
        return ansArr;
    }
 }
