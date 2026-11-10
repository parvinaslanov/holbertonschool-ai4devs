import java.util.ArrayList;
import java.util.List;

public class Bug3 {

    // Intended: Remove all odd numbers from an ArrayList
    public static void removeOddNumbers(List<Integer> numbers) {
        // Bug: Modifying list during forward iteration causes skipped elements
        for (int i = 0; i < numbers.size(); i++) {
            if (numbers.get(i) % 2 != 0) {
                numbers.remove(i);
            }
        }
    }

    // Intended: Compare two user account strings for equality
    public static boolean checkAccountName(String inputName, String targetName) {
        // Bug: Using reference equality (==) instead of .equals() for string comparison
        return inputName == targetName;
    }

    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(3);
        list.add(4);
        list.add(5);
        
        removeOddNumbers(list);
        System.out.println("Filtered List: " + list);

        String name1 = new String("admin");
        String name2 = new String("admin");
        System.out.println("Names Match: " + checkAccountName(name1, name2));
    }
}
