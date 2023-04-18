import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public class SortingArray {
    public static void main(String[] args) {
        int[] intarray = new int[5];
        int[][] arr = new int[][]{{5, 40, 1}, {3, 50, 1}, {1, 30, 1}, {4, 20, 1}, {2, 10, 1}, {1, 20, 1}, {1, 20, 2}};
        String[] strArr = new String[]{"1", "2", "3"};
        int[] ints = Arrays.stream(strArr).mapToInt(Integer::parseInt).toArray();
        System.out.println("strArr = " + Arrays.toString(strArr));
        System.out.println("ints = " + Arrays.toString(ints));
        System.out.println("arr = " + Arrays.deepToString(arr));

        Arrays.sort(arr, Comparator.comparing((int[] o) -> o[0]).thenComparing((int[] o) -> -o[1]).thenComparing((int[] o) -> o[2]));
        System.out.println("arr = " + Arrays.deepToString(arr));

        int[] array = new int[]{5, 1, 2, 3, 4, 5, 3};
        int[] a1 = Arrays.copyOfRange(array, 2, 10);
        System.out.println("a1 = " + Arrays.toString(a1));
        int maxValue = Arrays.stream(array).max().getAsInt();
        int minValue = Arrays.stream(array).min().getAsInt();
        int sumValue = Arrays.stream(array).sum();
        array = Arrays.stream(array).distinct().toArray();
        System.out.println("array = " + Arrays.toString(array));
        System.out.println("sumValue = " + sumValue);
        System.out.println("maxValue = " + maxValue);
        System.out.println("minValue = " + minValue);


        List<Integer> list = new ArrayList<>(Arrays.stream(array).boxed().collect(Collectors.toList()));
        array = list.stream().mapToInt(i -> i.intValue()).toArray();
        System.out.println("list = " + list);
        System.out.println("array = " + Arrays.toString(array));

        //stack : add / removeLast
        //queue : add / removeFirst
        Deque<Integer> q = new ArrayDeque<>(Arrays.stream(array).boxed().collect(Collectors.toList()));
        System.out.println("q = " + q);
        System.out.println("마지막 제거 = " + q.removeLast());
        System.out.println("처음 제거 = " + q.removeFirst());
        System.out.println();

        String[] getGroupParti = {"zeebra", "cobra", "cobra", "dog"};

        // 이름, 갯수로 Group으로 묶어 담아줌
        Map<String, Long> map = Arrays.stream(getGroupParti)
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        System.out.println("map = " + map);
        System.out.println("cobra : " + map.get("cobra"));

        // 조건에 맞으면 true, 아니면 false의 list 형태로 담아줌
        Map<Boolean, List<String>> map2 = Arrays.stream(getGroupParti)
                .collect(Collectors.groupingBy(val -> val.length() > 3));

        System.out.println(map2);

    }
}