import java.util.*;
import java.util.stream.Collectors;

public class SortingArray {
    public static void main(String[] args) {
        int[][] arr = new int[][]{{5, 40, 1}, {3, 50, 1}, {1, 30, 1}, {4, 20, 1}, {2, 10, 1}, {1, 20, 1}, {1, 20, 2}};
        String[] strArr = new String[]{"1", "2", "3"};
        int[] ints = Arrays.stream(strArr).mapToInt(Integer::parseInt).toArray();
        System.out.println("strArr = " + Arrays.toString(strArr));
        System.out.println("ints = " + Arrays.toString(ints));
        System.out.println("arr = " + Arrays.deepToString(arr));

        Arrays.sort(arr, Comparator.comparing((int[] o) -> o[0]).thenComparing((int[] o) -> -o[1]).thenComparing((int[] o) -> o[2]));
        System.out.println("arr = " + Arrays.deepToString(arr));

        int[] array = new int[]{1, 2, 3};
        List<Integer> list = new ArrayList<>(Arrays.stream(array).boxed().collect(Collectors.toList()));
        array = list.stream().mapToInt(i -> i).toArray();
        System.out.println("list = " + list);
        System.out.println("array = " + Arrays.toString(array));

        //stack : push / pop
        //queue : add / remove
        Deque q = new ArrayDeque(Arrays.asList(array));

    }
}